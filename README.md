    # PayPal Crowdfunding Platform

This project demonstrates a complete PayPal integration for a crowdfunding-style app. Features:

- One-time donations using PayPal Orders API (server-side create order -> approve -> capture)
- Recurring donations via PayPal Subscriptions (create product & plan -> subscription -> approval)
- Webhook endpoint to receive PayPal events (captures, subscriptions, payouts)
- Payouts to campaign owners via PayPal Payouts API

## Quickstart
1. unzip and cd into project
2. Set backend/.env with PAYPAL_CLIENT_ID and PAYPAL_SECRET and PUBLIC_BASE_URL
3. Start services: `docker-compose up --build`
4. In backend container:
   ```bash
   python manage.py migrate
   python manage.py seed_campaigns
   ```
5. Use the React frontend at http://localhost:3000 to try donations and subscriptions.

## PayPal Setup
- Use sandbox credentials and sandbox accounts. Set PAYPAL_API_BASE to https://api-m.sandbox.paypal.com and configure webhook URL in PayPal developer dashboard to https://<PUBLIC_BASE_URL>/api/paypal/webhook/
- For Payouts, enable Payouts in your sandbox account and use the recipient email addresses configured on campaigns.

## Security Notes
- Verify webhook signatures in production! This starter does not verify for simplicity.
- Persist PayPal customer and subscription IDs mapped to users in production.

## Use Case Idea
This app is useful for charities, community groups, or creators who want to accept both one-time and recurring donations via PayPal and then pay out funds to campaign owners.

If you want, I can:
- Add server-side verification of webhooks using PayPal's transmission verification.
- Implement UI flows to show subscription status and donation history per campaign.
- Add admin endpoints for issuing refunds via the PayPal API.
