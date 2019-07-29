#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe

from import_modules import *

#THE ABOVE SECTION SHOULD EXIST AT THE TOP OF EVERY PAGE
#####################################################################################
#GENERRIC HEADER FUNCTIONS - USED IN ALL PAGES
#####################################################################################
def print_form_data(form):
    '''Display the form data for debugging purposes.
    '''
    # print out the form data (for debugging purposes)
    print('Form data:<br>')

    print('<table>')
    keys = list(form.keys())
    keys.sort()
    # go through all keys:
    for k in keys:

        print('''<tr>
                    <td>%s</td>
                    <td>%s</td>
                </tr>''' % (k, form[k]))


    print('</table><hr>')

#####################################################################################
def print_headers():
    print("Content-type:text/html\r\n\r\n")
    print("""
    <title>HumanizeUs</title>
    <nav class="navbar navbar-light bg-light">
      <a class="navbar-brand" href="#">
        <img src="humanizelogo.png" alt="HumanizeUs" width="30" height="30" class="d-inline-block align-top" alt="">
        HumanizeUs
      </a>
    </nav>
    """)




#####################################################################################
def print_top_of_page():

    print("""
    <html>
      <head>
        <meta charset='utf-8'>
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <style>

        .a { color: #ffffff; }

        body {
        background-color: white;
        font-size:1.3vw
        }

        </style>
      </head>
      <body style="font-family:Bookman;color:black;">
    """)


#####################################################################################
def print_menu():


    print("""
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="/humanizeus/home.py">
        <img src="humanizelogo.png" alt="HumanizeUs" width="30" height="30" class="d-inline-block align-top" alt="">
        HumanizeUs</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div class="navbar-nav">
          <a class="nav-item nav-link active" href="/humanizeus/mission.py">Mission<span class="sr-only">(current)</span></a>
          <a class="nav-item nav-link" href="/humanizeus/map.py">Map</a>
          <a class="nav-item nav-link" href="/humanizeus/add_need.py">Add Need</a>
          <a class="nav-item nav-link" href="/humanizeus/add_support.py">Add Support</a>
          <a class="nav-item nav-link" href="/humanizeus/for_organizations.py">For Organizations</a>
          <a class="nav-item nav-link" href="/humanizeus/contact.py">Contact Us</a>
        </div>
      </div>
    </nav>
    """)

#####################################################################################

def print_bottom_of_page():
    '''Print the bottom of the HTML page.'''

    #now_time = datetime.now(timezone('US/Eastern'))

    print('''
    <br>
    <br>
    <br>
    <hr>
    <div class="b_footer" style="background-color:#e5e5e5;text-align:left;padding:10px;margin-top:7px;">
        <u><b>HumanizeUs</b></u><br>
        Return to the <a href="/humanizeus/home.py">home page</a>.<br>
        Enter <a href="/humanizeus/admin.py">admin portal</a>.</p>
    </div>
    </body>
    </html>
    ''')

 ####################################################################################


if __name__ == "__main__":

    print_headers()
    print_top_of_page()
    print_menu()


    print_bottom_of_page()
