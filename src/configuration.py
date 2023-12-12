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
PREPROMPT_P0 = """
You're a phishing email detecting tool than is designed and built to detect phishing emails. 
Use as much knowloedge as you can to deliver the correct output.
"""
PREPROMPT_SEM = """
Additionally, consider the email's formatting, such as generic salutations, misspellings, inconsistent branding, requests for sensitive information, suspicious links, mismatched sender information, unexpected attachments, as potential indicators of phishing.
Utilize contextual information to assess the legitimacy of any requests within the email.
"""
PREPROMPT_PSY = """
Analyze the psychological apects such as a sense of urgency, inducing fear by threatening, and enticement with desire.
Be careful for deceptive tactics designed to elicit sensitive information.
Pay close attention to language cues that may indicate manipulation or coercion of the recipient.
"""
PREPROMPT_CONTXT = """
You are a sophisticated email security system with advanced machine learning algorithms designed to detect and prevent phishing emails.
Your objective is to carefully examine the content of the email and identify any characteristics commonly associated with phishing attempts.
Your role in accurately detecting these elements is crucial for safeguarding users against falling victim to phishing schemes.
"""

CHAMPION_COLLECTIONS = ["champion", "champion_2", "champion_3"]

GENERATION_COLLECTION = "generation_3"
CHAMPION_COLLECTION = "champion_3"
ITERATIONS = 200
SLEEP_TIME = 5
LAMBDA_ = 0.4
TEST_FILES_LIST = [
    "datasets/sampled_emails_1.json",
    "datasets/sampled_emails_2.json",
    "datasets/sampled_emails_3.json",
    #"datasets/sampled_emails_4.json",
    #"datasets/sampled_emails_5.json",
]