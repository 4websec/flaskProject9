import requests
from .models import User
from twilio.rest import Client
from flask import current_app as app
import os

# Load Twilio Credentials and Initialize Twilio Client
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
from_phone_number = "+18447356172"  # Replace with your Twilio number
client = Client(account_sid, auth_token)


def daily_check():
    with app.app_context():
        users = User.query.all()
        for user in users:
            perform_check(user)


def perform_check(user):
    url = "https://sentry.cordanths.com/Sentry/WebCheckin/Lookup"
    data = dict(last_name=user.last_name, drug_testing_phone=user.drug_testing_phone, ivr_code=user.ivr_code)
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            # Assuming 'Valid' is a placeholder, replace with actual success condition
            if "Valid" in response.text:
                send_sms(user, "Your daily check-in is complete.", client)
            else:
                send_sms(user, "Your daily check-in is incomplete.", client)
        else:
            send_sms(user, "An error occurred while performing your daily check-in.", client)
    except requests.RequestException as e:
        send_sms(user, f"An exception occurred: {e}", client)


def send_sms(user, message, twilio_client):
    twilio_client.messages.create(
        body=message,
        from_=from_phone_number,
        to=user.drug_testing_phone
    )
