#Encuentra el primer documento en la colección de clientes:
#import pymongo
#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#mydb = myclient["mydatabase"]
#mycol = mydb["customers"]
#x = mycol.find_one()
#print(x)


#Devuelva todos los documentos de la colección "clientes" e imprima cada documento:
#import pymongo
#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#mydb = myclient["mydatabase"]
#mycol = mydb["customers"]
#for x in mycol.find():
#  print(x)


#Devuelve solo los nombres y direcciones, no los _ids:
#import pymongo
#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#mydb = myclient["mydatabase"]
#mycol = mydb["customers"]
#for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
#  print(x)


#Se produce un error si se especifican los valores 0 y 1 en el mismo objeto (excepto si uno de los campos es el campo _id):
#import pymongo
#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#mydb = myclient["mydatabase"]
#mycol = mydb["customers"]
#for x in mycol.find({},{ "name": 1, "address": 1 }):
#  print(x)


#Buscar documento(s) con la dirección "Park Lane 38":
#import pymongo
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# myquery = { "address": "Park Lane 38" }
# mydoc = mycol.find(myquery)
# for x in mydoc:
#   print(x)


#Busque documentos cuya dirección comience con la letra "S" o superior:
# import pymongo
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# myquery = { "address": { "$gt": "S" } }
# mydoc = mycol.find(myquery)
# for x in mydoc:
#   print(x)


# #Busque documentos cuya dirección comience con la letra "S":
# import pymongo
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# myquery = { "address": { "$regex": "^S" } }
# mydoc = mycol.find(myquery)
# for x in mydoc:
#   print(x)


# #Ordena el resultado alfabéticamente por nombre:
# import pymongo
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# mydoc = mycol.find().sort("name")
# for x in mydoc:
#   print(x)


# #Ordena el resultado alfabéticamente en orden inverso por nombre:
# import pymongo
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# mydoc = mycol.find().sort("name", -1)
# for x in mydoc:
#   print(x)


# #Elimine el documento con la dirección "Montaña 21":
# import pymongo
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# myquery = { "address": "Mountain 21" }
# mycol.delete_one(myquery)


# #Elimine todos los documentos cuya dirección comience con la letra S:
# import pymongo
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# myquery = { "address": {"$regex": "^S"} }
# x = mycol.delete_many(myquery)
# print(x.deleted_count, " documents deleted.")


# #Eliminar todos los documentos de la colección "clientes":
# import pymongo
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# x = mycol.delete_many({})
# print(x.deleted_count, " documents deleted.")


# #Eliminar la colección "clientes":
# import pymongo
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# mycol.drop()


# import pymongo
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# mylist = [
#   { "_id": 1, "name": "John", "address": "Highway 37"},
#   { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
#   { "_id": 3, "name": "Amy", "address": "Apple st 652"},
#   { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
#   { "_id": 5, "name": "Michael", "address": "Valley 345"},
#   { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
#   { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
#   { "_id": 8, "name": "Richard", "address": "Sky st 331"},
#   { "_id": 9, "name": "Susan", "address": "One way 98"},
#   { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
#   { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
#   { "_id": 12, "name": "William", "address": "Central st 954"},
#   { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
#   { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
# ]
# x = mycol.insert_many(mylist)
# #print list of the _id values of the inserted documents:
# print(x.inserted_ids)


# #Cambie la dirección de "Valley 345" a "Canyon 123":
# import pymongo
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# myquery = { "address": "Valley 345" }
# newvalues = { "$set": { "address": "Canyon 123" } }
# mycol.update_one(myquery, newvalues)
# #print "customers" after the update:
# for x in mycol.find():
#   print(x)


# #Actualiza todos los documentos cuya dirección comience con la letra "S":
# import pymongo
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# myquery = { "address": { "$regex": "^S" } }
# newvalues = { "$set": { "name": "Minnie" } }
# x = mycol.update_many(myquery, newvalues)
# print(x.modified_count, "documents updated.")


#Limitar el resultado para que devuelva solo 5 documentos:
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
myresult = mycol.find().limit(5)
#print the result:
for x in myresult:
  print(x)
