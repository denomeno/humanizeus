import mysql.connector

host = "humanize-us.c1xrcwz9rqrf.us-east-2.rds.amazonaws.com"

port = "3306"


cnx = mysql.connector.connect(user='humanizeusmaster', password='humanproject',
                                    host=host, port = port)
                                    #database='humanize-us')
