from rest_framework import serializers
from .models import Campaign, Donation, Subscription, Payout
class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'
class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
class PayoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payout
        fields = '__all__'
