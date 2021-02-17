from pymongo import MongoClient

client = MongoClient()

db = client.labflask

celebrities = client.labflask.celebrities
movies = client.labflask.movies


