'''
Let's get started!

This is the main entry point for the project. This will create the databases,
then allow for some user input to perform some basic CRUD operations on the
data we stored. Give it a try!

Command Line Arguments:
optional [-n] - if present, creates a new instance of the MongoDB

Created: April 22, 2018
By: Alexander Gimmi
'''

import sys, getopt
from api import etl
from api import crud
from api import models
from pymongo import MongoClient
from pprint import pprint

def main(argv):
    # Check command line flags to see if we need a new instance of the database
    new_db = False
    try:
        opts, args = getopt.getopt(argv, 'hn')
    except getopt.GetoptError:
        print('main.py [-n]')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('main.py [-n]')
            sys.exit()
        elif opt in ('-n'):
            new_db = True

    if new_db:
        etl.create_database()

    # Main Loop
    while True:
        # Take valid user input
        opt = input("1. Create" +
            "\n2. Find One" +
            "\n3. Find All" +
            "\n4. Update" +
            "\n5. Delete One" +
            "\n6. Exit" +
            "\nPlease choose one of the above: ")

        if not (opt.isdigit() and 1 <= eval(opt) <= 6):
            continue
        elif opt == "6":
            break

        # Parse user input
        print("What collection would you like to perform this action on?")
        if opt == "1":
            create()
        elif opt == "2":
            find_one()
        elif opt == "3":
            find()
        elif opt == "4":
            update_by_id()
        elif opt == "5":
            delete_by_id()

# Workflow for creating a new data entry
def create():
    collection = get_collection()
    json_data = create_helper(collection.name)
    crud.create(collection, json_data)

# Creates a new json object with user entered data
def create_helper(collection_name):
    json_data = {}

    if collection_name == "marvel_heroes":
        json_data = models.Hero.new().to_json()
    elif collection_name == "marvel_villains":
        json_data = models.Villain.new().to_json()
    elif collection_name == "marvel_stats":
        json_data = models.Stats.new().to_json()

    return json_data

# Workflow for finding a single matching element
def find_one():
    collection = get_collection()
    selector = find_helper(collection.name)
    result = crud.find_one(collection, selector)

    if result == None:
        print("No matching data entry found.")
    else:
        pprint(result)

# Workflow for finding multiple matching elements
def find():
    collection = get_collection()
    selector = find_helper(collection.name)
    result = crud.find(collection, selector)

    if result.count() == 0:
        print("No matching data entries found.")
    else:
        for r in result:
            pprint(r)

# Creates a new selector object with user entered data
# Note: Selectors can contain 1 or many targets - leave unused properties blank
def find_helper(collection_name):
    selector = {}

    if collection_name == "marvel_heroes":
        selector = models.Hero.new().to_selector()
    elif collection_name == "marvel_villains":
        selector = models.Villain.new().to_selector()
    elif collection_name == "marvel_stats":
        selector = models.Stats.new().to_selector()

    return selector

# Workflow for updating a single matching element
def update_by_id():
    collection = get_collection()
    selector = {'id' : input("ID: ")}
    json_data = create_helper(collection.name)
    if crud.update_one(collection, selector, {'$set' : json_data}) == None:
        print("Did not find any entries with the ID " + selector['id'] + ".")
    else:
        print("Entry with ID " + selector['id'] + " successfully updated.")

# Workflow for deleting a single matching element
def delete_by_id():
    collection = get_collection()
    selector = {'id' : input("ID: ")}
    if crud.delete_one(collection, selector).deleted_count > 0:
        print("Entry with ID " + selector['id'] + " successfully deleted.")
    else:
        print("Did not find any entries with ID " + selector['id'] + ".")

# Helper function used to determine which collection to act upon
def get_collection():
    # Establish a connection to the default local database
    client = MongoClient('localhost', 27017)
    db = client['gimmi']

    # Take valid user input
    opt = input("1. Hero" +
        "\n2. Villain" +
        "\n3. Stats" +
        "\nPlease choose one of the above: ")

    # Parse user input
    if opt == "1":
        return db['marvel_heroes']
    elif opt == "2":
        return db['marvel_villains']
    elif opt == "3":
        return db['marvel_stats']
    else:
        return get_collection()


if __name__ == '__main__':
    main(sys.argv[1:])