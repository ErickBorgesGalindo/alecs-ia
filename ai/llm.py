import requests

OLLAMA_URL = "http://localhost:11434/api/chat"

MODEL = "llama3"

def ask_llm(messages):

    payload = {
        "model": MODEL,
        "messages": messages,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    data = response.json()

    return data["message"]["content"]
