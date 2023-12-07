from openai import OpenAI
from json import loads

# local imports
from configuration import PREPROMPT_CONTEXTUALIZATION
from secret_stuff import API_KEYS

OPENAI_API_KEY = API_KEYS[0]


def get_context(item: dict) -> dict:
    client = OpenAI(api_key=OPENAI_API_KEY)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": PREPROMPT,
            },
            {"role": "user", "content": str(item)},
        ],
    )

    return loads(response.choices[0].message.content)
