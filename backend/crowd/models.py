from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()

class Campaign(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    goal_cents = models.IntegerField(default=0)
    owner_email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Donation(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='donations')
    donor_email = models.EmailField(blank=True)
    amount_cents = models.IntegerField()
    paypal_order_id = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=40, default='created')  # created, captured, refunded
    created_at = models.DateTimeField(auto_now_add=True)

class Subscription(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='subscriptions')
    subscriber_email = models.EmailField()
    paypal_subscription_id = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=40, default='active')  # active, cancelled
    created_at = models.DateTimeField(auto_now_add=True)

class Payout(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='payouts')
    amount_cents = models.IntegerField()
    paypal_batch_id = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=40, default='pending') # pending, SUCCESS, DENIED
    created_at = models.DateTimeField(auto_now_add=True)
