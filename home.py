#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe

from import_modules import *

#THE ABOVE SECTION SHOULD EXIST AT THE TOP OF EVERY PAGE

#####################################################################################
def home_page_display():

    matches = Database_requests.get_number_of_matches()

    for fulfilled_mathces in matches:

        fulfilled_mathces = matches[0]['fulfilled_mathces']

    print('''
    <h2>Building a community starts here!</h2>
    <button type="button" style="height:200px;width:200px" align="left"><a href='/humanizeus/add_need.py'><b>I need support</b></a></button>
    <button type="button" style="height:200px;width:200px" align="center"><a href='/humanizeus/add_support.py'><b>I want to donate</b></a></button>
    <button type="button" style="height:200px;width:200px" align="right"><a href='/humanizeus/for_organizations.py'><b>I am an organization</b></a></button>

    <br>
    <br>
    <h3>We have proudly supported %s newly housed people so far!</h3>
    ''' % fulfilled_mathces ) #ADD MATCH COMPLETE COUNT -- len(match_id)


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
