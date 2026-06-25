import os
import time
from groq import Groq, RateLimitError
from dotenv import load_dotenv
from log_config import logger

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=API_KEY)


def groq_with_retry(messages, model="llama-3.1-8b-instant", retries=5):
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages
            )
            return response
        except RateLimitError as e:
            wait = 2 ** attempt  # 1, 2, 4, 8, 16 seconds
            logger.error(
                f"Rate limited. Retrying in {wait}s... (attempt {attempt + 1})")
            time.sleep(wait)

    raise Exception("Groq rate limit exceeded after max retries")
