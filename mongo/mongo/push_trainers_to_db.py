import pymongo #to work with Mongo
# importing csv module
import csv
import dns
#authorization in Mongo


client = pymongo.MongoClient("mongodb+srv://trnsprntt:Always888@sportscourse-odfej.mongodb.net/test?retryWrites=true&w=majority")
db = client.test


collection = db["trainers"]

# csv file name
filename = "trainers.csv"

# initializing the titles and rows list
fields = []
rows = []
id = 1
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    collection.drop()
    for row in csvreader:
        json = {}
        json["_id"]=id
        json["first_name"]=row[1]
        json["last_name"]=row[2]
        json["email"] = row[3]
        collection.insert_one(dict(json))
        id+=1

