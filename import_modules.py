#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe

#print ("Content-type:text/html\r\n\r\n")

#import MySQLdb as db
#import mysql.connector # `pip install mysql-connector-python` - NOT NEEDED, ALREADY EXISTS IN `Humanize-Us.py`
import socket
import time
import timezone
import cgi
import cgitb; cgitb.enable()  # web debugging package
from flask import request, redirect #to get the submitted form data, and redirect browser
from flask import Flask
import folium #used to generate maps

import requests #for post/get requests
import json #to decode json

#######################################################3

from database_requests import *#dataabse MySQL request functions in a class
from google_requests import *#google api request functions
import matching_functions #matching functions for needs and providers


from index import *
