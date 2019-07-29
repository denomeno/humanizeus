#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe

from import_modules import *

#THE ABOVE SECTION SHOULD EXIST AT THE TOP OF EVERY PAGE

#####################################################################################

def view_admin_login():
    #display in browser
    print('''
    HumanizeUs admin?<br>
    <form method=POST >
      <div class="form-group">
        <label for="exampleInputEmail1">Email address</label>
        <input type="hidden" name="form_name" value="adminLogin"/>
        <input name="admin_email" type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
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
def view_list_of_all_matches():
    #THIS FUNCTION SHOULD:
    #1. PULL THE NEEDED DATA FROM DATABASE
    #2. DISPLAY LIST OF ALL: A. MATCHES B. NEEDS C. SUPPLIES

    matches = Database_requests.get_all_matches()

    print("""
    <h3> All Matches</h3>
    <p>

    <table border=1>
      <tr>
        <th><font size=+1"><b>Match Id</b></font></th>
        <th><font size=+1"><b>Item Name</b></font></th>
        <th><font size=+1"><b>In Need Name</b></font></th>
        <th><font size=+1"><b>Supplier Name</b></font></th>
        <th><font size=+1"><b>Time</b></font></th>
        <th><font size=+1"><b>Status</b></font></th>
        <th><font size=+1"><b>Approve</b></font></th>
        <th><font size=+1"><b>Deny</b></font></th>
      </tr>
    """)

    for match in matches:

        match_id = match['match_id']
        item_name = match['item_name']
        in_need_name = match['in_need_name']
        supply_name = match['supply_name']
        fulfillment_status = match['fulfillment_status']

        #print each line for table
        print("""
      <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>#add time#</td>
        <td>%s</td>
        <td><input type="checkbox" name="approve"></td>
        <td><input type="checkbox" name="deny"></td>
      </tr>
        """ % (match_id,item_name, in_need_name, supply_name, fulfillment_status))

    #print('''''') end of table
    print("""
    </table>
    <input type='submit' name="admin_portal" value='Update'>
    """)

#####################################################################################
def view_list_of_all_needs():
    #THIS FUNCTION SHOULD:
    #1. PULL THE NEEDED DATA FROM DATABASE
    #2. NEEDS

    needs = Database_requests.get_entities_need_items()

    print("""
    <h3> All Needs</h3>
    <table border=1>
      <tr>
        <th><font size=+1"><b>Entity Id</b></font></th>
        <th><font size=+1"><b>In Need Name</b></font></th>
        <th><font size=+1"><b>Item Name</b></font></th>

      </tr>
    """)

    for need in needs:

        entity_id = need['entity_id']
        entity_name = need['entity_name']
        item_name = need['item_name']

        #print each line for table
        print("""
      <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
      </tr>
        """ % (entity_id, entity_name, item_name))

    #print('''''') end of table
    print("""
    </table>
    """)

#####################################################################################
def view_list_of_all_supplies():
    #THIS FUNCTION SHOULD:
    #1. PULL THE NEEDED DATA FROM DATABASE
    #2. SUPPLIES

    supplies = Database_requests.get_entities_supply_items()

    print("""
    <h3> All Supplies</h3>
    <table border=1>
      <tr>
        <th><font size=+1"><b>Entity Id</b></font></th>
        <th><font size=+1"><b>Supplier Name</b></font></th>
        <th><font size=+1"><b>Item Name</b></font></th>

      </tr>
    """)

    for supply in supplies:

        entity_id = supply['entity_id']
        entity_name = supply['entity_name']
        item_name = supply['item_name']

        #print each line for table
        print("""
      <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
      </tr>
        """ % (entity_id, entity_name, item_name))

    #print('''''') end of table
    print("""
    </table>
    """)



 #####################################################################################


if __name__ == "__main__":

    print_headers()
    print_top_of_page()
    print_menu()
    #-----------

    form = cgi.FieldStorage()
    print_form_data(form)

    #-----------
    view_admin_login()

    #decide which form to run
    if form:
        if form['form_name'].value == 'adminLogin': #IF LOGIN TO EXISTING ORGANIZATION FORM FILLE

            #run function for existing organizations
            email = form['admin_email'].value

            admin_exists = Database_requests.get_admin_from_email(email)#list of matching admins

            if len(admin_exists) > 0:

                view_list_of_all_matches()
                view_list_of_all_needs()
                view_list_of_all_supplies()


    #-----------

    print_bottom_of_page()
