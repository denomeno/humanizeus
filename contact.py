#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe

from import_modules import *

#THE ABOVE SECTION SHOULD EXIST AT THE TOP OF EVERY PAGE
#####################################################################################

def process_contact_form(form):

    if form['form_name'].value == 'Contact':

        #gather form variables
        email_to = form['email'].value
        name = form['name'].value
        message = form['message'].value


        #insert into database
        Database_requests.insert_into_contact_us(name, email_to, message)


        #setup email contents
        subject = "Your contact inquery"

        message_body = """
        <p>We received the following message from you:</p>
        <br>
        %s
        <br>
        ----<br>
        We will contact you shortly.<br>
        <br>
        Humanizeus Team

        """ %(message)


        #create and send the email
        email_object = Email_requests()
        email_object.login()
        email_object.create_email(email_to , subject, message_body)
        email_object.send_email()
        return

    else: #if form is not contact form
        return


#####################################################################################
def contact_form():
    print('''
    <h3>We'd love to have a conversation, reach out to us.</h3>
    <form method=POST>
        <input type="hidden" name="form_name" value="Contact"/>
        Email:<br>
        <input name="email" type="email"><br>
        Name:<br>
        <input name="name" type="text"><br>
        What is on your mind?:<br>
        <input name="message" type="text"><br>
    <input type='submit' value='Submit'>
    </form>
    <h4>Thank you!<h4>
    ''')

#####################################################################################
#CONTROLLER FUNCTIONS

if __name__ == "__main__":

     print_headers()
     print_top_of_page()
     print_menu()

     form = cgi.FieldStorage()
     print_form_data(form)
     #-----------

     contact_form()

     if form:
         process_contact_form(form)

     #-----------
     print_bottom_of_page()
