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
