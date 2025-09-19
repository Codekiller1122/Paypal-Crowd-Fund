from django.urls import path
from . import views, webhook_views
urlpatterns = [
    path('campaigns/', views.campaigns_list),
    path('donations/', views.donations_list),
    path('subscriptions/', views.subscriptions_list),
    path('payouts/', views.payouts_list),
    path('paypal/create-order/', views.create_order),
    path('paypal/capture-order/', views.capture_order),
    path('paypal/create-subscription/', views.create_subscription_plan),
    path('paypal/subscription-return/', views.subscription_return),
    path('paypal/create-payout/', views.create_payout),

path('auth/register/', views.register),
path('auth/login/', views.login_view),
path('auth/logout/', views.logout_view),
path('me/donations/', views.my_donations),
path('me/subscriptions/', views.my_subscriptions),
path('paypal/refund/', views.refund_payment),
path('paypal/cancel-subscription/', views.cancel_subscription),

    path('paypal/create-order/approve/', views.create_order),  # alias
    # webhook endpoint
    path('paypal/webhook/', webhook_views.paypal_webhook),
]
