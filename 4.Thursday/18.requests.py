import requests
from pprint import pprint
import json

header_dict = {
    "Accept" : "application/json"
}

response = requests.get("https://icanhazdadjoke.com",headers=header_dict)
print(response.status_code)
print(type(response.text))

json_response = json.loads(response.text)
print(type(json_response))
pprint(json_response)


# file_handler = open("jokes.html", "w")

# file_handler.write(response.text)