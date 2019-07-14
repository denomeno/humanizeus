#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe

from import_modules import *

#THE ABOVE SECTION SHOULD EXIST AT THE TOP OF EVERY PAGE

#####################################################################################
def home_page_display():

    print('''
    <h2>Building a community starts here!</h2>
    <button type="button">I need support align="left"</button>
    <button type="button">I want to donate align="center"</button>
    <button type="button">I am an organization align="right"</button>

    ''')

 #####################################################################################

if __name__ == "__main__":

    print_headers()
    print_top_of_page()
    print_menu()
    #-----------


    form = cgi.FieldStorage()
    print_form_data(form)
    #-----------
    home_page_display()


    #-----------
    print_bottom_of_page()
