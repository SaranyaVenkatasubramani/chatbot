# email.py
import random
import smtplib
from email.message import EmailMessage

def send_otp(email_address):
    otp = str(random.randint(100000, 999999))
    msg = EmailMessage()
    msg.set_content(f"Your OTP is: {otp}")
    msg['Subject'] = 'Chatbot 2FA Verification'
    msg['From'] = 'your_email@gmail.com'   # replace with your email
    msg['To'] = email_address

    # Send email via Gmail SMTP
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('your_email@gmail.com', 'app_password')  # use App Password
    server.send_message(msg)
    server.quit()
    return otp
