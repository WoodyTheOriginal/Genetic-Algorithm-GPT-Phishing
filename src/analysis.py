from json import load, dumps
from mongo_queries import insert_document, get_champion, get_last_generation_champion
from configuration import JSON_FILENAME, PREPROMPT, GENERATION_COLLECTION, CHAMPION_COLLECTION, ITERATIONS, SLEEP_TIME
from functions import initialize_and_start_threads

if __name__ == "__main__":
    with open(JSON_FILENAME, "r", encoding="utf-8") as json_file:
        data_list = load(json_file)

    generation_iteration = 1
    champion_prompt = ""
    champion_accuracy = 0

    while generation_iteration < 11:

        generation = {
            'Name': f'Generation {generation_iteration}',
            'Children': {
                 'prompts': [],
                 'results': [],
            },
        }

        print(f'Generation {generation_iteration}')

        last_champion_accuracy_and_false_negatives = [get_last_generation_champion("Accuracy"), get_last_generation_champion("False Negatives")]
        last_champion_prompt = get_last_generation_champion("prompt")

        if generation_iteration == 1:

            children = initialize_and_start_threads(data_list, PREPROMPT, ITERATIONS, SLEEP_TIME)

        elif champion_accuracy_and_false_negatives[0] < last_champion_accuracy_and_false_negatives[0] and champion_accuracy_and_false_negatives[1] <= last_champion_accuracy_and_false_negatives[1]:

            children = initialize_and_start_threads(data_list, last_champion_prompt, ITERATIONS, SLEEP_TIME)

        else:
                
            children = initialize_and_start_threads(data_list, champion_prompt, ITERATIONS, SLEEP_TIME)
        
        # add all children return values to a dict and add to mongodb document
        for index, child in enumerate(children):
            generation['Children']['prompts'].append(children[index][0])
            generation['Children']['results'].append(children[index][1].join())
            print(f'Child {index+1} results: {children[index][1].join()}')
        
        #create a mongodb document in the generation collection named generation{generation_iteration} with all the returns elements
        document_id = insert_document(GENERATION_COLLECTION, generation)

        champion = get_champion(generation)
        print(f'Champion: {champion}')
        champion_prompt = champion[0]
        champion_accuracy_and_false_negatives = [champion[1]["Accuracy"], champion[1]["False Negatives"]]
        champion_mongo_format = {
            "Name": f"Generation {generation_iteration}",
            "prompt": champion_prompt, 
            "Accuracy": champion_accuracy_and_false_negatives[0],
            "False Negatives": champion_accuracy_and_false_negatives[1],
            }
        # add the champion to the champion collection in a new document
        insert_document(CHAMPION_COLLECTION, champion_mongo_format)

        generation_iteration += 1