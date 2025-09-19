from django.contrib import admin
from .models import Campaign, Donation, Subscription, Payout
@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('id','title','slug','goal_cents','owner_email','created_at')
@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('id','campaign','donor_email','amount_cents','status','created_at')
@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id','campaign','subscriber_email','paypal_subscription_id','status','created_at')
@admin.register(Payout)
class PayoutAdmin(admin.ModelAdmin):
    list_display = ('id','campaign','amount_cents','status','paypal_batch_id','created_at')
