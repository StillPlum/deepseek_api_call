import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("DS_API_KEY"), base_url="https://api.deepseek.com")


def generate_prompt(user_input: str) -> str:
    prompt = f"Rewrite the following natural-language request as a clear task prompt: '{user_input}'"
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content
