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
def home_page_display():

    print('''
    <h2>Building a community starts here!</h2>
    <button type="button">Click Me!</button>
    <button type="button">Click Me!</button>

    ''')

 #####################################################################################

if __name__ == "__main__":

    #print_headers()
    print_top_of_page()
    print_menu()
    #-----------
    home_page_display()


    #-----------
    print_bottom_of_page()
