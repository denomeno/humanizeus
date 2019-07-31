#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37-32\python.exe

from import_modules import *

#THE ABOVE SECTION SHOULD EXIST AT THE TOP OF EVERY PAGE

#####################################################################################
def view_existing_organizations_login():

    #display in browser
    print('''
    <h3>Existing member?</h3><br>
    <form method=POST >
      <div class="form-group">
        <label for="exampleInputEmail1">Email address</label>
        <input type="hidden" name="form_name" value="existingMemberLogin"/>
        <input name="login_email" type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
        <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
      </div>
      <div class="form-group">
        <label for="exampleInputPassword1">Password</label>
        <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
      </div>
      <div class="form-group form-check">
        <input type="checkbox" class="form-check-input" id="exampleCheck1">
        <label class="form-check-label" for="exampleCheck1">Check me out</label>
      </div>
      <button type="submit" class="btn btn-primary">Login</button>
    </form>
    ''')

#####################################################################################
def view_existing_organization_profile(email):

    #get profile data of organization
    org_profile = Database_requests.get_entity_from_email(email)

    #assign variables
    name = org_profile[0]['name']
    address = org_profile[0]['address']
    phone = org_profile[0]['phone']
    website = org_profile[0]['website']

    #display on page - preinserted into html form text inpput fields


    #1.show filled in form of information entered before
    print('''<form method=POST >
                <input type="hidden" name="form_name" value="updateProfile"/>
                <input type="hidden" name="org_email" value=%s>
                <input type="hidden" name="org_profile" value=%s>''' %(email, org_profile))

    #2. Organization name
    print('''
    <h3><b>Welcome Back %s!</b><br></h3>
    ''' % name)

    for org_profile in entity_id:

        print('''
            <table>
                <tr>
                    <td><label><b>Name:</b></label></td>
                    <td><center><input type="text" name="name" value='%s'></center></td>

                </tr>
                <tr>
                    <td><label><b>Address:</b></label></td>
                    <td><center><input type="text" name="address" value='%s'></center></td>
                </tr>
                <tr>
                    <td><label><b>Phone:</b></label></td>
                    <td><center><input type="text" name="phone" value='%s'></center></td>
                </tr>
                <tr>
                    <td><label>Website:</label></td>
                    <td><center><input type="text" name="website" value='%s'></center></td>
                </tr>
            </table>
        '''% (name, address, phone, website))

        print('''<input type='submit' name="profile_form" value='Update Profile'>
                 </form>''')



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

        #check if item should be shown
        if item['show_in_need_options_of_organization'] == "No":
            continue

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

        #check if item should be shown
        if item['show_in_supply_options_of_organization'] == "No":
            continue

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
             </form>''') #ADD REGISTERED NOTIFICATION


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
        <u>Email (will be used for login later, so you can update your resources):</u><br>
        <input name="new_organization_email" type="email" required><br>
        Organization Name:<br>
        <input name="entity_name" type="text" required><br>
        Address:<br>
        <div class="form-group">
            <input type="street" name="street" placeholder="Street" required>
            <input type="city" name="city" placeholder="City" required>
            <br>
            <input type="state" name="state" placeholder="State" required>
            <input type="zip" name="zip" placeholder="Zip" required>
        </div>
        <br>
        Phone:<br>
        <input name="phone" type="text"><br>
        <hr>
        Resources Provided at your Organization:<br>
        ''')

    #list of items provided
    for item in items: #dyamically generate options

        #check if item should be shown
        if item['show_in_supply_options_of_organization'] == "No":
            continue
        print('''<input type="checkbox" name="supplied_item_names" value="%s"> %s <br>''' %(item['name'], item['name']))


    print('''
        Resources your Organization Needs at the moment:<br>
        ''')

    #list of items needed
    for item in items: #dyamically generate options

        #check if item should be shown
        if item['show_in_need_options_of_organization'] == "No":
            continue
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

    print_headers()
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
                view_existing_organization_profile(email)
                view_existing_organizations_data(email)


        elif form['form_name'].value == "newOrganization": #IF NEW ORGZANITION FORM IS FILLED

            #get fields from the submitted form
            email = form['new_organization_email'].value
            entity_name = form['entity_name'].value
            address_street = form['street'].value
            address_city = form['city'].value
            address_state = form['state'].value
            address_zip = form['zip'].value
            phone = form['phone'].value
            time_in_1 = "0000"

            #assign organization type - because this form is only for organizations
            address = address_street + address_city + address_state + address_zip
            type = "Organization"
            description = "--no description for organizations--"

            try:#attempt to retrieve supplied item, if not retrieved, move on
                supplied_item_names = form['supplied_item_names'] #list of supplied items names
                are_there_supplied_items = True
                if isinstance(supplied_item_names, list) is True: #check if there are muclitple added items
                    multiple_supplied_items = True
                else:
                    multiple_supplied_items = False

            except KeyError:
                are_there_supplied_items = False

            #use this to check for item
            all_items = Database_requests.get_all_items()

            #get gocodeing of address
            geocode = Google_requests.get_geocode(address)

            #insert the organization into entities table
            database_entity_id = Database_requests.insert_into_entities(email, entity_name, address, type)#new entry is made, and entity id is returned

            #update address information of the entity
            Database_requests.update_geocode_of_entity(database_entity_id, geocode['formatted_address'], geocode['latitude'], geocode['longitude'])


            for item in all_items: #iterate all availeble items, and match from the form accorgin to their names
                quantity_requested = form['quantity_requested: %s' %(item['name'])].value
                if quantity_requested != "0": #if quantity_requested is 0, skip the item
                    Database_requests.insert_into_entities_need_items(database_entity_id, item['name'], description, quantity_requested)


            if are_there_supplied_items is True: #only if there are supplied items, attempt to put them in the database

                if multiple_supplied_items is True:#if there are mutliple number, iterate through list
                    for item in supplied_item_names:
                        item_name = item.value
                        quantity_requested = "0"
                        Database_requests.insert_into_entities_supply_items(database_entity_id, item_name, description, quantity_requested, time_in_1)
                elif multiple_supplied_items is False:#if not, use single element
                    item_name = supplied_item_names.value
                    quantity_requested = "0"
                    Database_requests.insert_into_entities_supply_items(database_entity_id, item_name, description, quantity_requested, time_in_1)



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

                except KeyError:
                    #if value error is present: this means there is no existing entry in entities_need_items for that organization and that item pair
                    #thus: insert new entry

                    entity_id = form['entity_id'].value

                     #get quantity
                    quantity_requested = form['quantity: %s' %(item['name'])].value

                    description = "Updated"

                    if int(quantity_requested) == 0:
                        continue

                    #insert into database
                    Database_requests.insert_into_entities_need_items(entity_id, item['name'], description,  quantity_requested)



                #get entities_need_items_id
                #get quantity

                #if number is not zero, create a new entry

                #if number is zero, delete the previous entry - accorind to id s


        elif form['form_name'].value == "updateSupply":

            all_items = Database_requests.get_all_items()

        elif form['form_name'].value == "updateProfile":

            email = form['org_email'].value

            #get profile data of organization
            org_profile = Database_requests.get_entity_from_email(email)

            #assign variables
            entity_id = org_profile[0]['entity_id']
            name = org_profile[0]['name']
            address = org_profile[0]['address']
            phone = org_profile[0]['phone']
            website = org_profile[0]['website']

            #get values from the form
            try:
                name = form['name'].value
            except KeyError:
                name = name

            try:
                address = form['address'].value

                #get gocodeing of address - for proper address
                geocode = Google_requests.get_geocode(address)
            except KeyError:
                address = address

            try:
                phone = form['phone'].value
            except KeyError:
                phone = phone

            try:
                website = form['website'].value
            except KeyError:
                website = website


            #update database
            Database_requests.update_entity_profile(entity_id, name, phone, website)

            #update address information of the entity
            Database_requests.update_geocode_of_entity(entity_id, geocode['formatted_address'], geocode['latitude'], geocode['longitude'])


    print_bottom_of_page()


#entities_need_items = Database_requests.get_entitites_need_items()
