'''
Hello again Tembo!

This file handles all the create, read, update, and delete operations on the
Marvel data in our NoSql database. This is where all the lifting of our API
is done!

I chose not to implement update_all and delete_all because I didn't want my
API to support that functionality.

Created: April 22, 2018
By: Alexander Gimmi
'''

# Create a new database entry given a collection and some data
def create(collection, json_data):
    collection.insert(json_data)

# Finds the first element in the collection that matches the given selector
def find_one(collection, selector):
	return collection.find_one(selector)

# Finds all elements in the collection that match the given selector
def find(collection, selector):
	return collection.find(selector)

# Updates the first element in the collection that matches the given selector
def update_one(collection, selector, json_data):
	return collection.update_one(selector, json_data)

# Updates all elements in the collection that match the given selector
#def update(collection, selector, json_data):
#	return collection.update(selector, json_data)

# Delete the first matching element in the collection that matches the given selector
def delete_one(collection, selector):
	return collection.delete_one(selector)

# Delete all elements in the collection that match the given selector
#def delete_many(collection, selector):
#	collection.delete_many(selector)
