import os
import sys
from dotenv import load_dotenv # type: ignore
from openai import OpenAI # type: ignore

# Load environment variables from .env file
load_dotenv()

# Create an OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Get the prompt from 'python ai.py my_prompt'
# get all the args as a string
prompt = " ".join(sys.argv[1:])

# Create a completion
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(completion.choices[0].message.content)