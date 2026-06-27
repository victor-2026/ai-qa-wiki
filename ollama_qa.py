import requests
import os
import sys

OLLAMA_HOST = os.getenv('OLLAMA_HOST', 'http://localhost:11434')

def ask_ollama(question, model='qwen2.5:3b'):
    res = requests.post(
        f'{OLLAMA_HOST}/api/generate',
        json={'model': model, 'prompt': question, 'stream': False},
        timeout=30
    )
    return res.json().get('response', '')

if __name__ == '__main__':
    q = sys.argv[1] if len(sys.argv) > 1 else "Привет"
    print(ask_ollama(q))
