import pymongo #to work with Mongo
import get_sport_hours
#authorization in Mongo


client = pymongo.MongoClient("mongodb+srv://trnsprntt:Always888@sportscourse-odfej.mongodb.net/test?retryWrites=true&w=majority")
db = client.test



collection = db["students"]

def update_sport_hours(students_attendance,training_duration):
    for i in range (len(students_attendance)):
        if(students_attendance[i][2]==1):
            #get current amount of sports hours
            current_hours = get_sport_hours.get_sport_hours(students_attendance[i][1])
            #add hours
            collection.update(
                {"_id": students_attendance[i][1]},
                {"$set": {"sport_hours": current_hours+training_duration}});




