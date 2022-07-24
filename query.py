import requests

# Declaring our endpoint and payload
url = "http://4f18-34-147-15-210.ngrok.io/similarity_score"
data = {"sentence1": "today is a great day", "sentence2": "today is a good day"}

# Defining our query function
def query(url, payload):
    return requests.post(url, json=payload)

# Sending a GET request and obtaining the results
response = query(url, data)

# Inspecting the response
print(response.json())

