#!C:\Users\Boray Toktay\AppData\Local\Programs\Python\Python37-32\python.exe

from import_modules import *

#THE ABOVE SECTION SHOULD EXIST AT THE TOP OF EVERY PAGE

#####################################################################################
#THIS SECTION WILL HANDLE DATA INPUT FROM THE FORMS INTO THE DATABASE

#####################################################################################
def add_support():

    #pull all needed data
    items = Database_requests.get_all_items() #list of dictionaries of all item types


    #display in browser
    print('''
<h3>Support a neighbor.</h3>
<p>Please fill out the form below to inform us about the resource you would like to provide, so we can match it with someone who needs exactly that. We’d appreciate it if you can let us know when we can pick it up too.</p>
<table>
<form method=POST >
    Email:<br>
    <input name="email" type="email" label="Name"><br>
    Name:<br>
    <input name="suppliername" type="text"><br>
    Address:<br>
    <input name="address" type="text"><br>
    Please select the item you are donating:<br>
    ''')

    for item in items: #dyamically generate options
        print('''<option value="%s">%s</option>''' %(item['name'], item['name']))

    print('''
    Please inform us about your donation(s) a little more:<br>
    <textarea name="message" rows="10" cols="30">
    </textarea><br>
    Let us know when we can pick it up.<br>
    <input name="time" type="text"><br>
    <input type='submit' value='Submit Form'>
</form>
</table>
<h4>Thank you for believing in your community<h/4>

''')

    #submit buttin - make post Database_requests
    #at top of page - if post request, enter to database

#####################################################################################

if __name__ == "__main__":



     #print_headers()
     print_top_of_page()
     print_menu()

     #----------------
     form = cgi.FieldStorage()
     print_form_data(form)


     #------------------
     add_support()
     print_bottom_of_page()
