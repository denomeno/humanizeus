#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe

from import_modules import *

#THE ABOVE SECTION SHOULD EXIST AT THE TOP OF EVERY PAGE

#####################################################################################
#MODEL FUNCTIONS

def generate_map():

    #pull all data
    all_entities = Database_requests.get_all_entities()
    persons_in_need = Database_requests.get_entities_need_items()

    #generate map
    #1. create map

    #create map object
    map = folium.Map(location=[42.34372, -71.074181],
                        zoom_start=13,
                        tiles="CartoDB dark_matter")

    #2. populate map

    for organization in all_entities:

        #assign variables to check if inputs exist
        latitude = organization['latitude']
        longitude = organization["longitude"]
        name = organization["name"]

        #if they dont exist, skip adding the marker
        if latitude == "" or longitude == "" or name == "":
            continue

        #filter for organization
        if organization['entity_type'] == "Organization":

            #populate organzations
            marker = folium.Marker(location=[latitude, longitude], #can also be folium.CircleMarker
                           popup ='<strong>%s</strong>' %(name),
                           tooltip = name)

            marker.add_to(map)


    for in_need in persons_in_need:

        #populate organzations

        #assign variables to check if inputs exist
        latitude = in_need['latitude']
        longitude = in_need["longitude"]
        name = in_need["entity_name"]

        #if they dont exist, skip adding the marker
        if latitude == "" or longitude == "" or name == "":
            continue

        #add to map only if they have longitude and latitude
        if in_need['latitude'] != None and in_need['longitude'] != None:

            marker = folium.CircleMarker(location=[latitude, longitude], #can also be folium.CircleMarker
                           popup ='<strong>%s</strong>' %(name), radius = 10,
                           tooltip = name)

            marker.add_to(map)

    #3. save map

    #Generate map
    map.save('map_main.html')



#####################################################################################
#VIEW FUNCTIONS

def display_map():

    print('''
    <iframe src="map_main.html" height="500" width="700">
    <p>Your browser does not support iframes.</p>
    </iframe>
''')



#####################################################################################
def get_list_of_organizations():
    """Middleware function to get all organization from the entities table.
    Returns a list of tuples of (organization_id, name, address)."""

    #pull all data
    all_entities = Database_requests.get_all_entities()
    entities_need_items = Database_requests.get_entities_need_items()
    entities_supply_items = Database_requests.get_entities_supply_items()

    ## create an HTML table for output:
    print("""
    <h2> All Organizations</h2>
    <p>

    <table border=1>
      <tr>
        <th><font size=+1"><b>Name</b></font></th>
        <th><font size=+1"><b>Address</b></font></th>
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

            supply = ""
            for item in entities_supply_items:
                if item['entity_name'] == organization['name']:
                    supply = supply + item['item_name'] + "<br>"


            #need = organization["entities_need_items"]
            need = "trial"

            display_list_of_organizations(name, address, supply, need)

    print("""
    </table>
    """)


#####################################################################################

def display_list_of_organizations(name, address, supply, need):

    # each iteration of this loop creates on record of output:
    #(name, address, supply, need) = organization

    print("""
  <tr>
    <td>%s</a></td>
    <td>%s</a></td>
    <td>%s</a></td>
    <td>%s</a></td>
  </tr>
    """ % (name, address, supply, need))






#####################################################################################
#CONTROLLER FUNCTIONS

if __name__ == "__main__":

     #print_headers()
     print_top_of_page()
     print_menu()
     #-----------
     #only for map
     generate_map()
     display_map()

     #only for organizations list/table
     display_list_of_organizations()

     #-----------
     print_bottom_of_page()
