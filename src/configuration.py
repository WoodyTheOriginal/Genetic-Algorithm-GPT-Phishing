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
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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"
]

GENERATION_COLLECTION = get_mongo_db_collection("generation")
CHAMPION_COLLECTION = get_mongo_db_collection("champion")
ITERATIONS = 100
SLEEP_TIME = 5