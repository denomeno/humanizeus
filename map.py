#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe

from import_modules import *

#THE ABOVE SECTION SHOULD EXIST AT THE TOP OF EVERY PAGE

#####################################################################################
#MODEL FUNCTIONS

def generate_map():

    #pull all data
    all_entities = Database_requests.get_all_entities()
    persons_in_need = Database_requests.get_entitites_need_items()

    #generate map
    #1. create map

    #create map object
    map = folium.Map(location=[42.34372, -71.074181],
                        zoom_start=13,
                        tiles="CartoDB dark_matter")

    #2. populate map

    for organization in all_entities:

        #filter for organization
        if organization['entity_type'] == "Organization":

            #populate organzations
            marker = folium.Marker(location=[organization['latitude'], organization["longitude"]], #can also be folium.CircleMarker
                           popup ='<strong>%s</strong>' %(organization["name"]),
                           tooltip = organization["name"] )

            marker.add_to(map)


    for in_need in persons_in_need:

        #populate organzations
        marker = folium.Marker(location=[in_need['latitude'], in_need["longitude"]], #can also be folium.CircleMarker
                       popup ='<strong>%s</strong>' %(in_need["entity_name"]),
                       tooltip = in_need["entity_name"] )

        marker.add_to(map)

    #3. save map

    #Generate map
    map.save('map_main.html')



#####################################################################################
#VIEW FUNCTIONS

def display_map():

    print('''
    <iframe src="map_main.html" height="500" width="700"></iframe>
    ''')

#####################################################################################

def display_organizations_list():

    print('''List of organizations.''')

    #1. create list
    all_entities = Database_requests.get_all_entities()
    for organization in all_entities:

            #filter for organization
            if organization['entity_type'] == "Organization":

                print('''
            <table>
            Organization Name: <strong>%s</strong>
            Address: %s
            Phone: 000-000-000
            Resources Provided: %s
            Resources Needed: %s
            </table>
            ''' % ((organization["entity_name"]),
                    (organization["address"])
                    (organization["entities_supply_items"])
                    (organization["entities_need_items"]))



#####################################################################################
#CONTROLLER FUNCTIONS

if __name__ == "__main__":

    print_top_of_page()
    print_menu()
    #-----------

    generate_map()
    display_organizations_list()

     #-----------
    print_bottom_of_page()
