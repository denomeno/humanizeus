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
                        tiles='openstreetmap')

    #2. populate map

    for organization in all_entities:

        #assign variables to check if inputs exist
        latitude = organization['latitude']
        longitude = organization["longitude"]
        name = organization["name"]
        address = organization["address"]
        phone = organization["phone"]

        #if they dont exist, skip adding the marker
        if latitude == "" or longitude == "" or name == "":
            continue

        #filter for organization
        if organization['entity_type'] == "Organization":

            popup ='''<b>Name:</b> %s<br>
                    <b>Address:</b> %s<br>
                    <b>Phone:</b> %s<br>
                    ''' %(name, address, phone)

            #populate organzations
            marker = folium.Marker(location=[latitude, longitude], #can also be folium.CircleMarker
                           popup = folium.Popup(popup, max_width=450),
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

        #exclude organizations from map
        if in_need['type_description'] == "Organization":
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
    <div id="main_block">
        <iframe id="left_frame" src="map_main.html" height="600" width="730">
        </iframe>
    ''')



#####################################################################################
def display_list_of_organizations():

    print('''
        <iframe id="right_frame" src="organization_list_frame.py" style = "width: 730px; height: 600px;" scrolling="yes"></iframe>
    </div>
    ''')


#####################################################################################
#CONTROLLER FUNCTIONS

if __name__ == "__main__":

     print_headers()
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
