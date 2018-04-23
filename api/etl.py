'''
Hello Tembo!

This file is designed to take all the steps necessary for extracting,
transforming, and loading the Marvel data into a NoSql database.

Created: April 22, 2018
By: Alexander Gimmi
'''

import os
from os.path import dirname, abspath
import sys
import csv, json
from pymongo import MongoClient

# Create a new MongoDB instance from the csv data
def create_database():
    # Establish a connection to the default local database
    client = MongoClient('localhost', 27017)
    db = client['gimmi']

    # Convert all csv files in the data directory
    rootdir = dirname(dirname(os.path.abspath(__file__)))
    datadir = os.path.join(rootdir, 'data')

    for subdir, dirs, files in os.walk(datadir):
        for file in files:
            filename = file.split('.')
            if filename[-1] == 'csv':
                print("Converting", filename[-2] + '.csv')
                json_data = csv_to_json(os.path.join(datadir, file))

                # Empty the DB then create a collection for each csv file
                db[filename[-2]].delete_many({})
                db[filename[-2]].insert_many(json.loads(json_data))

# Read csv file and return pretty-printed json
def csv_to_json(file):
    csv_rows = []
    with open(file, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        headers = reader.fieldnames

        # For each row, assign key:value pairs between the header and the data points
        for row in reader:
            csv_rows.extend([{headers[i]:row[headers[i]] for i in range(len(headers))}])
    
    return json.dumps(csv_rows, sort_keys=False, indent=4, separators=(',', ':'))


if __name__ == '__main__':
    create_database()