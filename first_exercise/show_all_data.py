#!/usr/bin/python3

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

cursor = mycol.find({})
for i, document in enumerate(cursor):
      print(i, document)
