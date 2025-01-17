import requests

response = requests.get("https://icanhazdadjoke.com/api")
# print(response)
# print(response.text)
# print(response.status_code)

file_handler = open("jokes.html", "w")

file_handler.write(response.text)