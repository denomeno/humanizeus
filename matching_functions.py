# Humanize-Us
import time


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
