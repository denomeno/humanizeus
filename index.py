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


def print_top_of_page():
      '''Print the top of the HTML page.'''

      print("""
  <html>
  <head>
  <title>HumanizeUs</title>
  </head>

  <body>
  """ )
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
<body>

<div id='cssmenu'>
<ul>
   <li class='active'><a href='/humanizeus/index.py'><span>Home</span></a></li>
   <li><a href='/humanizeus/add_need.py'><span>Add Need</span></a></li>
   <li><a href='/humanizeus/add_support.py'><span>Add Support</span></a></li>
   <li><a href='/humanizeus/for_organizations.py'><span>For Organizations</span></a></li>
   <li class='last'><a href='/humanizeus/map.py'><span>Map</span></a></li>
   <li><a href='/humanizeus/contact.py'><span>Contact Us</span></a></li>
</ul>
</div>

''')


def print_bottom_of_page():
     '''Print the bottom of the HTML page.'''

     print('''
 <hr>
 This page was generated at %s.<br>
 Return to the <a href="/humanizeus/humanizeus/index.py">main page</a>.
 </body>
 </html>
 ''' % time.ctime())


 #####################################################################################


if __name__ == "__main__":

     #print_headers()
     print_top_of_page()
     print_menu()
     print_bottom_of_page()

     hello
