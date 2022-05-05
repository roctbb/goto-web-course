import requests

answer = requests.post("http://127.0.0.1:5000/api/messages", data={
    "author": "lupa",
    "text": "pupa"
})

print(answer.text)