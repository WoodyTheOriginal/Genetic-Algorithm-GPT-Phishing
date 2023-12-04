from pymongo import MongoClient

def get_mongo_db_collection(collection_name: str):
    # Connect to the MongoDB server (default is localhost on port 27017)
    client = MongoClient('localhost', 27017)

    # Access the database
    db = client['master_ki']

    # Access collections
    return db[collection_name]

def insert_document(collection, document):
    # Insert sample documents into each collection
    return collection.insert_one(document).inserted_id

def print_collection(collection):
    # Print all documents in the collection and their content
    for document in collection.find():
        print(document)


def get_champion(generation_collection):

    accuracy_and_false_negatives = []

    for index, key in enumerate(generation_collection['Children']['results']):
        accuracy_and_false_negatives.append([generation_collection['Children']['results'][index]['Accuracy'], generation_collection['Children']['results'][index]['False Negatives']])

    # Initialize variables for the highest X and lowest Y
    highest_X = float('-inf')
    lowest_Y = float('inf')
    lowest_tuple = None

    # Iterate through each sublist
    for sublist in accuracy_and_false_negatives:
        X, Y = sublist
        if X > highest_X or (X == highest_X and Y < lowest_Y):
            highest_X = X
            lowest_Y = Y
            lowest_tuple = sublist

    return [generation_collection['Children']['prompts'][accuracy_and_false_negatives.index(lowest_tuple)], generation_collection['Children']['results'][accuracy_and_false_negatives.index(lowest_tuple)]]

def get_last_generation_champion(choice: str):
    champion_collection = get_mongo_db_collection("champion_2")
    nb_champions = champion_collection.count_documents({})
    match nb_champions:
        case 0:
            return 0
        case 1:
            return next(champion_collection.find().sort({"_id": -1}).limit(1))[choice]
        case _:
            return next(champion_collection.find().sort({"_id": -1}).skip(1).limit(1))[choice]