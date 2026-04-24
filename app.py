import os
from groq import Groq
import re

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
messages = []

def add_user_message(text):
    messages.append({
        "role": "user",
        "content": text
    })

def add_assistant_message(text):
    messages.append({
        "role": "assistant",
        "content": text
    })

def chat():
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )

    reply = response.choices[0].message.content
    add_assistant_message(reply)

    return reply


# Optional: system message (recommended)
messages.append({
    "role": "system",
    "content": "You are a helpful assistant."
})


def format_text(text: str) -> str:
    text = re.sub(r"\*\*(.*?)\*\*", r"\033[1m\1\033[0m", text)
    text = text.replace("•", "-")
    text = re.sub(r"\n\d+\.", lambda m: "\n\n" + m.group(), text)

    return text
print("🚀 Simple Chat (type 'exit' to quit)\n")

while 1:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye 👋")
        break

    add_user_message(user_input)

    try:
        reply = chat()
        print("\nAssistant:\n" + format_text(reply) + "\n")
    except Exception as e:
        print("Error:", e)


annotated-types==0.7.0
anyio==4.13.0
bidict==0.23.1
blinker==1.9.0
brotli==1.2.0
certifi==2026.2.25
charset-normalizer==3.4.7
click==8.3.3
ConfigArgParse==1.7.5
distro==1.9.0
Flask==3.1.3
flask-cors==6.0.2
Flask-Login==0.6.3
gevent==25.9.1
geventhttpclient==2.3.9
greenlet==3.4.0
groq==1.2.0
h11==0.16.0
httpcore==1.0.9
httpx==0.28.1
idna==3.11
iniconfig==2.3.0
itsdangerous==2.2.0
Jinja2==3.1.6
locust==2.43.4
MarkupSafe==3.0.3
msgpack==1.1.2
packaging==26.1
pluggy==1.6.0
psutil==7.2.2
pydantic==2.13.3
pydantic_core==2.46.3
Pygments==2.20.0
pytest==9.0.3
python-engineio==4.13.1
python-socketio==5.16.1
pyzmq==27.1.0
requests==2.33.1
simple-websocket==1.1.0
sniffio==1.3.1
typing-inspection==0.4.2
typing_extensions==4.15.0
urllib3==2.6.3
websocket-client==1.9.0
Werkzeug==3.1.8
wsproto==1.3.2
zope.event==6.1
zope.interface==8.3
(.venv) ➜  groq-test 
