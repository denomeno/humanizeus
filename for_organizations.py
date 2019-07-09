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
    #2. what organizations provde

    organization_needs = Database_requests.get_organizations_need_items()
    #ie. look at `view_add_organizations()` function for a similar implementation

    organizations_supply = Database_requests.get_organizations_supply_items()





    #TODO - Boray - needs database update functions



#####################################################################################
def view_add_organizations():

    #pull all needed data
    items = Database_requests.get_all_items() #list of dictionaries of all item types


    #display in browser
    print('''
    <h3>Join the communnity.</h3>
    <h5>Please add some necessary details about your organization so we can place you on our map for members to see. </h5>
    <table>
    <form method=POST ><br>
        Email (will be used for login later, so you can update your resources):<br>
        <input name="email" type="email"><br>
        Organization Name:<br>
        <input name="suppliername" type="text"><br>
        Address:<br>
        <input name="address" type="text"><br>
        Phone:<br>
        <input name="phone" type="text"><br>
        Resources Provided at your Organization:<br>
        ''')

    for item in items: #dyamically generate options
        print('''<select name="quantity_supplied: %s">
                      <option value="1">1</option>
                      <option value="2">2</option>
                      <option value="3">3</option>
                      <option value="4">4</option>
                    </select>
                <input type="checkbox" name="supplied_item_names" value="%s"> %s <br>''' %(item['name'], item['name'], item['name']))


    print('''
        Resources your Organization Needs at the moment:<br>
        ''')

    for item in items: #dyamically generate options
        print('''<select name="quantity_requested: %s">
                      <option value="1">1</option>
                      <option value="2">2</option>
                      <option value="3">3</option>
                      <option value="4">4</option>
                    </select>
                <input type="checkbox" name="needed_item_names" value="%s"> %s <br>''' %(item['name'], item['name'], item['name']))


    print('''
            <input type='submit' value='Submit Form'>
        </form>
        <h4>Thank you for joining the community!<h/4>
        ''')

    #submit button - make post Database_requests
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
        entity_name = form['entity_name'].value
        address = form['address'].value
        #phone = form['phone'].value                #need to add to database

        needed_item_names = form['needed_item_names'] #list of needed items names
        supplied_item_names = form['supplied_item_names'] #list of supplied items names

        type = "Organization"

        #1. check if email exists in database
        entity_id = Database_requests.get_entity_id_from_email(email)
        if entity_id[0]['entity_id']: #if it exists, display need list
            view_existing_organizations_data()

            #1.a. if exists, view update option

            #1.b. insert updated item data information into database


        #---------------------------------
        #2. IF NO FORM IS SUBMITTED, DO DEFAULT VIEW

        else:
            view_join_community_form()

        #---------------------------------
        #3. enter data about supplied and needed items
        for item in needed_item_names:
            item_name = item.value
            quantity_requested = form['quantity_requested: %s' %(item_name)].value
            Database_requests.insert_into_entities_need_items(entity_id, item_name, quantity_requested)

        for item in supplied_item_names:
            item_name = item.value
            quantity_requested = form['quantity_supplied: %s' %(item_name)].value
            Database_requests.insert_into_entities_supply_items(entity_id, item_name, quantity_supplied)


    print_bottom_of_page()


#entities_need_items = Database_requests.get_entitites_need_items()
