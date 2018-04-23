## Tembo Python Performance Task
*Goal*: Transform and load source data into a NoSQL database; create a REST API that allows access to Marvel heroes, villains, and their stats.

### Source data
`marvel_heroes.csv`: Contains a list of Marvel heroes and their profile attributes.
`marvel_villains.csv`: Contains a list of Marvel villains
`stats.csv`: Contains stats for each of the X-Men and villains

### Expected results
* A NoSQL database (or script to create one) containing the transformed source data, accessible via a REST API.
* All transformation code/scripts for the ETL process.
* API should allow anyone to access the heroes, villains, and their associated statistics.
* Tests should be included that demonstrate the capabilities and limitations of the API you create.
* Implementation is expected to be completed in Python 3.
* You are encouraged to ask questions along the way.
* This task is meant to be completed in 2-4 hours. It's better to solve minimally than to spend more time adding features.

### Dependencies
* Python v3.6.5
* MongoDB v3.6.4
* PyMongo v3.6.1
* StackOverflow

### Setup
1. Open a new terminal window and change directory to the location of this project
2. Run `python` and then do the following in order
    1. `import sys`
    2. `sys.append('/the/path/to/the/project/directory')`
    3. `exit()`
2. To start the MongoDB server, run `mongod --dbpath ./data/mongodb`
3. There are a few ways to start the project...
    1. If this is your first time running the project on your machine, run `python project/main.py ARGS` to start with a fresh database.
    2. Otherwise, you can simply run `python project/main.py` to avoid recreating the database and get right into the data manipulation.
4. If you have any questions or feedback, or run into any problems please let me know!