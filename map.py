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



def display_list_of_organizations():

    #pull all data
    all_entities = Database_requests.get_all_entities()


    #generate the table lines
    for organization in all_entities:

        print("top of tmml table")

        #filter for organization
        if organization['entity_type'] == "Organization":

            print("html goes here")


        print("html for bottom of table")


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
