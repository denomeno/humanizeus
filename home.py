#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe

from import_modules import *

#THE ABOVE SECTION SHOULD EXIST AT THE TOP OF EVERY PAGE

#####################################################################################
def home_page_display():

    print('''
    <h2>Building a community starts here!</h2>
    <button type="button" style="font-size: 20px height:200px;width:200px" align="left"><a href='/humanizeus/add_need.py'>I need support</a></button>
    <button type="button" style="font-size: 20px height:200px;width:200px" align="center"><a href='/humanizeus/add_support.py'>I want to donate</a></button>
    <button type="button" style="font-size: 20px height:200px;width:200px" align="right"><a href='/humanizeus/for_organizations.py'>I am an organization</a></button>

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
