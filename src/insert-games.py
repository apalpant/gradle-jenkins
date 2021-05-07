import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

dblist = myclient.list_database_names()

print(myclient.list_database_names())
    
mydb = myclient["mydatabase-webservices"]

print(mydb.list_collection_names())

mycol = mydb["games"]

mylist = [
{
    "id": 0,
    "name": "Scrabble",
    "editor": "mattel",
    "year_published": "1978",
    "description": "descp",
    "category": "family",
    "time": "60min",
    "number_player": "2-5"
  },
  {
    "id": 1,
    "name": "Aventuriers du rail",
    "editor": "asmodee",
    "year_published": "2006",
    "description": "descp",
    "category": "family",
    "time": "45min",
    "number_player": "2-5"
  }
]

x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)