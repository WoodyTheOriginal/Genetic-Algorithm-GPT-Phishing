from pymongo import MongoClient

# local imports
from configuration import CHAMPION_COLLECTION


def get_mongo_db_collection(collection_name: str):
    client = MongoClient("localhost", 27017)
    db = client["master_ki"]
    return db[collection_name]


def insert_document(collection, document):
    return collection.insert_one(document).inserted_id


def print_collection(collection):
    for document in collection.find():
        print(document)


def get_champion(generation_collection):
    accuracy_and_false_negatives = []

    for index, key in enumerate(generation_collection["Children"]["results"]):
        accuracy_and_false_negatives.append(
            [
                generation_collection["Children"]["results"][index]["Accuracy"],
                generation_collection["Children"]["results"][index]["False Negatives"],
            ]
        )

    # Initialize variables for the highest X and lowest Y
    highest_X = float("-inf")
    lowest_Y = float("inf")
    lowest_tuple = None

    # Iterate through each sublist
    for sublist in accuracy_and_false_negatives:
        X, Y = sublist
        if X > highest_X or (X == highest_X and Y < lowest_Y):
            highest_X = X
            lowest_Y = Y
            lowest_tuple = sublist

    return [
        generation_collection["Children"]["prompts"][
            accuracy_and_false_negatives.index(lowest_tuple)
        ],
        generation_collection["Children"]["results"][
            accuracy_and_false_negatives.index(lowest_tuple)
        ],
    ]


def get_last_generation_champion(choice: str):
    champion_collection = get_mongo_db_collection(CHAMPION_COLLECTION)
    nb_champions = champion_collection.count_documents({})
    match nb_champions:
        case 0:
            return 0
        case 1:
            return next(champion_collection.find().sort({"_id": -1}).limit(1))[choice]
        case _:
            return next(champion_collection.find().sort({"_id": -1}).skip(1).limit(1))[
                choice
            ]


def get_all_previous_generations_champion(collection: str):
    champion_collection = get_mongo_db_collection(collection).find()
    champions = []
    for champion in champion_collection:
        champions.append(champion)
    return champions


def get_champion_from_champions(champions: list):
    accuracy_and_false_negatives = []

    if len(champions) == 0:
        return 0

    for index, key in enumerate(champions):
        accuracy_and_false_negatives.append(
            [champions[index]["Accuracy"], champions[index]["False Negatives"]]
        )

    # Initialize variables for the highest X and lowest Y
    highest_X = float("-inf")
    lowest_Y = float("inf")
    lowest_tuple = None

    # Iterate through each sublist
    for sublist in accuracy_and_false_negatives:
        X, Y = sublist
        if X > highest_X or (X == highest_X and Y < lowest_Y):
            highest_X = X
            lowest_Y = Y
            lowest_tuple = sublist

    return champions[accuracy_and_false_negatives.index(lowest_tuple)]


def get_max_false_negatives_in_champions():
    client = MongoClient("localhost", 27017)
    db = client["master_ki"]
    collection = db[CHAMPION_COLLECTION]
    result = collection.find().sort("False Negatives", -1).limit(1)
    for document in result:
        return document["False Negatives"]
