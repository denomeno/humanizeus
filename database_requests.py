#!C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe

import time
import mysql.connector

"""
cnx = mysql.connector.connect(user='root', password='',
                                host='localhost',
                                database='homeless_project')
"""

host = "humanize-us.c1xrcwz9rqrf.us-east-2.rds.amazonaws.com"
port = "3306"

cnx = mysql.connector.connect(user='humanizeusmaster', password='humanproject',
                                    host=host, port = port,
                                    database='humanizeusmaster')


class Database_requests:

    '''

    This class houses methods to interact with the MySQL database.

    Table of Contentst:
    1. Get Functions
    2. Insert Functions

    '''

    #############################################################

    #---------------1-GET FUNCTIONS------------------------------

    def get_entities_need_items():#enetity_type = entity_type
        myc = cnx.cursor(dictionary = True)
        myc.execute("""
SELECT

    `entities`.`entity_id`,
    IFNULL(`entities`.`name`, '') AS `entity_name`,
    IFNULL(`entities`.`latitude`, '') AS `latitude`,
    IFNULL(`entities`.`longitude`, '') AS `longitude`,
    `items`.`name` AS `item_name`,
    `entities_need_items`.`quantity_requested`,
    `entities_need_items`.`quantity_fulfilled`,
    IFNULL(`entities_need_items`.`time_in_1`, '') AS `time_in_1`,
    IFNULL(`entities_need_items`.`time_out_1`, '') AS `time_out_1`

FROM `entities_need_items`

JOIN `entities`
ON `entities_need_items`.`entity_id` = `entities`.`entity_id`

JOIN `items`
ON `entities_need_items`.`item_id`=`items`.`item_id`""")
        return myc.fetchall()


    def get_entities_supply_items():
        myc = cnx.cursor(dictionary = True)
        myc.execute("""
SELECT

    `entities`.`name` AS `entity_name`,
    `items`.`name` AS `item_name`,
    IFNULL(`entities`.`latitude`, '') AS `latitude`,
    IFNULL(`entities`.`longitude`, '') AS `longitude`,
    `entities_supply_items`.`quantity_requested`,
    `entities_supply_items`.`quantity_fulfilled`,
    `entities_supply_items`.`time_in_1`,
    `entities_supply_items`.`time_out_1`

FROM `entities_supply_items`

JOIN `entities`
ON `entities_supply_items`.`entity_id` = `entities`.`entity_id`

JOIN `items`
ON `entities_supply_items`.`item_id`=`items`.`item_id`""")
        return myc.fetchall()


    def get_organizations_need_items(email):
        myc = cnx.cursor(dictionary = True)
        myc.execute("""
SELECT
    `entities_need_items`.`entities_need_items_id`,
    `entities`.`name` AS `entity_name`,
    `items`.`name` AS `item_name`,
    `entity_types`.`description`,
    `entities_need_items`.`quantity_requested`,
    `entities_need_items`.`quantity_fulfilled`,
    `entities`.`latitude`,
    `entities`.`longitude`,
    `entities_need_items`.`time_in_1`,
    `entities_need_items`.`time_out_1`


FROM `entities_need_items`

JOIN `items`
ON `entities_need_items`.`item_id`=`items`.`item_id`

JOIN `entities`
ON `entities_need_items`.`entity_id` = `entities`.`entity_id`

JOIN `entity_types`
ON  `entity_types`.`type_id` = `entities`.`type_id`

WHERE `entity_types`.`description` = 'Organization'
AND `entities`.`email` = %s
""", (email, ))
        return myc.fetchall()

    def get_organizations_supply_items(email):
        myc = cnx.cursor(dictionary = True)
        myc.execute("""
    SELECT
        `entities_supply_items`.`entities_supply_items_id`,
        `entities`.`name` AS `entity_name`,
        `entities`.`email`,
        `items`.`name` AS `item_name`,
        `entity_types`.`description`,
        `entities_supply_items`.`quantity_requested`,
        `entities`.`latitude`,
        `entities`.`longitude`,
        `entities_supply_items`.`time_in_1`,
        `entities_supply_items`.`time_out_1`


    FROM `entities_supply_items`

    JOIN `items`
    ON `entities_supply_items`.`item_id`=`items`.`item_id`

    JOIN `entities`
    ON `entities_supply_items`.`entity_id` = `entities`.`entity_id`

    JOIN `entity_types`
    ON  `entity_types`.`type_id` = `entities`.`type_id`

    WHERE `entity_types`.`description` = 'Organization'
    AND `entities`.`email` = %s
    """, (email, ))
        return myc.fetchall()


    def get_all_items():
        myc = cnx.cursor(dictionary = True)
        myc.execute("""
SELECT

    `items`.`name`,
    `items`.`description`

FROM `items`;""")
        return myc.fetchall()


    def get_all_entities():
        myc = cnx.cursor(dictionary = True)
        myc.execute("""
SELECT

    `entities`.`entity_id`,
    IFNULL(`entities`.`name`, '') AS `name`,
    IFNULL(`entities`.`address`,  '') AS `address`,
    IFNULL(`entities`.`phone`, '') AS `phone`,
    IFNULL(`entity_types`.`description`,  '') AS `entity_type`,
    IFNULL(`entities`.`latitude`, '') AS  `latitude`,
    IFNULL(`entities`.`longitude`,  '') AS  `longitude`


FROM `entities`
JOIN `entity_types`
ON `entity_types`.`type_id` = `entities`.`type_id`;""")
        return myc.fetchall()




    def get_entity_id_from_email(email):
        myc = cnx.cursor(dictionary = True)
        myc.execute("""
SELECT

    `entities`.`entity_id`

FROM `entities`
WHERE `entities`.`email` = %s;""", (email, ))
        return myc.fetchall()


    def get_all_matches():
        myc = cnx.cursor(dictionary = True)
        myc.execute("""

    SELECT

        `matches`.`match_id`,
        `items`.`item_id`,
        `items`.`name`,
        `need_entities`.`entity_id` AS `in_need_entity_id`,
        `need_entities`.`name` AS `in_need_name`,
        `supply_entities`.`entity_id` AS `supply_entity_id`,
        `supply_entities`.`name` AS `supply_name`


    FROM `matches`

    JOIN `entities_need_items`
    ON `entities_need_items`.`entities_need_items_id` = `matches`.`entities_need_items_id`

    JOIN `entities_supply_items`
    ON `entities_supply_items`.`entities_supply_items_id` = `matches`.`entities_supply_items_id`

    JOIN `entities` AS `need_entities`
    ON `need_entities`.`entity_id` = `entities_need_items`.`entity_id`

    JOIN `entities` AS `supply_entities`
    ON `supply_entities`.`entity_id` = `entities_supply_items`.`entity_id`

    JOIN `items`
    ON `entities_need_items`.`item_id` = `items`.`item_id`

    ;""")


        return myc.fetchall()



    #############################################################

    #---------------2-INSERT FUNCTIONS---------------------------


    def insert_into_entities(email, name, address, type):
        myc = cnx.cursor()
        myc.execute("""
INSERT IGNORE INTO `homeless_project`.`entities`

(`email`, `name`, `address`, `type_id`)

VALUES (%s, %s, %s, (SELECT
                        `entity_types`.`type_id`
                        FROM `entity_types`
                        WHERE `entity_types`.`description` = %s));""", (email, name, address, type))
        cnx.commit()


    def insert_into_entities_need_items(entity_id, item_name, description, quantity_requested):
        myc = cnx.cursor()
        myc.execute("""
INSERT INTO `homeless_project`.`entities_need_items`

(`entity_id`, `item_id`, `description`, `quantity_requested`)

VALUES (%s,

        (SELECT
                `items`.`item_id`
            FROM `items`
            WHERE `items`.`name` = %s),

        %s,
        %s);

""", (entity_id, item_name, description, quantity_requested))

        cnx.commit()


    def insert_into_entities_supply_items(entity_id, item_name, description, quantity_requested, time_in_1):
        myc = cnx.cursor()
        myc.execute("""
INSERT INTO `homeless_project`.`entities_supply_items`

(`entity_id`, `item_id`, `description`, `quantity_requested`)

VALUES (%s,

        (SELECT
                `items`.`item_id`
            FROM `items`
            WHERE `items`.`name` = %s),

        %s,
        %s,
        %s);

""", (entity_id, item_name, description, quantity_requested, time_in_1))

        cnx.commit()
