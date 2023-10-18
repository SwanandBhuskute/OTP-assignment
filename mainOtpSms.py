from twilio.rest import Client
import codesOtpSms as codes
import random
client = Client(codes.account_sid, codes.auth_token)

message = client.messages.create(

    body = "Your OTP is " + str(random.randint(100000, 999999)) + ". Valid for next 15 minutes.",
    from_= codes.twilio_num,
    to=codes.target

)

print(message.body)
print("Check Phone!")