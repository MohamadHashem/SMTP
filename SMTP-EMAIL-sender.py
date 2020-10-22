import smtplib #importing library for SMTP
import datetime
# here is the sender email address 
sender = ""  #type the email here 
# Enter receiver address
receiver = input(str("Type Email you want send to : ")) 
# you need to enter sender email password to login 
passd = input(str("Type your password  "))
server_ssl=smtplib.SMTP_SSL('smtp.gmail.com',465)
server_ssl.ehlo()
#server_ssl.starttls()
#login to sender email address after typing the password
server_ssl.login(sender,passd)
print("login success")
#the message and subject that will be send
date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )
#enter the subject of email
sub=input(str("Type your subject:  "))
#type the content of the message 
textmsg=input(str("Type your message:  "))
msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( sender,receiver,sub,date,textmsg )
#the sender email send the message to the reciever email
server_ssl.sendmail(sender,receiver,msg)
print("Thank you your message was send to: ",receiver)
#quit the server 
server_ssl.quit()