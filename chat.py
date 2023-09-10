import requests
from credentials import config

# Replace [yourApiKey] with your actual API key
api_key = config['deepl-api']['key']

# API endpoint for ChatGPT
api_endpoint = "https://api.openai.com/v1/chat/completions"

# Your message to ChatGPT
user_message = "Translate the following English text to French: 'Hello, world!'"

# Make a POST request to the ChatGPT API
response = requests.post(api_endpoint, json={"model": "gpt-3.5-turbo", "messages": [{"role": "system", "content": "You are a helpful assistant that translates English to French."}, {"role": "user", "content": user_message}]}, headers={"Authorization": f"Bearer {api_key}"})

# Check if the request was successful
if response.status_code == 200:
    chat_response = response.json()
    # Extract the assistant's reply
    assistant_reply = chat_response["choices"][0]["message"]["content"]
    print("Assistant:", assistant_reply)
else:
    print("Error:", response.status_code, response.text)