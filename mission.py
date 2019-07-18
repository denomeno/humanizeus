#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe

from import_modules import *

#THE ABOVE SECTION SHOULD EXIST AT THE TOP OF EVERY PAGE
#####################################################################################

def description_of_mission():
    print('''
    <h2>We have a mission.</h2>
    <u>Mission:</u> HumanizeUs's mission is to provide a technical solution to improve access to essential home items for persons that are entering stable housing in our communities.

    <br>
    <u>Vision:</u> We envision a world where all of our neighbors support each other to have a healthy and sustainable home.

    <br>
    HumanizeUs is a non-profit dedicated to fighting homelessness by connecting the community through enabling people to donate directly to those in their local community that are in need. We mobilize resources via geographical information systems. Our online platform changes the traditional model of donating to organizations by centralizing the needs of organizations working in the field and the resources of the community to systematically deliver newly housed people with essential living items.

    <h5>Thank you for joining our cause!<h5>
    ''')

#####################################################################################
#CONTROLLER FUNCTIONS

if __name__ == "__main__":

     print_headers()
     print_top_of_page()
     print_menu()
     #-----------

     description_of_mission()

     #-----------
     print_bottom_of_page()
