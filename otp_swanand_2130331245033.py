import random
import re
import smtplib
from twilio.rest import Client

class OTPSender:
    def __init__(self, account_sid, auth_token, twilio_num):
        self.client = Client(account_sid, auth_token)
        self.twilio_num = twilio_num

    @staticmethod
    def generate_otp(n=6):
        return ''.join(str(random.randint(0, 9)) for _ in range(n))

    @staticmethod
    def validate_mobile(mobile):
        return len(mobile) == 10 and mobile.isdigit()

    @staticmethod
    def validate_email(receiver):
        validation_condition = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return bool(re.search(validation_condition, receiver))

    def send_otp_over_mobile(self, target, otp):
        if self.validate_mobile(target):
            target = "+91" + target
            message = self.client.messages.create(
                body="Your OTP is " + otp + ". Valid for next 15 minutes.",
                from_=self.twilio_num,
                to=target
            )
            print(message.body)
            print("Check Phone! Sent to ", target)
        else:
            print("Enter a valid mobile number!!")

    @staticmethod
    def send_otp_over_email(sender, password, receiver, otp):
        body = "Your OTP is " + otp + ". Valid for next 15 minutes."
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, body)
        print("Mail sent - OTP: ", otp)

if __name__ == "__main__":
    print("Welcome to Random OTP sender!!\nHere, we send random OTPs to phone number and mails.\n")

    sender_email = "swanandbhuskute567@gmail.com"
    sender_password = "gvkguusgyahnhnfe"

    account_sid_value = 'AC1a01a4fd1cc7cdbb358e19fe12b9ce93'
    auth_token_value = '1fbcb17dfe649c3d4476b8d0330e07dc'
    twilio_number = '+15735944610'

    otp_sender = OTPSender(account_sid_value, auth_token_value, twilio_number)

    receiver_email = input("Enter mail: ")
    generated_otp = otp_sender.generate_otp(6)

    if otp_sender.validate_email(receiver_email):
        otp_sender.send_otp_over_email(sender_email, sender_password, receiver_email, generated_otp)
    else:
        print("Please enter a valid email!!")

    send_twilio = input("\nDo you want to send OTP via SMS: ")
    if send_twilio.lower() == "yes":
        target_mobile = input("Enter mobile: ")
        otp_sender.send_otp_over_mobile(target_mobile, generated_otp)
        print("\nOTP sending program ended\n")
    else:
        print("OTP sending program ended")

    # Program Ended
