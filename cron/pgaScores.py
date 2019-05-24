#!/usr/bin/python3
import json
import pymongo
import requests


pga_request = requests.get(
    "http://statdata.pgatour.com/r/current/leaderboard-v2mini.json"
)

# PyMongo Info
client = pymongo.MongoClient('mongodb://database:27017')

db = client['scores']
collection = db['actual']

collection.find_one_and_replace({}, pga_request.json(), upsert=True)

client.close()
