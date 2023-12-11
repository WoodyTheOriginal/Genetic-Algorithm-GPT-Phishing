from json import load, dumps
from mongo_queries import get_max_false_negatives_in_champions, get_mongo_db_collection, insert_document, get_champion, get_all_previous_generations_champion, get_champion_from_champions
from configuration import JSON_FILENAME, PREPROMPT, GENERATION_COLLECTION, CHAMPION_COLLECTION, ITERATIONS, SLEEP_TIME
from functions import initialize_and_start_threads, calculate_score

if __name__ == "__main__":
    with open(JSON_FILENAME, "r", encoding="utf-8") as json_file:
        data_list = load(json_file)

    generation_iteration = 1
    champion_prompt = ""
    champion_accuracy = 0
    champion_collection = get_mongo_db_collection(CHAMPION_COLLECTION)
    generation_collection = get_mongo_db_collection(GENERATION_COLLECTION)

    while generation_iteration < 11:

        generation = {
            'Name': f'Generation {generation_iteration}',
            'Children': {
                 'prompts': [],
                 'results': [],
            },
        }

        print(f'Generation {generation_iteration}')

        #Value to calculate the score of champions in order to compare them
        Y_max = get_max_false_negatives_in_champions()

        all_last_champions = get_all_previous_generations_champion(CHAMPION_COLLECTION)
        if all_last_champions != []:
            champion_from_all_last_champions = get_champion_from_champions(all_last_champions)

            champion_from_all_last_champions_prompt = champion_from_all_last_champions["prompt"]
            champion_from_all_last_champions_accuracy_and_false_negatives = [champion_from_all_last_champions["Accuracy"], champion_from_all_last_champions["False Negatives"]]
            champion_from_all_last_champions_score = calculate_score(champion_from_all_last_champions_accuracy_and_false_negatives[0], champion_from_all_last_champions_accuracy_and_false_negatives[1], Y_max)

        if generation_iteration == 1:

            children = initialize_and_start_threads(data_list, PREPROMPT, ITERATIONS, SLEEP_TIME)

        elif champion_from_all_last_champions_score > champion_score:

            children = initialize_and_start_threads(data_list, champion_from_all_last_champions_prompt, ITERATIONS, SLEEP_TIME)

        else:
                
            children = initialize_and_start_threads(data_list, champion_prompt, ITERATIONS, SLEEP_TIME)
        
        # add all children return values to a dict and add to mongodb document
        for index, child in enumerate(children):
            generation['Children']['prompts'].append(children[index][0])
            generation['Children']['results'].append(children[index][1].join())
            print(f'Child {index+1} results: {children[index][1].join()}')
        
        #create a mongodb document in the generation collection named generation{generation_iteration} with all the returns elements
        document_id = insert_document(generation_collection, generation)

        champion = get_champion(generation)
        champion_prompt = champion[0]
        print(f'Champion prompt is : {champion_prompt}')
        champion_accuracy_and_false_negatives = [champion[1]["Accuracy"], champion[1]["False Negatives"]]
        champion_score = calculate_score(champion_accuracy_and_false_negatives[0], champion_accuracy_and_false_negatives[1], Y_max)
        champion_mongo_format = {
            "Name": f"Generation {generation_iteration}",
            "prompt": champion_prompt, 
            "Accuracy": champion_accuracy_and_false_negatives[0],
            "False Negatives": champion_accuracy_and_false_negatives[1],
            }
        # add the champion to the champion collection in a new document
        insert_document(champion_collection, champion_mongo_format)

        generation_iteration += 1