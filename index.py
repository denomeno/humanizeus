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
    <img src="humanizelogo.png" alt="HumanizeUs" style="width:320px;height:200px; display: inline-block;
    vertical-align: top;">
    """)


#####################################################################################
def print_top_of_page():

    print("""
    <html>
      <head>
        <meta charset='utf-8'>
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>

        .a { color: #ffffff; } 

        body {
        background-color: white;
        font-size:1.3vw
        }

        button[type=home_button] {
        color: #C0C0C0;
        background-color: transparent;
        border: 5px solid #FF0000;
        border-radius: 15px;
        text-transform: uppercase;
        font-size: 2vw
        }

        </style>
      </head>
      <body style="font-family:Bookman;color:black;">
    """)


#####################################################################################
def print_menu():

    print('''
    <style>

    ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background-color: #333;
    }

    li {
    float: left;
    }

    li a {
    display: block;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
    }

    li a:hover {
    background-color: #111;
    }
    </style>
    ''')


    print('''
    <ul>
        <li><a href='/humanizeus/home.py'><span>Home</span></a></li>
        <li><a href='/humanizeus/mission.py'><span>Our Mission</span></a></li>
        <li><a href='/humanizeus/map.py'><span>Map</span></a></li>
        <li><a href='/humanizeus/add_need.py'><span>Add Need</span></a></li>
        <li><a href='/humanizeus/add_support.py'><span>Add Support</span></a></li>
        <li><a href='/humanizeus/for_organizations.py'><span>For Organizations</span></a></li>
        <li><a href='/humanizeus/contact.py'><span>Contact Us</span></a></li>
    </ul>
    <br>
    ''')


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
