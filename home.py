#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37-32\python.exe

from import_modules import *

#THE ABOVE SECTION SHOULD EXIST AT THE TOP OF EVERY PAGE

#####################################################################################
def home_page_display():

    matches = Database_requests.get_number_of_matches()

    for fulfilled_mathces in matches:

        fulfilled_mathces = matches[0]['fulfilled_mathces']

    print('''<center>
    <h2>Building a community starts here!</h2>
    <div class="jumbotron">
        <h1 class="display-4">Building a community starts here!</h1>
        <p class="lead">We connect those who need with those who have.</p>
        <hr class="my-4">
        <p>How can we best help you?</p>
        <div class="btn-group" role="group" aria-label="Basic example">
            <a class="btn btn-group-lg btn-secondary" href="/humanizeus/add_need.py" role="button">I need support</a>
            <a class="btn btn-group-lg btn-secondary" href="/humanizeus/add_support.py" role="button">I want to donate</a>
            <a class="btn btn-group-lg btn-secondary" href="/humanizeus/for_organizations.py" role="button">I am an organization</a>
        </div>
    </div>
    <br>
    <br>
    <h3>We have proudly supported %s newly housed people so far!</h3></center>
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
