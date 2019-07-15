#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe

from import_modules import *

#THE ABOVE SECTION SHOULD EXIST AT THE TOP OF EVERY PAGE


#####################################################################################

def display_list_row(name, address, phone, supply, need):

    # each iteration of this loop creates on record of output:
    #(name, address, supply, need) = organization

    print("""
  <tr>
    <td>%s</a></td>
    <td>%s</a></td>
    <td>%s</a></td>
    <td>%s</a></td>
    <td>%s</a></td>
  </tr>
    """ % (name, address, phone, supply, need))


#####################################################################################


def generate_organization_list_table():

    #pull all data
    all_entities = Database_requests.get_all_entities()
    entities_need_items = Database_requests.get_entities_need_items()
    entities_supply_items = Database_requests.get_entities_supply_items()

    ## create an HTML table for output:
    print("""
    print("Content-type:text/html\r\n\r\n")
    <h2><center>List of All Organizations</center></h2>
    <p>

      <table border=1 align="center">
          <tr>
              <th><font size=+1"><b>Name</b></font></th>
              <th><font size=+1"><b>Address</b></font></th>
              <th><font size=+1"><b>Phone</b></font></th>
              <th><font size=+1"><b>Provides</b></font></th>
              <th><font size=+1"><b>Needs</b></font></th>
          </tr>
    """)

    #generate the table lines
    #for organization in all_entities:

    for organization in all_entities:

      #filter for organization
      if organization['entity_type'] == "Organization":

          #get variables needed for table
          if organization['name']:
              name = organization['name']
          elif not organization['name']:
              name = "N/A"

          if organization["address"]:
              address = organization["address"]
          elif not organization["address"]:
              address = "N/A"

          if organization["phone"]:
              phone = organization["phone"]
          elif not organization["phone"]:
              phone = "N/A"

          supply = ""
          for item in entities_supply_items: #iterate supplied items list,
              if item['entity_name'] == organization['name']: #for matching organization names, add the supplied item name
                  supply = supply + item['item_name'] + "<br>"

          need = ""
          for item in entities_need_items:
              if item['entity_name'] == organization['name']:
                  quantity_requested = item['quantity_requested']
                  quantity_fulfilled = item['quantity_fulfilled']
                  quantity = int(quantity_requested - quantity_fulfilled)
                  need = need + str(quantity) + " - " + item['item_name'] + "<br>"

          display_list_row(name, address, phone, supply, need)

    print("""
      </table>
    <br>
    """)

if __name__ == "__main__":
    generate_organization_list_table()
