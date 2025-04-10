import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
import os

# Load your OpenAI API key from your environment variables.

def analyze_financial_data(text):
    prompt = f"""Here is some financial data extracted from a user's bank and credit card statements:

{text}

Your job is to analyze this data and provide suggestions to increase their savings or investment rate.
Include specific recommendations such as cutting back on subscriptions or reducing dining expenses."""

    response = client.chat.completions.create(model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a smart finance assistant."},
        {"role": "user", "content": prompt}
    ])

    return response.choices[0].message.content