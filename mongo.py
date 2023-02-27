import pymongo

client = pymongo.MongoClient("<your connection string>")

db = client['exampledb']
print("Database created")

#Verification
""" print("List of databases")
print(client.list_database_names()) """

#Creating a collection
collection = db['example']
print("Collection created........")

#Inserting document into a collection
doc1 = {"name": "Ram", 
        "age": "26", 
        "city": "Hyderabad"}
collection.insert_one(doc1)
print(collection.find_one())

#Inserting document into a collection
data = [
   {
      "_id": "101", 
      "name": "Ram", 
      "age": "26", 
      "city": "Hyderabad"
   },
   {
      "_id": "102", 
      "name": "Rahim", 
      "age": "27", 
      "city": "Bangalore"
   },
   {
      "_id": "103", 
      "name": "Robert", 
      "age": "28", 
      "city": "Mumbai"
   }
]
res = collection.insert_many(data)
print("Data inserted ......")
print(res.inserted_ids)

#Retrieving a record with is 103 using the find_one() method
print("Record whose id is 103: ")
print(collection.find_one({"_id": "103"}))

#Retrieving all the records using the find() method
print("Records of the collection: ")
print(collection.find())

for doc1 in collection.find():
    print(doc1) 

#Retrieving records with age == 26 using the find() method
print("Record whose age is equal to 26: ")
for doc2 in collection.find({"age":"26"}):
    print(doc2)

#Retrieving records with age > 26 using the find() method
print("Record whose age is > than 26: ")
for doc2 in collection.find({"age":{"$gt":"26"}}):
    print(doc2)

#Retrieving records with age >= 26 using the find() method
print("Record whose age is >= than 26: ")
for doc2 in collection.find({"age":{"$gte":"26"}}):
    print(doc2)


#Retrieving records name Ram using the find() method
print("Record name is Ram: ")
for doc2 in collection.find({"name":"Ram"}):
    print(doc2)

# delete record with id 103
collection.delete_one({"_id": "103"})

# delete all the records where age >26
collection.delete_many({"age": {"$gt": "26"}})

# update a record
collection.update_one({"_id": "101"}, {"$set": {"age": "30"}})

# update multiple records
collection.update_many( {"$set": {"age": "30"}})

# sort records based on age
print("Records sorted on the basis of age")
for doc2 in collection.find().sort("age"):
    print(doc2) 

# drop a collection
collection.drop()

