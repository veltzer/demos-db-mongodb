#!/usr/bin/python3

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydict = { "name": "Mark", "address": "Highway 37" }

x = mycol.insert_one(mydict)
assert x.acknowledged, "insert did not succeed"
print(f"the id of the new data is {x.inserted_id}")
