import openai
import os
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def parse_task_from_input(user_input):
    prompt = f"""
You are a productivity assistant. Extract task details from this sentence: "{user_input}"
Respond in JSON format with keys: "task", "date", and "time". If date or time is not specified, return null.
Example Output:
{{"task": "Call John", "date": "2025-04-01", "time": "14:00"}}
Now, process this: "{user_input}"
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-4"
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    result_text = response.choices[0].message.content.strip()

    try:
        return eval(result_text)
    except Exception as e:
        print("Failed to parse:", e)
        return None
