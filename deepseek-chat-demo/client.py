import os
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

DS_API_URL = os.getenv("DS_API_URL", "https://api.deepseek.com/v1/chat/completions")
DS_API_KEY = os.getenv("DS_API_KEY", "")
DS_MODEL = os.getenv("DS_MODEL", "deepseek-chat")


def _headers() -> dict:
    if not DS_API_KEY:
        raise RuntimeError("Missing DS_API_KEY in environment or .env")
    return {
        "Authorization": f"Bearer {DS_API_KEY}",
        "Content-Type": "application/json",
    }


def send_message(user_id: str, messages: list) -> dict:
    payload = {
        "model": DS_MODEL,
        "messages": messages,
        # "user": user_id,  # optional for some providers
    }
    r = requests.post(DS_API_URL, headers=_headers(), json=payload, timeout=60)
    r.raise_for_status()
    return r.json()
