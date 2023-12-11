from openai import OpenAI, BadRequestError
from json import loads
from time import sleep
from configuration import PREPROMPT_IMPROVE, PREPROMPT_SENTENCE_TO_INPUT

def get_gpt_opinion(api_key: str, preprompt: str, email_body: str) -> dict:
    client = OpenAI(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "system",
                    "content": preprompt,
                },
                {"role": "user", "content": email_body.replace("'", "")},
            ],
        )

        return loads(response.choices[0].message.content)["status"]
    except ConnectionError as e:
        print(e)
        print(f"Sleeping for 10seconds before retry")
        sleep(10)
        get_gpt_opinion(email_body=email_body)
    except BadRequestError as e:
        print(e)


def experiment(data_list: str, api_key: str, preprompt: str, iterations: int, sleep_time: int = 5) -> dict:
    total = iterations

    true_positives = 0
    true_negatives = 0
    false_positives = 0
    false_negatives = 0

    for i in range(iterations):
        print(f"iteration {i+1}")

        email_body = data_list[i]["content"]
        response = get_gpt_opinion(api_key, preprompt, email_body)

        # a true positive is a Phishing Email

        if response is not None:
            match response:
                case "Safe Email" as safe:
                    if get_email_status(data_list=data_list, email_body=email_body) == safe:
                        true_negatives += 1
                    else:
                        false_negatives += 1
                case "Phishing Email" as unsafe:
                    if get_email_status(data_list=data_list, email_body=email_body) == unsafe:
                        true_positives += 1
                    else:
                        false_positives += 1
        else:
            total -= 1

        sleep(sleep_time)

    return {
        "Accuracy": (true_positives + true_negatives) / total,
        "Error": 1 - (true_positives + true_negatives) / total,
        "True Positives": true_positives,
        "True Negatives": true_negatives,
        "False Positives": false_positives,
        "False Negatives": false_negatives,
    }
            
def improve_preprompt(api_key: str, prompt: str):
    client = OpenAI(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "system",
                    "content": PREPROMPT_IMPROVE,
                },
                {"role": "user", "content": prompt},
            ],
        )
        
        return (f'{loads(response.choices[0].message.content)["prompt"]} {PREPROMPT_SENTENCE_TO_INPUT}')
    
    except ConnectionError as e:
        print(e)
        print(f"Sleeping for 10seconds before retry")
        sleep(10)
        improve_preprompt(api_key=api_key, prompt=prompt)
    except BadRequestError as e:
        print(e)

def get_email_status(data_list: str, email_body: str):
    return next(
        (item["status"] for item in data_list if item["content"] == email_body), None
    )