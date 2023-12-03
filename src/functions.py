from children_class import Children
from secrets_things import API_KEYS
from openai_queries import experiment, improve_preprompt

def initialize_and_start_threads(data_list, prompt, iterations, sleep_time):
    children = []
    improved_preprompts = []
    for index, key in enumerate(API_KEYS):
        # create a prompt for each child
        improved_preprompts.append(improve_preprompt(key, prompt))
        children.append([improved_preprompts[index], Children(target=experiment, args=(data_list, key, improved_preprompts[index], iterations, sleep_time))])
        children[index][1].start()
    return children