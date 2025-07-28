print("""Choices are:
    1. Send Email
    2. Send Whatsapp Message
    3. Send sms
    4. Exit
""")
while(True):    
    choice=int(input("Enter your Choice (1-4):"))
    if choice==1:
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart


        sender = input("Enter your Gmail address: ")
        password = input("Enter your Gmail App Password: ")
        to = input("Enter recipient email: ")
        subject = input("Enter subject: ")
        msg = input("Enter message: ")

        try:
   
            message = MIMEMultipart()
            message["From"] = sender
            message["To"] = to
            message["Subject"] = subject
            message.attach(MIMEText(msg, "plain"))

            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender, password)
                server.send_message(message)

            print("Email sent successfully!")

        except Exception as e:
            print(f"Failed to send email: {str(e)}")
    elif choice==2:
        import pywhatkit as kit
        import datetime

        phone_number = input("Enter phone number with country code (e.g., +91XXXXXXXXXX): ")
        message = input("Enter your message: ")


        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute + 1  

        try:
            print("Opening WhatsApp Web...")
            kit.sendwhatmsg(phone_no=phone_number, message=message, time_hour=hour, time_min=minute)
            print("Message scheduled successfully!")

        except Exception as e:
            print(f"Failed to send message: {str(e)}")
    elif choice==3:
        from twilio.rest import Client


        account_sid = 'AC235cb59aa9b6ea74f3a5eacd50650797'
        auth_token = '0a5a298c0d8eeab10c1b6c0beb564ccc'
        twilio_number = '+17755499097'


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
    else:
        break


