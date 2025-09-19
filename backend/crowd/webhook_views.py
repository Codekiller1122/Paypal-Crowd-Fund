import os, json, requests
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


def verify_paypal_webhook(request):
    '''Verify PayPal webhook signature using VERIFY-WEBHOOK-SIGNATURE API.'''
    transmission_id = request.META.get('HTTP_PAYPAL_TRANSMISSION_ID') or request.POST.get('transmission_id')
    transmission_time = request.META.get('HTTP_PAYPAL_TRANSMISSION_TIME') or request.POST.get('transmission_time')
    cert_url = request.META.get('HTTP_PAYPAL_CERT_URL') or request.POST.get('cert_url')
    auth_algo = request.META.get('HTTP_PAYPAL_AUTH_ALGO') or request.POST.get('auth_algo')
    transmission_sig = request.META.get('HTTP_PAYPAL_TRANSMISSION_SIG') or request.POST.get('transmission_sig')
    webhook_id = os.environ.get('PAYPAL_WEBHOOK_ID','')
    if not webhook_id:
        return False, 'no webhook id configured'
    try:
        body = request.body.decode()
        token = paypal_token()
        headers = {'Content-Type':'application/json','Authorization':f'Bearer {token}'}
        payload = {
            'transmission_id': transmission_id,
            'transmission_time': transmission_time,
            'cert_url': cert_url,
            'auth_algo': auth_algo,
            'transmission_sig': transmission_sig,
            'webhook_id': webhook_id,
            'webhook_event': json.loads(body)
        }
        r = requests.post(f"{settings.PAYPAL_API_BASE}/v1/notifications/verify-webhook-signature", headers=headers, json=payload)
        if r.status_code==200 and r.json().get('verification_status')=='SUCCESS':
            return True, ''
        return False, r.text
    except Exception as e:
        return False, str(e)

from .models import Donation, Subscription, Payout

# basic webhook receiver - in production verify transmission via PayPal webhook-ID and signatures
@csrf_exempt
def paypal_webhook(request):
    try:
        # verify signature
        ok, msg = verify_paypal_webhook(request)
        if not ok:
            # reject if verification fails
            return HttpResponse(status=400)
        event = json.loads(request.body.decode())
    except Exception as e:
        return HttpResponse(status=400)
    kind = event.get('event_type')
    data = event.get('resource', {})
    # handle common events
    if kind == 'CHECKOUT.ORDER.APPROVED' or kind == 'PAYMENT.CAPTURE.COMPLETED':
        order_id = data.get('id') or data.get('supplementary_data', {}).get('related_ids', {}).get('order_id')
        # mark donation captured if exists
        if order_id:
            Donation.objects.filter(paypal_order_id=order_id).update(status='captured')
    elif kind == 'BILLING.SUBSCRIPTION.ACTIVATED' or kind == 'BILLING.SUBSCRIPTION.CREATED':
        sub_id = data.get('id')
        Subscription.objects.filter(paypal_subscription_id=sub_id).update(status=data.get('status','active'))
    elif kind == 'PAYMENT.PAYOUTSBATCH.DENIED' or kind == 'PAYMENT.PAYOUTSBATCH.SUCCESS':
        batch_id = data.get('batch_header', {}).get('payout_batch_id')
        if batch_id:
            Payout.objects.filter(paypal_batch_id=batch_id).update(status=data.get('batch_header', {}).get('batch_status',''))
    # respond 200
    return JsonResponse({'status':'ok'})
