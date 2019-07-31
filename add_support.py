#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37-32\python.exe

from import_modules import *

#THE ABOVE SECTION SHOULD EXIST AT THE TOP OF EVERY PAGE

#####################################################################################
#THIS SECTION WILL HANDLE DATA INPUT FROM THE FORMS INTO THE DATABASE

def upload_add_support_form_to_database(form):
    #this functions gets data from the form, enter into database

    #check if form exists
    if form:

        try:
            email = form['email'].value
        except KeyError:
            email = "Not entered. "

        try:
            entity_name = form['entity_name'].value
        except KeyError:
            entity_name = "Not entered."

        try:
            address = form['address'].value
        except KeyError:
            address = "Not entered."

        try:
            message = form['message'].value
        except KeyError:
            message = "Not entered."

        try:
            time_in_1 = str(form['time'].value)
        except KeyError:
            time_in_1 = "Not entered."


        type = "Donor"


        #get list of available item options
        needed_items = Database_requests.get_only_needed_items()


        #RETRIEVE QUANTITY OF EACH ITEM

        #1. enter entity to system

        Database_requests.insert_into_entities(email, entity_name, address, type)

        #2. get the entity_id from the email

        entity_id = Database_requests.get_entity_id_from_email(email)
        entity_id = entity_id[0]['entity_id']


        for item in needed_items:

            #3 match entity with item in entity_need_items
            item_name = item['name']

            quantity_supplied = form['quantity_requested: %s' %(item_name)].value

            #quantity_supplied = 1 #CHANGE WHEN ENTERED FROM THE FORM

            if quantity_supplied != '0':

                Database_requests.insert_into_entities_supply_items(entity_id, item_name, message, quantity_supplied, time_in_1)

            #4-NEED TO ADD TIME AVAILABLE FOR PICKUP


#####################################################################################
def add_support():

    #pull all needed data
    needed_items = Database_requests.get_only_needed_items()#list of dictionaries of item types that are needed by others

    #display in browser
    print('''
<h3>Support your communnity.</h3>
<p>Please fill out the form below to inform us about the resource you would like to provide, so we can match it with someone who needs exactly that. We will appreciate it if you can let us know when we can pick it up too.</p>
<form method=POST>
    Email:<br>
    <input name="email" type="email" required><br>
    Name:<br>
    <input name="entity_name" type="text" required><br>
    Address:<br>
    <input name="address" type="text" required><br>
    <br>Please select the item you are donating. <br>
    ''')

    for item in needed_items: #dyamically generate options
        print('''<select name="quantity_requested: %s">
                      <option value="0">0</option>
                      <option value="1">1</option>
                      <option value="2">2</option>
                      <option value="3">3</option>
                      <option value="4">4</option>
                    </select> %s <br>''' %(item['name'], item['name']))

    print('''
    <br>Please inform us about your donation(s) a little more:<br>
    <textarea name="message" rows="10" cols="30">
    </textarea><br>
    Let us know when we can pick it up.<br>
    <input name="time" type="text"><br>
    <input type='submit' value='Submit Form'>
    </form>
    <h4>Thank you for supporting your community. We will contact you when we find a match.<h/4>

    ''')

    #submit button - make post Database_requests
    #at top of page - if post request, enter to database

#####################################################################################

if __name__ == "__main__":

    print_headers()
    print_top_of_page()
    print_menu()
    #----------------
    form = cgi.FieldStorage()
    print_form_data(form)

    #--------------------------------
    #run controller functions
    upload_add_support_form_to_database(form)

     #------------------
    add_support()
    print_bottom_of_page()
