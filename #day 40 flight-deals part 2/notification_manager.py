from twilio.rest import Client

TWILIO_SID = "ACb18cf2014d34e5c4fd3b365892a06127"
TWILIO_AUTH_TOKEN = "833494a09a7d81a76568ef2a490b763b"
TWILIO_VIRTUAL_NUMBER = "+19164720365"
TWILIO_VERIFIED_NUMBER = "+91 63794 68663"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    # def send_emails(self, emails, message):
    #     with smtplib.SMTP(EMAIL_PROVIDER_SMTP_ADDRESS) as connection:
    #         connection.starttls()
    #         connection.login(MY_EMAIL, MY_PASSWORD)
    #         for email in emails:
    #             connection.sendmail(
    #                 from_addr=MY_EMAIL,
    #                 to_addrs=email,
    #                 msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
    #             )
