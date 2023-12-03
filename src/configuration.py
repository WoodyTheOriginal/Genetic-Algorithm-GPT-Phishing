from mongo_queries import get_mongo_db_collection

JSON_FILENAME = "phishing_email.json"
PREPROMPT = """
You're a phishing email detecting tool than is designed and built to detect phishing emails. 
Use as much knowloedge as you can to deliver the correct output.
"""
PREPROMPT_SENTENCE_TO_INPUT = """
You are a phishing email detector trained to output a JSON string where the key is "status" and the value can be either "Safe Email" or "Phishing Email". Now, analyze the following email body and output the appropriate response.\n
Don't input a sample email body.
"""
PREPROMPT_IMPROVE = """
You are a prompt engineer trying to build a prompt that will help GPT model to detect phishing emails.
You're given a prompt that is not working well. Improve it.
Be as detailed as possible in your prompt.
Answer in a JSON format with one key 'prompt' and the value is the prompt you improved.
"""
API_KEYS = [
    "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",
    "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",
    "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"
]

GENERATION_COLLECTION = get_mongo_db_collection("generation")
CHAMPION_COLLECTION = get_mongo_db_collection("champion")
ITERATIONS = 200
SLEEP_TIME = 5