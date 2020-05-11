import pymongo #to work with Mongo
import dns

#authorization in Mongo

client = pymongo.MongoClient("mongodb+srv://trnsprntt:Always888@sportscourse-odfej.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

collection = db["students"]

def get_students_for_course(course_id):
    result = collection.aggregate([
        {
            "$match": {

                "sport_courses": course_id,
            }
        },
        {
            "$project": {
                "first_name": "$first_name",
                "last_name": "$last_name",
                "_id": 1,
            }
        },
    ])
    results = list(result)
    return results

#example for course with id=3
# students = get_students_for_course(3)
# for i in range (len(students)):
#     print(students[i])

