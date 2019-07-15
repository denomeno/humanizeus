#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe

from import_modules import *

#THE ABOVE SECTION SHOULD EXIST AT THE TOP OF EVERY PAGE

#####################################################################################
def home_page_display():

    print('''
    <h2>Building a community starts here!</h2>
    <button type="button" style="height:200px;width:200px" align="left">I need support </button>
    <button type="button" style="height:200px;width:200px" align="center">I want to donate </button>
    <button type="button" style="height:200px;width:200px" align="right">I am an organization </button>

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
