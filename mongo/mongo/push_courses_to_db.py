import pymongo #to work with Mongo
# importing csv module
import csv
import dns
#authorization in Mongo


client = pymongo.MongoClient("mongodb+srv://trnsprntt:Always888@sportscourse-odfej.mongodb.net/test?retryWrites=true&w=majority")
db = client.test


collection = db["courses"]

def get_trainer_by_mail(mail):
    col = db["trainers"]
    trainer_id = col.aggregate([
        {
            "$match": {
                "email": mail,
            }
        },
        {
            "$project": {
                "_id": 1,
            }
        },
    ])
    return (trainer_id.next()["_id"])

# csv file name
filename = "trainers.csv"

# initializing the titles and rows list
fields = []
rows = []
id = 1
mail = "a.pavlova@innopolis.ru"
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
        json["title"]=row[0]
        json["trainer_id"]= get_trainer_by_mail(row[3])
        collection.insert_one(dict(json))
        id+=1



