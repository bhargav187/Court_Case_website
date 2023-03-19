from twilio.rest import Client

# Your Account SID and Auth Token from twilio.com/console
account_sid = 'AC5e7dc3d64249cfc611d4a96d7c60628c'
auth_token = '0a4745fbe0c7d21741ec4c896a8f6e04'
client = Client(account_sid, auth_token)

# Your Twilio phone number
from_number = '+19134236819'

# The phone number you want to send the message to
to_number = '+917021111781'

# The message you want to send
message = ' Hello Kunal ! Welcome to Qspider '

# Send the message
message = client.messages.create(
    to=to_number,
    from_=from_number,
    body=message)

print(f"Reminder message sent to {to_number}")
