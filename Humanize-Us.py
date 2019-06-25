# Humanize-Us
import time
import mysql.connector

cnx = mysql.connector.connect(user='root', password='',
                                host='localhost',
                                database='homeless_project')

class Database_requests:

    def get_entitites_need_items():#enetity_type = entity_type
        myc = cnx.cursor(dictionary = True)
        myc.execute("""
SELECT
    `entities`.`name` AS `entity_name`,
    `items`.`name` AS `item_name`,
    `entities_need_items`.`time_in_1`,
    `entities_need_items`.`time_out_1`

FROM `entities_need_items`

JOIN `entities`
ON `entities_need_items`.`entity_id` = `entities`.`entity_id`

JOIN `items`
ON `entities_need_items`.`item_id`=`items`.`item_id`""")
        return myc.fetchall()


    def get_entitites_supply_items():
        myc = cnx.cursor(dictionary = True)
        myc.execute("""
SELECT

    `entities`.`name` AS `entity_name`,
    `items`.`name` AS `item_name`,
    `entities_supply_items`.`time_in_1`,
    `entities_supply_items`.`time_out_1`

FROM `entities_supply_items`

JOIN `entities`
ON `entities_supply_items`.`entity_id` = `entities`.`entity_id`

JOIN `items`
ON `entities_supply_items`.`item_id`=`items`.`item_id`""")
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
    `entities`.`name`,
    `entities`.`address`,
    `entity_types`.`description` AS `entity_type`

FROM `entities`
JOIN `entity_types`
ON `entity_types`.`type_id` = `entities`.`type_id`;""")
        return myc.fetchall()






class Matching_functions:

    def match_needs_and_supply():

        #get all data
        needed_items = Database_requests.get_entitites_need_items()
        supplied_items = Database_requests.get_entitites_supply_items()

        #final output list
        matched_items_list = []

        #matching iteration
        for needed_item in needed_items:

            for supplied_item in supplied_items:

                if needed_item['item_name'] == supplied_item['item_name']:

                    #add time slot match check

                    data = {

                    'item_name' : needed_item['item_name'],
                    'need_entity_name' : needed_item['entity_name'],
                    'supply_entity_name' : supplied_item['entity_name']
                    #add time matched time slot start-end times

                    }

                    matched_items_list.append(data)
