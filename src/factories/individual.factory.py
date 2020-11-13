from faker import Faker
from datetime import datetime
from bson.objectid import ObjectId
from data.sex import 

def create():
    return {
        "animal_id": ObjectId(allAnimals[animal]["_id"]),
        "nickname": nicknames[random.randint(0, allAnimals.count() - 1)],
        "date_arrive": fake.date(),
        "responsible": fake.name(),
        "healthStatus": healthStatus[random.randint(0, len(healthStatus) - 1)],
        "sex": sex[random.randint(0, len(sex) - 1)],
        "media": fake.profile()["website"]
    }