'''
This was a late addition to the project, but it really helped to clean up the
structure of some of the code. Here are some skeleton classes used as models
for any data entry in the Marvel database. They allow for easy creation of json
or selectors (dictionaries used for filtering).

Created: April 22, 2018
By: Alexander Gimmi
'''

# Represents any kind of data used in our database
class DbObject:

	def to_json(self):
		return vars(self)

	def to_selector(self):
		return {k: v for k, v in vars(self).items() if v is not ''}

# Represents a Hero data entry
class Hero(DbObject):

	def __init__(self, entity_id, name, identity, align, eye, hair, sex, alive, first_appearance, year):
		self.id = entity_id
		self.name = name
		self.identity = identity
		self.align = align
		self.eye = eye
		self.hair = hair
		self.sex = sex
		self.alive = alive
		self.first_appearance = first_appearance
		self.year = year

	def new():
		print("Enter the following information for your hero...")
		entity_id = input("ID: ")
		name = input("Name: ")
		identity = input("Identity: ")
		align = input("Align: ")
		eye = input("Eye: ")
		hair = input("Hair: ")
		sex = input("Sex: ")
		alive = input("Alive: ")
		first_appearance = input("First Appearance: ")
		year = input("Year: ")

		return Hero(entity_id, name, identity, align, eye, hair, sex, alive, first_appearance, year)

# Represents a Villain data entry
class Villain(DbObject):

	def __init__(self, entity_id, name, identity, eye, hair, sex, alive, at_large, first_appearance, year):
		self.id = entity_id
		self.name = name
		self.identity = identity
		self.eye = eye
		self.hair = hair
		self.sex = sex
		self.alive = alive
		self.at_large = at_large
		self.first_appearance = first_appearance
		self.year = year

	def new():
		print("Enter the following information for your villain...")
		entity_id = input("ID: ")
		name = input("Name: ")
		identity = input("Identity: ")
		eye = input("Eye: ")
		hair = input("Hair: ")
		sex = input("Sex: ")
		alive = input("Alive: ")
		at_large = input("At Large: ")
		first_appearance = input("First Appearance: ")
		year = input("Year: ")

		return Villain(entity_id, name, identity, eye, hair, sex, alive, at_large, first_appearance, year)

# Represents a Stats data entry
class Stats(DbObject):

	def __init__(self, entity_id, metric_id, year, value):
		self.entity_id = entity_id
		self.metric_id = metric_id
		self.year = year
		self.value = value

	def new():
		print("Enter the following information for your stats...")
		entity_id = input("Entity ID: ")
		metric_id = input("Metric ID: ")
		year = input("Year: ")
		value = input("Value: ")

		return Stats(entity_id, metric_id, year, value)