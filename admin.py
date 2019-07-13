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
 print()

#####################################################################################
def print_top_of_page():
      '''Print the top of the HTML page.'''

      print("""
      <html>
      <head>
      <title>HumanizeUs</title>
      <h1>HumanizeUs</h1>
      <h3>A Neighborly Exchange</h3>
      <style>

      h1 {
      color: red
      font-family: "Garamound";
      }

      body {
      background-color: white;
      }

      </style>
      </head>
      <body>
      """)

      #text-align: center;

#####################################################################################
def print_menu():

    print('''
<head>
   <meta charset='utf-8'>
   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   <meta name="viewport" content="width=device-width, initial-scale=1">
   <link rel="stylesheet" href="styles.css">
   <script src="http://code.jquery.com/jquery-latest.min.js" type="text/javascript"></script>
   <script src="script.js"></script>
   <title>CSS MenuMaker</title>
</head>

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
</head>

<body>
<div id='cssmenu'>
<ul>
   <li class='active'><a href='/humanizeus/index.py'><span>Home</span></a></li>
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

def view_admin_login():
    #display in browser
    print('''
    HumanizeUs member?<br>
    <form method=POST >
        <input type="hidden" name="form_name" value="adminLogin">
        <input name="admin_email" type="email">
        <input type='submit' value='Login'>
    </form>
    ''')

#####################################################################################
def view_list_of_all_matches():
    #THIS FUNCTION SHOULD:
    #1. PULL THE NEEDED DATA FROM DATABASE
    #2. DISPLAY LIST OF ALL: A. MATCHES B. NEEDS C. SUPPLIES

    matches = Database_requests.get_all_matches()

    print("""
    <h3> All Matches</h3>
    <p>

    <table border=1>
      <tr>
        <th><font size=+1"><b>Match Id</b></font></th>
        <th><font size=+1"><b>Item Name</b></font></th>
        <th><font size=+1"><b>In Need Name</b></font></th>
        <th><font size=+1"><b>Supplier Name</b></font></th>
        <th><font size=+1"><b>Status</b></font></th>
      </tr>
    """)

    for match in matches:

        match_id = match['match_id']
        item_name = match['item_name']
        in_need_name = match['in_need_name']
        supply_name = match['supply_name']
        fulfillment_status = match['fulfillment_status']

        #print each line for table
        print("""
      <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
      </tr>
        """ % (match_id,item_name, in_need_name, supply_name, fulfillment_status))

    #print('''''') end of table
    print("""
    </table>
    """)



#####################################################################################

def print_bottom_of_page():
     '''Print the bottom of the HTML page.'''

     print('''
 <hr>
 This page was generated at %s.<br>
 Return to the <a href="/humanizeus/index.py">main page</a>.
 Enter <a href="/humanizeus/admin.py">admin portal</a>.
 </body>
 </html>
 ''' % time.ctime())


 #####################################################################################


if __name__ == "__main__":

    #print_headers()
    print_top_of_page()
    print_menu()
    #-----------

    #-----------
    view_admin_login()

    #decide which form to run
    if form:
        if form['form_name'].value == 'adminLogin': #IF LOGIN TO EXISTING ORGANIZATION FORM FILLE

            #run function for existing organizations
            email = form['admin_email'].value
            view_list_of_all_matches()
    #-----------

    print_bottom_of_page()
