import requests

def get_response_from_openai(prompt):
    api_key = 'YOUR_OPENAI_API_KEY'
    url = 'https://api.openai.com/v1/chat/completions'

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }

    data = {
        'model': 'gpt-3.5-turbo',  # or 'gpt-4' if you have access
        'messages': [{'role': 'user', 'content': prompt}],
    }

    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()

    if response.status_code == 200:
        return response_data['choices'][0]['message']['content']
    else:
        return f"Error: {response_data.get('error', {}).get('message', 'Unknown error')}"

# Example usage
if __name__ == "__main__":
    question = input("Ask me anything: ")
    answer = get_response_from_openai(question)
    print("Response:", answer)
