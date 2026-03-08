import os
import requests
from dotenv import load_dotenv
from prompts import TEST_GEN_PROMPT

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")


def generate_tests(model_name: str, source_code: str) -> str:
    prompt = TEST_GEN_PROMPT.format(code=source_code)

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": "You generate Python pytest test files only."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }

    response = requests.post(
        f"{BASE_URL}/chat/completions",
        headers=headers,
        json=payload,
        timeout=120
    )
    response.raise_for_status()

    data = response.json()

    content = data["choices"][0]["message"]["content"]

# Remove markdown formatting if present
    if "```" in content:
        parts = content.split("```")
        if len(parts) > 1:
            content = parts[1]
            if content.startswith("python"):
                content = content.replace("python", "", 1)

    return content.strip()