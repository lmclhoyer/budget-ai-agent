import os
import openai

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_financial_data(text):
    prompt = f"""Here is some financial data extracted from a user's bank and credit card statements:

{text}

Your job is to analyze this data and provide suggestions to increase their savings or investment rate.
Include specific recommendations such as cutting back on subscriptions or reducing dining expenses."""
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a smart finance assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content
