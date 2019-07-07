# Humanize-Us
import time
import mysql.connector

#connect to database
cnx = mysql.connector.connect(user='root', password='',
                                host='localhost',
                                database='homeless_project')


class Database_requests:

    #----------------------------
    #`DATABASE_REQUESTS` CLASS SECTIONS

    #1. GET REQUESTS
    #2. INSERT REQUESTS
    #3. UPDATE REQUESTS
    #4. DELETE REQUESTS
    #----------------------------


    #1. GET REQUESTS


    def get_entities_need_items():#enetity_type = entity_type
        myc = cnx.cursor(dictionary = True)
        myc.execute("""
SELECT
    `entities`.`entity_id`,
    `entities`.`name` AS `entity_name`,
    `items`.`item_id`,
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

    `entities`.`entity_id`,
    `entities`.`name` AS `entity_name`,
    `items`.`item_id`,
    `items`.`name` AS `item_name`,
    `entities_supply_items`.`time_in_1`,
    `entities_supply_items`.`time_out_1`,
    `entities_supply_items`.`time_in_2`,
    `entities_supply_items`.`time_out_2`,
    `entities_supply_items`.`time_in_3`,
    `entities_supply_items`.`time_out_3`

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

    `item`.`item_id`,
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


    def get_all_matches():
        myc = cnx.cursor(dictionary = True)
        myc.execute("""
SELECT
    *
FROM `matches`;""")
        return myc.fetchall()


    #2. INSERT REQUESTS

    def insert_into_matches(item_id, supplier_entity_id, receiver_entity_id, fulfillment_status):
        myc = cnx.cursor()
        myc.execute("""

INSERT INTO
    `homeless_project`.`matches`

(`item_id`, `supplier_entity_id`, `receiver_entity_id`, `fulfillment_status`)

VALUES  (%s, %s, %s, %s)
        """, (item_id, supplier_entity_id, receiver_entity_id, fulfillment_status))
        cnx.commit()


    def




class Matching_functions:

    def match_needs_and_supply():

        #get all data
        needed_items = Database_requests.get_entities_need_items()
        supplied_items = Database_requests.get_entitites_supply_items()
        matches = Database_requests.get_all_matches()

        print(needed_items)
        print("\n\n")
        print(supplied_items)

        #final output list
        matched_items_list = []

        #matching iteration
        for needed_item in needed_items:

            for supplied_item in supplied_items:

                #MATCH CONDITIONS
                #1. SAME ITEM NAME
                #2. AN ITEM FROM A SUPPLIER PREVIOUSLY NOT FULFILLED IN ANOTHER MATCH

                #CONDITION - 1
                if needed_item['item_id'] == supplied_item['item_id']:

                    #add time slot match check
                    """
                    data = {

                    'item_name' : needed_item['item_name'],
                    'need_entity_name' : needed_item['entity_name'],
                    'supply_entity_name' : supplied_item['entity_name']
                    #add time matched time slot start-end times

                    }
                    """
                    #matched_items_list.append(data)

                    #CONDITION - 2

                    #for match in matches:

                    #    if match['item_id'] == needed_item['item_id'] and match['supplier_entity_id'] == supplied_item['entity_id'] and match['receiver_entity_id'] == needed_item['entity_id']:

                    print("Match executed.")

                    #insert into matched items
                    Database_requests.insert_into_matches(needed_item['item_id'], supplied_item['entity_id'], needed_item['entity_id'], 'No')
