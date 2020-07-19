import csv,smtplib
from settings import SENDER_EMAIL,SENDER_PASSWORD

ACCEPTED_MSG='''
Hi {},
We are pleased to let you know you are accepted.
Your coach is {}.

Thank You,
TEAM WORKS

'''
REJECTED_MSG='''
Hi {},
We are sorry to tell you that you are rejected.


Thank You,
TEAM WORKS

'''
with open('applications.csv') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')
    next(csv_reader)#MOVE ITERABLE POINTER of csv _reader TO NEXT ROW
    smtp=smtplib.SMTP('smtp.gmail.com')#SET UP CONNECTION TO Gmail's SMTP SERVER.

    smtp.ehlo()#Identify Client To SERVER

    smtp.starttls()# Start TLS (Transport Layer Security)ENCRYPTION
    smtp.ehlo() #The client SHOULD send an EHLO command as the first command after a successful TLS action.
    smtp.login(SENDER_EMAIL,SENDER_PASSWORD)#Login With Details
    for row in csv_reader:
         name,email,accepted,coach,language=row
         if accepted =='Yes':
           msg=ACCEPTED_MSG.format(name,coach)
           subj="Workshop Accepted"
         else:
           msg=REJECTED_MSG.format(name)
           subj = "Workshop Rejected"
         email_msg = "Subject:{} \n \n{}".format(subj, msg)#ADD Subject To Email
         smtp.sendmail(SENDER_EMAIL,email,email_msg)

smtp.quit()#Don't forget to Cut Connection.
