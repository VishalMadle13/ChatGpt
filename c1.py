import requests

# Set up the API endpoint and parameters
endpoint = "https://api.openai.com/v1/engines/davinci-codex/completions"
headers = {"Content-Type": "application/json", "Authorization": "Bearer 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"}
data = {
    "prompt": "Write a Python function that calculates the sum of two numbers.",
    "max_tokens": 50,
    "temperature": 0.7,
    "n": 1,
    "stop": "\n\n"
}

# Make the API request
response = requests.post(endpoint, headers=headers, json=data)

# Check the status code to make sure the request was successful
if response.status_code == 200:
    # Extract the response data and print it
    result = response.json()["choices"][0]["text"]
    print(result)
else:
    print("Error: " + response.text)
