# pip install openai
from openai import OpenAI
client = OpenAI(api_key="YOUR_API_KEY")        # or set OPENAI_API_KEY
response = client.completions.create(
    model="gpt-3.5-turbo-instruct",            # GPT-3 family completion model; change if retired
    prompt="Write a two-line poem about the ocean.",
    max_tokens=60,
    temperature=0.7)
print(response.choices[0].text.strip())
