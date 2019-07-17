#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe

from import_modules import *

#THE ABOVE SECTION SHOULD EXIST AT THE TOP OF EVERY PAGE

#####################################################################################
#THIS SECTION WILL HANDLE DATA INPUT FROM THE FORMS INTO THE DATABASE

def upload_add_need_form_to_database(form):
    #this functions gets data from the form, enter into database
    if form:
        email = form['email'].value
        entity_name = form['entity_name'].value
        address = form['address'].value
        message = form['message'].value

        needed_item_names = form['needed_item_names'] #list of needed items names

        type = "In Need"

        #RETRIEVE QUANTITY OF EACH ITEM


        #1. enter entity to system

        Database_requests.insert_into_entities(email, entity_name, address, type)

        #2. get the entity_id from the email

        entity_id = Database_requests.get_entity_id_from_email(email)
        entity_id = entity_id[0]['entity_id']


        for item in needed_item_names:

            #3 match entity with item in entite_need_items
            item_name = item.value

            quantity_requested = form['quantity_requested: %s' %(item_name)].value

            #quantity_requested = 1 #CHANGE WHEN ENTERED FROM THE FORM

            Database_requests.insert_into_entities_need_items(entity_id, item_name, message, quantity_requested)



#####################################################################################
def add_need():

    #pull all needed data
    items = Database_requests.get_all_items() #list of dictionaries of all item types

    #display in browser
    print('''
<h3>We are here to support you.</h3>
<p>Tell us your needs, and we will match you with a neighbor who might have exactly what you need right now.</p>
<form method = "POST">
    Email:<br>
    <input name="email" type="email" required><br>
    Name:<br>
    <input name="entity_name" type="text" required><br>
    Address:<br>
    <input name="address" type="text" required><br>
    <br>Please select need. If what you need is not on the list, let us know in the box below:<br>
    ''')

    for item in items: #dyamically generate options
        print('''<select name="quantity_requested: %s">
                      <option value="0">0</option>
                      <option value="1">1</option>
                      <option value="2">2</option>
                      <option value="3">3</option>
                      <option value="4">4</option>
                    </select> %s <br>''' %(item['name'], item['name']))

    print('''
    <br>Please inform us about your need(s) a little more:<br>
    <textarea name="message" rows="10" cols="30">
    </textarea><br>
    <input type='submit' value='Submit Form'>
</form>
<h4>Thank you for believing in your community. We will contact you when we find a match.<h/4><br>

''')


#####################################################################################



if __name__ == "__main__":

    print_headers()
    print_top_of_page()
    print_menu()

    form = cgi.FieldStorage()
    print_form_data(form)

    #--------------------------------
    #run controller functions
    upload_add_need_form_to_database(form)

    #---------------------------------

    add_need()
    print_bottom_of_page()


#entities_need_items = Database_requests.get_entitites_need_items()
