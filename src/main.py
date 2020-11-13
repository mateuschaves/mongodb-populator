from pymongo import MongoClient
from dotenv import load_dotenv
from faker import Faker
from bson.objectid import ObjectId
from datetime import datetime


import random
import os

load_dotenv()
fake = Faker()

client = MongoClient(os.environ.get("MONGO_DB_URI"))
database = client.data

animals = database.animals

allAnimals = animals.find({})

nicknames = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "Henri",
    "X-Men",
    "Afro",
    "Pink",
    "Size",
    "Chienne",
    "Lore",
    "Clil",
    "Ted",
    "Kate",
    "Tuf",
    "Polie",
    "Popo",
    "Zazá",
    "Meg",
    "Lucy",
    "Gregg",
    "Kim",
    "Lulu",
    "Nina",
    "Dedé",
    "Eva",
    "Dara",
    "Hana",
    "Chita",
    "Bilú",
    "Mel",
    "Maki",
    "Nixe",
    "Willy",
    "Pluto",
    "Lady",
    "Kami",
    "Lassie",
    "Misturinha",
    "Floquinho",
    "Bitoca",
    "Tchutchuba",
    "Tambico",
    "Chumbinho",
    "Chokito",
    "Costelinho",
    "Simbad",
    "Paloma",
    "Flofinha",
    "Chiquinha",
    "Merlin",
    "Docinho",
    "Nikita",
    "Nicole",
    "Princesa",
    "Malhadinho",
    "Samuray",
    "Michirica",
    "Travolta",
    "Bolota",
    "Bisroka",
    "Naniko",
    "Chuvisco",
    "Tâmara",
    "Yasmin",
    "Rosinha",
    "Madonna",
    "Florinda",
    "Hoshiko"
]
healthStatus = [ "Saudável", "Saudável", "Hospitalizado", "Hospitalizado", "Hospitalizado", "Hospitalizado", "Hospitalizado", "Hospitalizado", "Morto", "Morto" ]
sex = [ "Masculino", "Feminino", ""]

individuals = []

for i in range(2):
    animal = random.randint(0, allAnimals.count() - 1)
    individual = {
        "animal_id": ObjectId(allAnimals[animal]["_id"]),
        "nickname": nicknames[random.randint(0, allAnimals.count() - 1)],
        "date_arrive": fake.date(),
        "responsible": fake.name(),
        "healthStatus": healthStatus[random.randint(0, len(healthStatus) - 1)],
        "sex": sex[random.randint(0, len(sex) - 1)],
        "media": fake.profile()["website"]
    }
    individuals.append(individual)

database.individuals.insert_many(individuals)