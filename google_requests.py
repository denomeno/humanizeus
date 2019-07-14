#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe

from import_modules import *

########################################################################

class Google_requests:

    def get_geocode(address):

        #prepare request varibales
        base_url = """https://maps.googleapis.com/maps/api/geocode/json"""
        api_key = "AIzaSyCDxPm_6eofnsoB5z80trBikEy6m4GT5hI" #obtained from google geocoding service on humanizeus account

        parameters = {"address": address,
                      "key" : api_key}

        #make the request
        response = requests.get(base_url, params = parameters)

        #check response cde and extract variables
        if response.status_code != 200:
            formatted_address = "N/A" 
            longitude = "N/A"
            latitude = "N/A"
        else:
            data = json.loads(response.text) #make data into a readable format

            formatted_address = data['results'][0]['formatted_address']
            latitude = data['results'][0]['geometry']['location']['lat']
            longitude = data['results'][0]['geometry']['location']['lng']


        #put the output in a dictionary format
        output = {"formatted_address" : formatted_address,
                  "latitude" : latitude,
                  "longitude": longitude}

        return output
