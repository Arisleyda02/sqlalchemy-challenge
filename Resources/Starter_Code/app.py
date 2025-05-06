# Import the dependencies.
# Import dependencies
from pymongo import MongoClient
from pprint import pprint


     

# Create an instance of MongoClient
mongo = MongoClient(port=27017)


     

# confirm that our new database was created
print(mongo.list_database_names())


     
['admin', 'classDB', 'config', 'epa', 'local', 'met', 'newDB', 'petsitly_marketing', 'uk_food']

# assign the uk_food database to a variable name
db = mongo['uk_food']


     

# review the collections in our new database
print(db.list_collection_names())


     
['establishments']

# review a document in the establishments collection
pprint(db.establishments.find_one())


     


#################################################
# Database Setup
#################################################


# reflect an existing database into a new model

# reflect the tables


# Save references to each table


# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################




#################################################
# Flask Routes
#################################################
