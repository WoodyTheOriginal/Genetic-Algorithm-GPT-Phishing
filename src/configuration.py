from mongo_queries import get_mongo_db_collection

JSON_FILENAME = "phishing_email.json"
PREPROMPT = """
You're a phishing email detecting tool than is designed and built to detect phishing emails. 
Use as much knowloedge as you can to deliver the correct output.
"""
PREPROMPT_SENTENCE_TO_INPUT = """
Your ouput must be in a JSON format with one key 'status' and the value is either 'Safe Email' or 'Phishing Email'.
"""
PREPROMPT_IMPROVE = """
You are a prompt engineer trying to build a prompt that will help GPT model detect phishing emails.
You're given a prompt that is not working well. Improve it.
GPT model will be given only the email body.
Try to expand the prompt but stay on the same scope.
Be as detailed as possible in your prompt.
Don't input a sample email body.
Answer in a JSON format with one key 'prompt' and the value is the prompt you improved.
"""

GENERATION_COLLECTION = get_mongo_db_collection("generation_2")
CHAMPION_COLLECTION = get_mongo_db_collection("champion_2")
ITERATIONS = 200
SLEEP_TIME = 5