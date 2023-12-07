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
You are given a prompt.
You will output a new prompt that stays on the same scope of detecting phishing emails.
GPT model will be given only the email body.
Be as detailed as possible in your prompt.
Be very creative and use as much knowledge as you can.
Don't input a sample email body.
Answer in a JSON format with one key 'prompt' and the value is the new prompt you just created.
"""

GENERATION_COLLECTION = "generation_3"
CHAMPION_COLLECTION = "champion_3"
ITERATIONS = 1
SLEEP_TIME = 5
LAMBDA_ = 0.4