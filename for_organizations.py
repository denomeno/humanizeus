#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe

from import_modules import *

#THE ABOVE SECTION SHOULD EXIST AT THE TOP OF EVERY PAGE

#####################################################################################
def view_existing_organizations_login():

    #display in browser
    print('''
    Existing member?<br>
    <form method=POST >
        <input type="hidden" name="form_name" value="existingMemberLogin"/>
        <input name="login_email" type="email">
        <input type='submit' value='Login'>
    </form>
    ''')


#####################################################################################
def view_existing_organizations_data(email):
    #THIS FUNCTION SHOULD:
    #1. PULL THE NEEDED DATA FROM DATABASE
    #2. DISPLAY: A. ORGANIZATIONS NEEDS, B. ORGANIZATIONS SUPPLY

    entity_id = Database_requests.get_entity_id_from_email(email)
    entity_id = entity_id[0]['entity_id']

    organizations_supply = Database_requests.get_organizations_supply_items(email)
    organizations_need = Database_requests.get_organizations_need_items(email)
    items = Database_requests.get_all_items()


    #A. ORGANIZATIONS NEED
    print('''
    <b>Resources Needed at your Organization:</b><br>
    ''')

    #1.show filled in form of items needed selected before
    print('''<form method=POST >
                <input type="hidden" name="form_name" value="updateNeeds"/>
                <input type="hidden" name="entity_id" value=%s>''' %(entity_id))

    for item in items:

        quantity = 0 #variable to store how many of each item an organization supplies

        #form displays all items that can be chosen
        for need_item in organizations_need: #dyamically generate options

            entities_need_items_id = need_item['entities_need_items_id'] #unique if of organization_supply_items match


            if item['name'] == need_item['item_name']:

                quantity_requested = need_item['quantity_requested']
                quantity_fulfilled = need_item['quantity_fulfilled']
                quantity = int(quantity_requested-quantity_fulfilled)

                print('''
                    <input type="hidden" name="entities_need_items_id: %s" value=%s>
                    ''' %(need_item['item_name'], entities_need_items_id)) #make hidden fields to identify the unique organization_need_items_id


        print('''<select name="quantity: %s">
                 ''' %(item['name']))

        for i in range(0,5): #display the selection boxes
            if quantity == i: #display the selected box if box number matches with requested quantity
                print('''<option value="%s" selected>%s</option>
                        ''' %(i, i))
            else:
                print('''<option value="%s">%s</option>
                        ''' %(i, i))

        print('''</select>
                <output type="checkbox" name="organizations_supply_item_names" value="%s"> %s <br>
                ''' %(item['name'],item['name']))#add organization need item id



    print('''<input type='submit' value='Update Needs'>
             </form>''')


    #B. ORGANIZATIONS SUPPLY
    print('''
    <br>
    <br>
    <br>
    ''')

    print('''
    <b>Resources Provided at your Organization:</b><br>
    <p>

    ''')

    print('''<form method=POST >
                <input type="hidden" name="form_name" value="updateSupply"/>''')

    for item in items:
        #use boolean to store if matched
        item_supplied = False #set initially as not needed

        for supply_item in organizations_supply: #find if item amongst organizations's supply

            entities_supply_items_id = supply_item['entities_supply_items_id'] #unique if of organization_supply_items match

            if item['name'] == supply_item['item_name']:

                item_supplied = True

        if item_supplied is True:

            print('''
                <input type="checkbox" value=%s checked >%s<br>
            '''%(item['name'],item['name']))

        elif item_supplied is False:
            print('''
                <input type="checkbox" value=%s>%s<br>
                '''%(item['name'],item['name']))

    print('''<input type='submit' value='Update Provided Item List'>
             </form>''')


#####################################################################################
def view_add_organizations():

    #pull all needed data
    items = Database_requests.get_all_items() #list of dictionaries of all item types


    #display in browser
    print('''
    <h3>Join the communnity.</h3>
    <h4>Please add some necessary details about your organization so we can place you on our map for members to see. </h4>
    <form method=POST ><br>
        <input type="hidden" name="form_name" value="newOrganization"/>
        <u>Email (will be used for login later, so you can update your resources):<br>
        <input name="new_organization_email" type="email"><br>
        Organization Name:<br>
        <input name="suppliername" type="text"><br>
        Address:<br>
        <input name="address" type="text"><br>
        Phone:<br>
        <input name="phone" type="text"><br>
        <hr>
        Resources Provided at your Organization:<br>
        ''')

    #list of items provided
    for item in items: #dyamically generate options
        print('''<input type="checkbox" name="supplied_item_names" value="%s"> %s <br>''' %(item['name'], item['name']))


    print('''
        Resources your Organization Needs at the moment:<br>
        ''')

    #list of items needed
    for item in items: #dyamically generate options
        print('''<select name="quantity_requested: %s">
                      <option value="0">0</option>
                      <option value="1">1</option>
                      <option value="2">2</option>
                      <option value="3">3</option>
                      <option value="4">4</option>
                    </select>
                 %s <br>''' %(item['name'], item['name']))


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

    if not form: #view only if no form is submitted - at the very beginning
        view_add_organizations()

    #--------------------------------
    #IF A FORM IS FILLED AND SUBMITTED, DO THE ACTIONS FOR THE FORM

    #decide which form to run
    if form:
        if form['form_name'].value == 'existingMemberLogin': #IF LOGIN TO EXISTING ORGANIZATION FORM FILLE

            #run function for existing organizations
            email = form['login_email'].value

            #1. check if email exists in database
            entity_id = Database_requests.get_entity_id_from_email(email)
            if entity_id[0]['entity_id']: #if it exists, display need list
                view_existing_organizations_data(email)


        elif form['form_name'].value == "newOrganization": #IF NEW ORGZANITION FORM IS FILLED

            #get fields from the submitted form
            email = form['email'].value
            entity_name = form['entity_name'].value
            address = form['address'].value
            phone = form['phone'].value

            needed_item_names = form['needed_item_names'] #list of needed items names
            supplied_item_names = form['supplied_item_names'] #list of supplied items names

            #assign organization type - because this form is only for organizations
            type = "Organization"

            #insert the organization into entities table
            Database_requests.insert_into_entities(email, entity_name, address, type)


            for item in needed_item_names:
                item_name = item.value
                quantity_requested = form['quantity_requested: %s' %(item_name)].value
                Database_requests.insert_into_entities_need_items(entity_id, item_name, quantity_requested)

            for item in supplied_item_names:
                item_name = item.value
                quantity_requested = form['quantity_requested: %s' %(item_name)].value
                Database_requests.insert_into_entities_supply_items(entity_id, item_name, quantity_requested)



        elif form['form_name'].value == "updateNeeds":

            all_items = Database_requests.get_all_items()

            for item in all_items:

                #get the fiels with the item name
                try:
                    #get entities_need_items_id
                    entities_need_items_id = form['entities_need_items_id: %s' %(item['name'])].value

                    #get quantity
                    quantity_requested = form['quantity: %s' %(item['name'])].value

                    #update database
                    Database_requests.update_quantity_requested_of_entities_need_items(entities_need_items_id, quantity_requested)

                except ValueError:
                    #if value error is present: this means there is no existing entry in entities_need_items for that organization and that item pair
                    #thus: insert new entry

                    entity_id = form['entity_id'].value

                     #get quantity
                    quantity_requested = form['quantity: %s' %(item['name'])].value

                    Database_requests.insert_into_entities_need_items()




                #get entities_need_items_id
                #get quantity

                #if number is not zero, create a new entry

                #if number is zero, delete the previous entry - accorind to id s


        elif form['form_name'].value == "updateSupply":

            all_items = Database_requests.get_all_items()


    print_bottom_of_page()


#entities_need_items = Database_requests.get_entitites_need_items()
