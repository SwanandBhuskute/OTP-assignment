import random
import re
import smtplib
from twilio.rest import Client

class Mobile:
    @staticmethod
    def validate_mobile(mobile):
        return len(mobile) == 10 and mobile.isdigit()

    @staticmethod
    def send_otp_over_mobile(client, twilio_num, target, otp):
        if Mobile.validate_mobile(target):
            target = "+91" + target
            message = client.messages.create(
                body="Your OTP is " + otp + ". Valid for next 15 minutes.",
                from_=twilio_num,
                to=target
            )
            print(message.body)
            print("Check Phone! Sent to ", target)
        else:
            print("Enter a valid mobile number!!")

class Email:
    @staticmethod
    def validate_email(receiver):
        validation_condition = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return bool(re.search(validation_condition, receiver))

    @staticmethod
    def send_otp_over_email(sender_email, sender_password, receiver, otp):
        if Email.validate_email(receiver):
            body = "Your OTP is " + otp + ". Valid for next 15 minutes."
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver, body)
            print("Mail sent - OTP: ", otp)
        else:
            print("Please enter a valid email!!")

class OTPServices:
    def _init_(self, account_sid, auth_token, twilio_num, sender_email, sender_password):
        self.client = Client(account_sid, auth_token)
        self.twilio_num = twilio_num
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.mobile_service = Mobile()
        self.email_service = Email()

    def send_otp(self, receiver_email, send_twilio=True, target_mobile=None):
        generated_otp = self.generate_otp(6)

        if send_twilio:
            self.mobile_service.send_otp_over_mobile(self.client, self.twilio_num, target_mobile, generated_otp)

        self.email_service.send_otp_over_email(self.sender_email, self.sender_password, receiver_email, generated_otp)

    @staticmethod
    def generate_otp(n=6):
        return ''.join(str(random.randint(0, 9)) for _ in range(n))

if _name_ == "_main_":
    print("Welcome to Random OTP sender!!\nHere, we send random OTPs to phone number and mails.\n")

    account_sid_value = 'AC1a01a4fd1cc7cdbb358e19fe12b9ce93'
    auth_token_value = '1fbcb17dfe649c3d4476b8d0330e07dc'
    twilio_number = '+15735944610'
    sender_email = "swanandbhuskute567@gmail.com"
    sender_password = "gvkguusgyahnhnfe"

    otp_services = OTPServices(account_sid_value, auth_token_value, twilio_number, sender_email, sender_password)

    receiver_email = input("Enter mail: ")
    send_twilio = input("\nDo you want to send OTP via SMS: ")

    if send_twilio.lower() == "yes":
        target_mobile = input("Enter mobile: ")
        otp_services.send_otp(receiver_email, send_twilio=True, target_mobile=target_mobile)
    else:
        otp_services.send_otp(receiver_email, send_twilio=False)

    print("\nOTP sending program ended\n")
    # Program Ended
