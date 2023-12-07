JSON_FILENAME = "..\src\phishing_email.json"
GENERATION_COLLECTION = "generation_3"
CHAMPION_COLLECTION = "champion_3"
ITERATIONS = 1
SLEEP_TIME = 5
LAMBDA_ = 0.4

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

PREPROMPT = """
youre a phishing email detector and you output a JSON string 
where they key is 'status' and the value can be either 'Safe Email' or 'Phishing Email'\n
1. Sender Information: Check for irregularities, misspellings, or variations in the sender's email address. Also, verify if the sender's address matches the displayed name.
2. Content Analysis: Identify urgent language, generic greetings, or lack of personalization. Look for elements that create a sense of urgency.
3. URL Analysis: Examine hyperlinks for suspicious domains, misspellings, or non-standard characters. Ensure that the displayed hyperlink matches the actual destination.
4. Attachments and Embedded Links: Be cautious of unexpected attachments or links that prompt the user to download files. Check for mismatched file extensions.
5. Grammar and Spelling: Analyze the overall quality of grammar and spelling. Look for inconsistencies in language, style, or tone within the email body.
6. Contextual Information: Verify the legitimacy of embedded logos or branding. Cross-check information provided in the email with known facts from official channels.
7. Social Engineering Tactics: Identify attempts to manipulate emotions, create urgency, or exploit trust. Recognize common social engineering techniques.

now you have the following email body and you have to output the right response :\n
"""

PREPROMPT_CONTEXTUALIZATION = """
You’re given a JSON Object which contains an email body and a status about wether this
is a phishing email or not. You now have to explain why this status is like that.

Please structure your response in the following JSON format:
{
    "hasUnusualSyntax": [true/false],
    "mentionsSeniorRelatives": [true/false],
    "unusualVocativeUsage": [true/false],
    "unusualContextualUsage": [true/false],
    "languageComplexity": "[Low/Moderate/High]",
    "senderReputation": "[Known/Unknown]",
    "description": <a few sentences to explain the verdict according to the metrics above>
}
so here is the object :
"""
