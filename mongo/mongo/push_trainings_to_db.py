import pymongo #to work with Mongo
import get_students_for_course
import random
import update_sport_hours_when_new_training_added


client = pymongo.MongoClient("mongodb+srv://trnsprntt:Always888@sportscourse-odfej.mongodb.net/test?retryWrites=true&w=majority")
db = client.test


collection = db["trainings"]
new_collection = []



def students(course_id):
    students = get_students_for_course.get_students_for_course(course_id)
    students_attendance = []
    for student in students:
        students_attendance.append((str(student["first_name"]+" "+student["last_name"]), student["_id"], random.randint(0,1)))
    return students_attendance

students(1)

id=1
for i in range (100):
    json = {}
    json["_id"]=id
    json["date"]= str(random.randint(2019,2020))+"-"+str(random.randint(1,12))+"-"+str(random.randint(1,31))+"T"+str(random.randint(8,21))+":00:00"
    duration = random.randint(1,3)
    json["duration"]= duration
    course_id = random.randint(1,23)
    json["course_id"] = course_id
    students_attendance = students(course_id)
    json["students"] = students_attendance
    update_sport_hours_when_new_training_added.update_sport_hours(students_attendance, duration)
    new_collection.append(dict(json))
    id+=1

def push_trainings_to_db(date,duration,course_id):
    json = {}
    json["_id"] = len(collection)+1
    json["date"] = date
    json["duration"] = duration
    json["course_id"] = course_id
    json["students"] = students(course_id)
    collection.insert_one(dict(json))

collection.drop()
collection.insert_many(new_collection)
