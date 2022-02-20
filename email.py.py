from ast import For
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


from_addr=input("enter Sender's Email ::  ")
recv_num=int(input("how many recievers do you want   :: "))
to_addr=[]
for i in range(0,recv_num):
    to_eml=input("enter reciever's "+str(i+1)+" email address::  ")
    to_addr.append(to_eml)
    

msg=MIMEMultipart()
msg['From']=from_addr
msg['To']=" ,".join(to_addr)
subj=input("enter the subject of the email :: ")
msg['subject']=subj    
body=input("enter the body of the email ::   ")

msg.attach(MIMEText(body,'plain'))
email=from_addr
password='5380jack'

mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(email,password)
text=msg.as_string()
mail.sendmail(from_addr,to_addr,text)
    



print("email was sent successfully")
mail.quit()