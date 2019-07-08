#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe

from import_modules import *

#THE ABOVE SECTION SHOULD EXIST AT THE TOP OF EVERY PAGE

#####################################################################################
def view_existing_organizations_login():

    #display in browser
    print('''
    Existing member?<br>
    <form method=POST >
        <input name="email" type="email">
        <input type='submit' value='Submit'>
    </form>
    ''')


#####################################################################################

def view_existing_organizations_data():
    #THIS FUNCTION SHOULD:
    #1. PULL THE NEEDED DATA FROM DATABASE
    #2. DISPLAY: A. ORGANIZATIONS NEEDS, B. ORGANIZATIONS SUPPLY

    #get the following data:
    #1. what organization need
    #2. what organizations donate

    organization_needs = Database_requests.get_organizations_need_items()





#####################################################################################
def view_add_organizations():

    #pull all needed data
    items = Database_requests.get_all_items() #list of dictionaries of all item types


    #display in browser
    print('''
<h3>Support a neighbor.</h3>
<p>Please fill out the form below to inform us about the resource you would like to provide, so we can match it with someone who needs exactly that. We’d appreciate it if you can let us know when we can pick it up too.</p>
<table>
<form method=POST >
    <input name="email" type="email" label="Name">
    <input name="suppliername" type="text">
    <input name="address" type="text">
    <select name="resourcelist">''')

    for item in items: #dyamically generate options
        print('''<option value="%s">%s</option>''' %(item['name'], item['name']))

    print('''
    </select>
    <textarea name="message" rows="10" cols="30">
    Describe the item a little more.
    </textarea>
    <input name="time" type="text">
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

    form = cgi.FieldStorage()
    print_form_data(form)

    #--------------------------------
    #INSERT GENERAL VIEW ITEMS, THAT APPEAR REGARDLESS IF THE
    #FORM IS SUBMITTED OR NOT

    view_existing_organizations_login()
    view_add_organizations()

    #--------------------------------
    #IF A FORM IS FILLED AND SUBMITTED, DO THE ACTIONS FOR THE FORM

    #run controller functions
    if form:
        email = form['email'].value
        type = "Organization"

        #1. check if email exists in database
        entity_id = Database_requests.get_entity_id_from_email(email)
        if entity_id[0]['entity_id']: #if it exists, display need list
            view_existing_organizations_data()

        #else:
            #view_join_community_form()

    #---------------------------------
    #IF NO FORM IS SUBMITTED, DO DEFAULT VIEW


    print_bottom_of_page()

#print_top_of_page('MiniFacebook')

#entities_need_items = Database_requests.get_entitites_need_items()
