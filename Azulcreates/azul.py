#!/usr/bin/python3
# author: Deniz Hallik (hallik@bu.edu)
# filename: azulcreates.py
# My online painting shop!

import MySQLdb as db    # the mysql database API
import time
import cgi
import cgitb; cgitb.enable() # web debugging package; always import it into your web apps

################################################################################
def connect_to_database():
    '''Create a connection object to connect to MySQL database.
    Return the connection and cursor objects.
    '''

    conn = db.connect(host="localhost",
                  user="hallik",
                  passwd="0705",
                  db="cs108_hallik_project")

    cursor = conn.cursor()
    return conn, cursor


#####################################################################################
def print_form_data(form):
    '''Display the form data for debugging purposes.
    '''
    # print out the form data (for debugging purposes)
    print('Form data:<br>')

    print('<table>')
    keys = list(form.keys())
    keys.sort()
    # go through all keys:
    for k in keys:

        print('''<tr>
                    <td>%s</td>
                    <td>%s</td>
                </tr>''' % (k, form[k]))


    print('</table><hr>')


#####################################################################################
def print_headers():
    '''Print the HTTP headers.'''

    # print the content-type header
    print("Content-Type: text/html")
    print() # blank line to indicate end of headers


#####################################################################################
def print_top_of_page(title):
    '''Print the top of the HTML page.'''

    print("""
<html>
<head>
<title>%s</title>
<style>

h1 {
        color: blue
        font-family: "Garamound";
}

body {
        background-color: white;
        text-align: center;
}

</style>
</head>

<body>
""" % title)

#####################################################################################
def print_bottom_of_page():
    '''Print the bottom of the HTML page.'''

    print('''
<hr>
This page was generated at %s.<br>
Return to the <a href="./a20_mini_facebook.py">main page</a>.
</body>
</html>
''' % time.ctime())


################################################################################
def get_all_paintings():
    """
    Middleware function to get all paintings from the paintinglist table.
    Returns a list of tuples of (painting_id, name, year, material, price, image_url).
    """

    # connect to database
    conn, cursor = connect_to_database()

    # build SQL
    sql = """
    SELECT painting_id, name, year, material, price, image_url
    FROM paintinglist
    """

    # execute the query
    cursor.execute(sql)

    # get the data from the database:
    data = cursor.fetchall()

    # clean up
    conn.close()
    cursor.close()

    return data

## end: def get_all_paintings():

################################################################################
def get_one_painting(painting_id):
    """
    Middleware function to retrieve one painting record from the database.
    Returns a list containing one tuple.
    """

    # connect to database
    conn, cursor = connect_to_database()

    # build SQL
    sql = """
    SELECT *
    FROM paintinglist
    WHERE painting_id=%s
    """

    # execute the query
    parameters = (int(painting_id), )
    cursor.execute(sql, parameters)

    # get the data from the database:
    data = cursor.fetchall()

    # clean up
    conn.close()
    cursor.close()

    return data

## end: def get_one_painting(painting_id):


################################################################################
def show_all_paintings(data):
    """
    Presentation layer function to display a table containing all paintings' last names
    and first names.
    """

    ## create an HTML table for output:
    print("""
    <h2> All Paintings</h2>
    <p>

    <table border=1>
      <tr>
        <th><font size=+1"><b>name</b></font></th>
        <th><font size=+1"><b>year</b></font></th>
        <th><font size=+1"><b>material</b></font></th>
        <th><font size=+1"><b>price</b></font></th>
        <th><font size=+1"><b>image</b></font></th>
      </tr>
    """)

    for record in data:

        # each iteration of this loop creates on record of output:
        (painting_id, name, year, material, price, image_url) = record

        print("""
      <tr>
        <td><a href="?profile_id=%s">%s</a></td>
        <td><a href="?profile_id=%s">%s</a></td>
        <td><a href="?profile_id=%s">%s</a></td>
        <td><a href="?profile_id=%s">%s</a></td>
        <td><a href="?profile_id=%s">%s</a></td>
      </tr>
        """ % (painting_id, name,
               painting_id, year,
               painting_id, material,
               painting_id, price,
               painting_id, image_url,))


    print("""
    </table>
    """)
    print("Found %d paintings.<br>" % len(data))

## end: def show_all_paintings(data):

################################################################################
def get_all_inspirations():
    """
    Middleware function to get all inspirations from the inspirations table.
    Returns a list of tuples of (inspiration_id, name, cob).
    """

    # connect to database
    conn, cursor = connect_to_database()

    # build SQL
    sql = """
    SELECT inspiration_id, name, cob
    FROM inspirations
    """

    # execute the query
    cursor.execute(sql)

    # get the data from the database:
    data = cursor.fetchall()

    # clean up
    conn.close()
    cursor.close()

    return data

## end: def get_all_inspirations():


################################################################################
def show_all_inspirations(data):
    """
    Presentation layer function to display a table containing all inspirations' name and cob.
    """

    ## create an HTML table for output:
    print("""
    <h2> All Inspirations</h2>
    <p>

    <table border=1>
      <tr>
        <th><font size=+1"><b>Name</b></font></th>
        <th><font size=+1"><b>Country of Birth</b></font></th>
      </tr>
    """)

    for record in data:

        # each iteration of this loop creates on record of output:
        (inspiration_id, name, cob) = record

        print("""
      <tr>
        <td><a href="?profile_id=%s">%s</a></td>
        <td><a href="?profile_id=%s">%s</a></td>
      </tr>
        """ % (inspiration_id, name,
               inspiration_id, cob,))


    print("""
    </table>
    """)
    print("Found %d inspirations.<br>" % len(data))

## end: def show_all_inspiration_id(data):


################################################################################
def show_painting_page(paintinglist_data, inspirations_data):
    """
    Presentation layer function to display the painting page for one painting.
    """

    ## show profile information
    record= paintinglist_data[0] # we expect only one record in this data set
    (painting_id, name, year, material, price, image_url) = record

    print("<h2>This painting is called %s and was made in %.</h2>" % (name, year))

    # painting info
    print("""
    <img src=%s width=200 height=200>
    <p>
    <table border=1>
        <tr>
            <td>Image</td>
            <td>%s</td>
        </tr>
        <tr>
            <td>Material</td>
            <td>%s</td>
        </tr>
        </tr>
        <tr>
            <td>Price</td>
            <td>%s</td>
        </tr>
    </table>
    """ % (image_url,
           material,
           price))


    # Update & Comment
    print('''
    <form>
    <p>
    <td>
    <input type="Submit" name="update_profile" value="Update">
    </td>
    <br>
    <tr>
    <th>What do you see in this painting?<th>
    <td><textarea> <name="message" rows="5" cols="50"><textarea></td>
    <td><input type="submit" name="insert_comment" value="Add Comment"></td>
    <input type="hidden" name="painting_id" value="%s">
    </tr>
    </form>
        '''% (painting_id))

    # show all inspirations
    heading = 'Inspirations of %s' % (name)
    show_all_inspirations(inspirations_data, heading)

    #show update
    print('<hr>')
    show_update_painting_form()


## end: def show_painting_page(data):


################################################################################
def get_inspirations_of_painting(painting_id):
    """
    Middleware function to get inspirations for painting from the inspirations table.
    Returns a list of tuples of (inspiration_id, name, cob).
    """

    # connect to database
    conn, cursor = connect_to_database()

    # build SQL
    sql = """
    SELECT inspirations.inspiration_id, inspirations.name, inspirations.cob
    FROM inspirations
    INNER JOIN paintings_inspirations ON paintings_inspirations.inspiration_id = inspirations.inspiration_id
    WHERE paintings_inspirations.painting_id = %s
    """

    # make tuple
    parameters = (painting_id, )

    # execute the query
    cursor.execute(sql, parameters)

    # get the data from the database:
    data = cursor.fetchall()

    # clean up
    conn.close()
    cursor.close()

    return data

## end: get_inspirations_of_painting(painting_id):



################################################################################

def insert_painting(name, year, material, price, image_url):
    '''Encapsulates HTML'''

    conn, cursor = connect_to_database()

    sql='''
    INSERT INTO paintinglist (painting_id, name, year, material, price, image_url)
    VALUE(%s,%s,%s,%s,%s,%s)
    '''

    parameters = (name, year, material, price, image_url)
    cursor.execute(sql, parameters)
    rowcount=cursor.rowcount
    cursor.close()
    conn.commit()
    conn.close()
    return rowcount



################################################################################
def show_add_painting_form():
    '''display HTML form to add new profile to the database'''

    print('''
    <h2> Made a new painting? </h2>
    <p>
    <form>
    <table>
        <tr>
            <td><label> Name</label></td>
            <td><center><input type="text" name="name"></center></td>

        </tr>
        <tr>
            <td><label>Year</label></td>
            <td><center><input type="text" name="year"></center></td>
        </tr>
        <tr>
            <td><label>Material</label></td>
            <td><center><input type="text" name="material"></center></td>
        </tr>
        <tr>
            <td><label>Price</label></td>
            <td><center><input type="text" name="price"></center></td>
        </tr>
        <tr>
            <td><label>Picture</label></td>
            <td><center><input type="text" name="image_url"></center></td>
        </tr>
        <tr>
            <th></th>
            <input type="submit" name="insert_painting" value="Add"><td>
        </tr>
    </table>
    </form>
    ''')



################################################################################
def update_painting(painting_id, name, year, material, price, image_url):
    '''Encapsulates HTML'''

    conn, cursor = connect_to_database()

    sql='''
    UPDATE paintings
    SET name=%s, year=%s,material=%s, price=%s,image_url=%
    WHERE painting_id=%s
    '''

    parameters = (name, year, material, price, image_url, painting_id)
    cursor.execute(sql, parameters)
    rowcount=cursor.rowcount
    cursor.close()
    conn.commit()
    conn.close()
    return rowcount



################################################################################
def show_update_painting_form(painting_id, name, year, material, price, image_url):
    '''display HTML form to update profile in the database'''

    print('''
    <h2> Want to update a painting? </h2>
    <p>
    <form>
    <input type='hidden' name='painting_id' value='%s'
    <table>
        <tr>
            <td><label> Name</label></td>
            <td><center><input type="text" name="name" value='%s'></center></td>

        </tr>
        <tr>
            <td><label>Year</label></td>
            <td><center><input type="text" name="year" value='%s'></center></td>
        </tr>
        <tr>
            <td><label>Material</label></td>
            <td><center><input type="text" name="material" value='%s'></center></td>
        </tr>
        <tr>
            <td><label>Price</label></td>
            <td><center><input type="text" name="price" value='%s'></center></td>
        </tr>
        <tr>
            <td><label>Picture</label></td>
            <td><center><input type="text" name="image_url" value='%s'></center></td>
        </tr>
        <tr>
            <th></th>
            <input type="submit" name="update_painting" value="Update"><td>
        </tr>
    </table>
    </form>
    '''%(painting_id, name, year, material, price, image_url))



################################################################################
def insert_comment(painting_id, message):
    ''' takes two parameters and adds to database'''

    conn, cursor = connect_to_database()

    #format current time as a timestamp
    tm= time.localtime()
    timestamp = '%04d-%02d-%02d %02d:%02d:%02d' % tm[0:6]

    # SQL query
    sql='''
    INSERT INTO comments (comment_id, painting_id, comment_time, message)
    VALUES (NULL, %s, %s, %s)
    '''

    parameters = (painting_id, timestamp, message)

    cursor.exeucte(sql, parameters)
    # add row count
    rowcount=cursor.rowcount

    conn.commit()
    conn.close()
    cursor.close()
    return rowcount

################################################################################
def show_comments_for_painting(data):
    """
    Presents comments for one painting.
    """

    print("""
    <h2>Comments made on %s </h2>
    <p>


    """ % name)

    print('''
    <table border=1>
        <tr>
            <th>Comment Time</th>
            <th>Comment</th>
        </tr>
    ''')

    for record in data:
        (comment_id, painting_id, comment_time, message) = record

    print("""
    <tr>
        <td>%s &nbsp; %s</td>
    </tr>
    """ % (comment_time, message))


################################################################################
def get_comments_for_painting(painting_id):
    """
    Middleware function to retrieve all comments record from the database.
    Returns a list containing one tuple.
    """

    # connect to database
    conn, cursor = connect_to_database()

    # build SQL
    sql = """
    SELECT *
    FROM comments
    WHERE painting_id=%s
    """

    # execute the query
    parameters = (int(painting_id), )
    cursor.execute(sql, parameters)

    # get the data from the database:
    data = cursor.fetchall()

    # clean up
    conn.close()
    cursor.close()

    return data


################################################################################
def get_inspirations(inspiration_id):
    """
    Shows painters inspired from.
    """

    # connect to database
    conn, cursor = connect_to_database()

    # build SQL
    # add inspirations tables for sql (JOIN)
    sql = """
    SELECT DISTINCT inspirations.inspiration_id, paintings.painting_id, paintings.name, paintings.year
    FROM inspirations INNER JOIN inspirations ON inspirations.inspiration_id=paintings.painting_id
    WHERE inspirations.painting_id=%s
    """



    # execute the query
    parameters = (painting_id,)
    cursor.execute(sql, parameters)

    # get the data from the database:
    data = cursor.fetchall()

    # clean up
    conn.close()
    cursor.close()

    return data



################################################################################
def show_inspirations(data):
    """
    Prints out table of inspirations's profiles.
    """

    print("""
    <h2>Showing All Inspirations</h2>
    <p>

    <table border=1>
      <tr>
        <td><font size=+1"><b>Name</b></font></td>
        <td><font size=+1"><b>Country of Birth</b></font></td>
      </tr>
    """)

    for record in data:

        # each iteration of this loop creates on record of output:
        (inspiration_id, painting_id, name, cob) = record

        print("""
      <tr>
        <td><a href="?painting_id=%s">%s</a></td>
        <td><a href="?painting_id=%s">%s</a></td>
      </tr>
        """ % (painting_id, name,
               painting_id, cob,))


    print("""
    </table>
    """)
    print("Found %d inspirations.<br>" % len(data))

################################################################################
def show_add_inspiration_form(painting):
    '''
    displays a form for you to add an inspiration
    '''

    print('''
    <h2> Add an inspiration </h2>
    <p>
    <form>
    <table>
        <tr>
            <td><label> Name </label></td>
            <td><center><input type="text" name="name"></center></td>
        </tr>
        <tr>
            <td><label>Country of Birth</label></td>
            <td><center><input type="text" name="last_name"></center></td>
        </tr>
        <tr>
            <td><input type="submit" name="insert_inspiration" value="Add!"></td>
        </tr>
    </table>
    </form>
        ''')


################################################################################
if __name__ == "__main__":


    print_headers()
    print_top_of_page('AzulCreates')

    form = cgi.FieldStorage() # obtain the HTTP form data into a python variable

    print_form_data(form) # debugging information about form data


    if 'painting_id' in form:
        # read HTTP form
        painting_id=form['painting_id'].value

        paintinglist_data = get_one_painting(painting_id) # get data for all paintings
        inspirations_data = get_inspirations_of_painting(painting_id)
        show_painting_page(paintinglist_data, inspirations_data)

    else:

        data=get_all_paintings()
        show_all_paintings(data)

##
##
##        if 'update_painting' in form:
##            name=form['name'].value
##            year=form['year'].value
##            material=form['material'].value
##            price=form['price'].value
##            image_url=form['image_url'].value
##
##            rc = update_painting(painting_id, name, year, material, price, image_url)
##            print("%d rows were inserted." %rc)
##
##        # done with update process
##
##        painting_data = get_one_painting(painting_id)
##        inspirations_data = get_inspirations(inspiration_id)
##
##        show_painting_page(painting_data, inspirations_data)
##
##
##
##    elif 'insert_painting' in form:
##        name=form['name'].value
##        year=form['year'].value
##        material=form['material'].value
##        price=form['price'].value
##        image_url=form['image_url'].value
##
##        rc=insert_painting(name, year, material, price, image_url)
##        print("%d rows were inserted." %rc)
##
##    elif 'show_add_painting_form' in form:
##        show_add_painting_form()

##
##
##        if 'complete_update' in form:
##            if('material' in form and 'image_url' in form and 'price' in form):
##                material=form['material'].value
##                image_url=form['image_url'].value
##                price=form['price'].value
##                rc=update_painting(painting_id, material, price, image_url)
##                print("%d rows were updated." %rc)
##            else:
##                print("<b>Cannot update painting, missing some required form data.<b>")
##
##        if 'insert_comment' in form:
##            painting_id=form['painting_id'].value
##            comment=form['comment'].value
##            rc=insert_comment(profile_id,comment)
##
##        if 'insert_friend' in form:
##            painting_id=form['painting_id'].value
##            inspiration_id=form['inspiration_id'].value
##            rc=add_inspiration(painting_id,inspiration_id)
##            print("%d rows were inserted." %rc)
####
##        data=get_one_painting(painting_id)
##        show_painting_page(data)
##
##        comments=get_comments_for_user(painting_id)
##        show_comments_for_painting(comments)
##
##        inspirations=get_inspirations(inspiration_id)
##        show_inspirations(inspirations)
##        show_add_inspiration_form(inspiration_id)


##
##    else:
##        data=get_all_paintings()
##        show_all_paintings(data)

    #standard bottom of page
    print_bottom_of_page()
