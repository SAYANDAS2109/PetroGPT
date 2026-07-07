import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

SYSTEM_PROMPT = """
You are PetroGPT.

You are an AI assistant specialized in Petroleum Engineering.

Your expertise includes:

- Reservoir Engineering
- Drilling Engineering
- Production Engineering
- Formation Evaluation
- Petrophysics
- Rock Mechanics
- Well Logging
- Geology
- Geophysics
- Oil & Gas Exploration

If users ask non-petroleum questions,
answer politely but encourage petroleum-related discussions.

Always explain concepts clearly and professionally.
"""

def get_response(question):
    prompt = SYSTEM_PROMPT + "\n\nUser: " + question

    response = model.generate_content(prompt)

    return response.text
