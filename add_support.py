#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe

from import_modules import *

#THE ABOVE SECTION SHOULD EXIST AT THE TOP OF EVERY PAGE

#####################################################################################
#THIS SECTION WILL HANDLE DATA INPUT FROM THE FORMS INTO THE DATABASE

def upload_add_support_form_to_database(form):
    #this functions gets data from the form, enter into database

    #check if form exists
    if form:
        email = form['email'].value
        entity_name = form['entity_name'].value
        address = form['address'].value
        message = form['message'].value

        supply_item_names = form['supply_item_names'] #list of needed items names

        type = "Donor"

        #RETRIEVE QUANTITY OF EACH ITEM


        #1. enter entity to system

        Database_requests.insert_into_entities(email, entity_name, address, type)

        #2. get the entity_id from the email

        entity_id = Database_requests.get_entity_id_from_email(email)
        entity_id = entity_id[0]['entity_id']


        for item in supply_item_names:

            #3 match entity with item in entity_need_items
            item_name = item.value

            quantity_supplied = form['quantity_requested: %s' %(item_name)].value

            #quantity_supplied = 1 #CHANGE WHEN ENTERED FROM THE FORM

            Database_requests.insert_into_entities_supply_items(entity_id, item_name, message, quantity_supplied)

            #4-NEED TO ADD TIME AVAILABLE FOR PICKUP


#####################################################################################
def add_support():

    #pull all needed data
    items = Database_requests.get_all_items() #list of dictionaries of all item types


    #display in browser
    print('''
<h3>Support your communnity.</h3>
<p>Please fill out the form below to inform us about the resource you would like to provide, so we can match it with someone who needs exactly that. We will appreciate it if you can let us know when we can pick it up too.</p>
<form method=POST>
    Email:<br>
    <input name="email" type="email"><br>
    Name:<br>
    <input name="entity_name" type="text"><br>
    Address:<br>
    <input name="address" type="text"><br>
    Please select the item you are donating:<br>
    ''')

    for item in items: #dyamically generate options
        print('''<select name="quantity_requested: %s">
                      <option value="1">1</option>
                      <option value="2">2</option>
                      <option value="3">3</option>
                      <option value="4">4</option>
                    </select>
                <input type="checkbox" name="supply_item_names" value="%s"> %s <br>''' %(item['name'], item['name'], item['name']))

    print('''
    Please inform us about your donation(s) a little more:<br>
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
