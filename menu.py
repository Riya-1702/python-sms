from twilio.rest import Client
account_sid = ''
auth_token = ''
twilio_number = ''
to_number = input("Enter recipient phone number (with country code): ")
message_body = input("Enter the SMS message: ")
try:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                body=message_body,
                from_=twilio_number,
                to=to_number
            )
    print(f"SMS sent! Message SID: {message.sid}")
except Exception as e:
    print(f"Failed to send SMS: {str(e)}")
   

