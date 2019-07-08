#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe
# -*- coding: UTF-8 -*-


#needsmap

import MySQLdb as db
import time
import cgi
import cgitb; cgitb.enable()  # web debugging package

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
  print("Content-Type: text/html")
  print()

#####################################################################################
def print_top_of_page(title):
      '''Print the top of the HTML page.'''

      print("""
  <html>
  <head>
  <title>%s</title>
  </head>

  <body>
  """ % title)

#####################################################################################
def print_bottom_of_page():
    '''Print the bottom of the HTML page.'''

    print('''
<hr>
This page was generated at %s.<br>
Return to the <a href="./home">main page</a>.
</body>
</html>
''' % time.ctime())


#####################################################################################

if __name__ == "__main__":

  print_headers()
  print_top_of_page('MiniFacebook')

  form = cgi.FieldStorage()
  print_form_data(form)



entities_need_items = Database_requests.get_entitites_need_items()
