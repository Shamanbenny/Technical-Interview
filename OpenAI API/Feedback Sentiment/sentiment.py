from enum import Enum
from pydantic import BaseModel
from dotenv import load_dotenv
import openai
from openai import OpenAI
import os

"""
import kagglehub

# Download latest version
path = kagglehub.dataset_download("andrewmvd/trip-advisor-hotel-reviews")

print("Path to dataset files:", path)"
"""

load_dotenv()
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

class Sentiment(str, Enum):
    positive = "Positive"
    negative = "Negative"
    neutral = "Neutral"

class Rating(int, Enum):
    veryPoor = 1
    poor = 2
    average = 3
    good = 4
    excellent = 5

class Query(BaseModel):
    sentiment: Sentiment
    rating: Rating

while True:
    user_input = input("You: ")
    if user_input == "exit":
        break
    response = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a sentiment classifier. Please classify the sentiment of the following text, for possible ratings (1 to 5; such that 1 is very poor), as well as the sentiment itself (positive, negative or neutral)."},
            {"role": "user", "content": user_input},
        ],
        tools=[openai.pydantic_function_tool(Query)],
    )
    print("Response:", response.choices[0].message.tool_calls[0].function.parsed_arguments)