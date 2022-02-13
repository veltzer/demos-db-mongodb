#!/usr/bin/python3

import csv
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

with open('movies.csv', 'r') as file:
    reader = csv.reader(file)
    # skip the header line of the CSV file
    next(reader)
    for i, row in enumerate(reader):
        f_name = row[8]
        f_description = row[9]
        one_movie_data = { "name": f_name, "description": f_description }
        x = mycol.insert_one(one_movie_data)
        assert x.acknowledged, "insert did not succeed"
        print(f"the id of the new data is {x.inserted_id} {i}")
