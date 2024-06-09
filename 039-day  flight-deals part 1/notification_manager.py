from twilio.rest import Client

TWILIO_SID = "ACb18cf2014d34e5c4fd3b365892a06127"
TWILIO_AUTH_TOKEN = "833494a09a7d81a76568ef2a490b763b"
TWILIO_VIRTUAL_NUMBER = "+19164720365"
TWILIO_VERIFIED_NUMBER = "+91 63794 68663"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def sent_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER
        )
        print(message.sid)