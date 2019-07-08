#!"C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe"

from import_modules import *

#THE ABOVE SECTION SHOULD EXIST AT THE TOP OF EVERY PAGE
#####################################################################################

def contact_form():
    print('''
    <h3>We'd love to have a conversation, reach out to us.</h3>
    Email:<br>
    <input name="email" type="email"><br>
    Name:<br>
    <input name="name" type="text"><br>
    What is on your mind?:<br>
    <input name="words" type="text"><br>
    <h4>Thank you!<h4>
    ''')

#####################################################################################
#CONTROLLER FUNCTIONS

if __name__ == "__main__":

     #print_headers()
     print_top_of_page()
     print_menu()
     #-----------

     contact_form()

     #-----------
     print_bottom_of_page()
