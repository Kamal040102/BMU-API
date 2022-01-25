from email.mime.text import MIMEText
import string
import random
import smtplib
from email.mime.multipart import MIMEMultipart

def createSendOTP(username, email):
   lower = string.ascii_lowercase
   upper = string.ascii_uppercase
   num = string.digits
   var = lower + upper + num
   code = ''.join(random.sample(var,6))

   sender = "coding.coding.everyday@gmail.com"
   receiver = email
   password = 'missajibsharma040102'

   message = f'''
   <html>
   <head></head>
   <body>
      <hr>
      <h1 align='center'>BMU API</h1>
      <hr>
      <h4>Hiii {username},</h4>
      <h4>Your OTP for BMU API Registration is {code}.</h4>
      <h5>Don't share this code with anyone else.</h5>
      <h5 align='center'>This code is valid for 10 mins only.</h5>
      <hr>
      <h4 align='center'>Thanks for using BMU API.</h4>
      <hr>
   </body>
   </html>
   '''

   msg = MIMEMultipart()
   msg['From'] = sender
   msg['To'] = receiver
   msg['Subject'] = "OTP | BMU API"
   body = MIMEText(message, 'html')
   msg.attach(body)
 
   try:
      smtpObj = smtplib.SMTP('smtp.gmail.com',587)
      smtpObj.ehlo()
      smtpObj.starttls()
      smtpObj.ehlo()
      smtpObj.login(sender, password)
      smtpObj.sendmail(sender, receiver, msg.as_string())    
      res = f"Mail has been sent Successfully on email {email}"   
      smtpObj.quit()
   except Exception as e:
      res = e

   return code, res

# createSendOTP("kamal","kamal5201ks@gmail.com")