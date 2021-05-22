from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false")
db=client.admin
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
#pprint(serverStatusResult)
pprint(client['perceptool-v0']['tracks'].find_one({"track_id":"6J8ZycfHriIYpJbmo0wN27"}))
pprint("")
response = client['perceptool-v0']['tracks'].find_one({"track_id":"7"})
pprint(response)
pprint(type(response))