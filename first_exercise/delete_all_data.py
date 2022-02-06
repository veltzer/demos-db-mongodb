#!/usr/bin/python3

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

result = mycol.delete_many({})
print(f"{result.deleted_count} documents were deleted")
