#!/usr/bin/python3
import json
import pymongo
import urllib.request as api

print("Starting API Request.")

pga_request = api.urlopen(
    "http://statdata.pgatour.com/r/current/leaderboard-v2mini.json"
)

pga_data = json.loads(pga_request.read().decode("utf-8"))

# print(pga_data)

print("Data Received from PGA Endpoint.")

# PyMongo Info
client = pymongo.MongoClient('mongodb://database:27017')

db = client['scores']
collection = db['actual']

collection.find_one_and_replace({}, pga_data, upsert=True)

print("Updated Document.")
