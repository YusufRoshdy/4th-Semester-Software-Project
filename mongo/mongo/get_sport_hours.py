import pymongo #to work with Mongo
import dns

#authorization in Mongo

client = pymongo.MongoClient("mongodb+srv://trnsprntt:Always888@sportscourse-odfej.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

collection = db["students"]

def get_sport_hours(student_id):
    result = collection.aggregate([
        {
            "$match": {
                "_id": student_id,
            }
        },
        {
            "$project": {
                "sport_hours": "$sport_hours",
                "_id": 0,
            }
        },
    ])
    return(result.next()['sport_hours'])



#in case we will need to do this using names, not ids
def get_sport_hours_by_name(first_name, last_name):
    result = collection.aggregate([
        {
            "$match": {
                "first_name": first_name,
                "last_name": last_name,
            }
        },
        {
            "$project": {
                "sport_hours": "$sport_hours",
                "_id": 0,
            }
        },
    ])
    return(result.next()['sport_hours'])



#example
#print("Sport hours for student with id=5:", get_sport_hours(5))