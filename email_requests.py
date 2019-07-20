#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe

from import_modules import *

#THE ABOVE SECTION SHOULD EXIST AT THE TOP OF EVERY PAGE

####################################################################################


class Email_requests:

    def __init__(self):
        #SETUP OUTGOING SMTP SERVER

        #server settings - change this part
        #----------------------------------
        server = "smtpout.secureserver.net"
        port = 456
        #----------------------------------

        self.server_outgoing = smtplib.SMTP_SSL(server, port)#setup smtp server connection

        #SETUP INCOMING IMAP SERVER - FOR ATTACHMENT RETRIEVAL
        #self.server_incoming = imaplib.IMAP4_SSL('imap.secureserver.net', 993)

        self.email_object = None #to be set if email file is generated

    def login(self):

        #--- Email configuration and login--

        MY_ADDRESS = 'contact@humanize-us.org'
        #PASSWORD = 'Welcome2018!'

        #LOGIN TO OUTGOING CONNECTION
        #server = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)#setup smtp server connection
        self.server_outgoing.ehlo()
        self.server_outgoing.login(MY_ADDRESS, PASSWORD) #login through connection

        #LOGIN INCOMING CONNECTION
        #self.server_incoming.login(MY_ADDRESS, PASSWORD)
        #self.server_incoming.select() #select default mailbox

#------------------

    def create_email(self, to, subject, message_body):
        #input variables:
        #`from`: String
        #`to`: list
        #`subject` : string
        #`message`: string

        email_from = "contact@humanize-us.org"

        #3. Create the email

        # create a message
        msg = MIMEMultipart()

        # setup the parameters of the message
        msg['From']= email_from
        msg['To']= "%s" %'; '.join(to)#join() intakes a list of strings

        msg['Subject']= subject #input from the email_request call, which will be the main function used to generate emails

        #add email body


        msg.attach(MIMEText(message_body, 'html'))#`message_body` is a string to be input from the email_request call

        # store the email object in the main object
        self.email_object = msg


    def send_email(self):

        # send the message via the server set up earlier.
        self.server_outgoing.send_message(self.email_object)

        # Terminate the SMTP session and close the connection
        self.server_outgoing.quit()
