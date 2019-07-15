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
    <h1>HumanizeUs</h1>
    <h3>A Neighborly Exchange</h3>
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

          h1 {
            color: red
              font-family: "Bookman";
          }

          body {
            background-color: white;
            clear: both
          }

          footer {
          color: black;
          text-align: left;
          padding: 2px 10px 0px 0px;
          }

        </style>
      </head>
      <body style="font-family:Bookman;color:black;">
    """)


#####################################################################################
def print_menu():

    """
    <head>
    <link rel="stylesheet" href="styles.css">
    <script src="http://code.jquery.com/jquery-latest.min.js" type="text/javascript"></script>
    <script src="script.js"></script>
    <title>CSS MenuMaker</title>
    </head>
    """

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

<body>
<div id='cssmenu'>
<ul>
   <li class='active'><a href='/humanizeus/home.py'><span>Home</span></a></li>
   <li><a href='/humanizeus/mission.py'><span>Our Mission</span></a></li>
   <li class='last'><a href='/humanizeus/map.py'><span>Map</span></a></li>
   <li><a href='/humanizeus/add_need.py'><span>Add Need</span></a></li>
   <li><a href='/humanizeus/add_support.py'><span>Add Support</span></a></li>
   <li><a href='/humanizeus/for_organizations.py'><span>For Organizations</span></a></li>
   <li><a href='/humanizeus/contact.py'><span>Contact Us</span></a></li>
</ul>
</div>
</body>
<br>

''')


#####################################################################################

def print_bottom_of_page():
    '''Print the bottom of the HTML page.'''

    print('''
    <br>
    <br>
    <br>
    <hr>
    <div class="b_footer" style="background-color:#e5e5e5;text-align:center;padding:10px;margin-top:7px;">
        <u>©humanizeus</u>
        This page was generated at %s.<br>
        Return to the <a href="/humanizeus/index.py">main page</a>.<br>
        Enter <a href="/humanizeus/admin.py">admin portal</a>.</p>
    </div>
    </body>
    </html>
    ''' % time.ctime())


 #####################################################################################


if __name__ == "__main__":

    #print_headers()
    print_top_of_page()
    print_menu()


    print_bottom_of_page()
