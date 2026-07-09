import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()


api_key = st.secrets.get("GOOGLE_API_KEY", None)

if api_key is None:
    api_key = os.getenv("GOOGLE_API_KEY")


genai.configure(api_key=api_key)

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

    try:
        response = model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.2,
                "max_output_tokens": 2048,
                "top_p": 0.95,
                "top_k": 40
            }
        )
        print("Finish Reason:", response.candidates[0].finish_reason)

        return response.text

    except Exception as e:
        return f"❌ Gemini Error:\n\n{e}"
# import os
# from dotenv import load_dotenv
# import google.generativeai as genai

# load_dotenv()

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# model = genai.GenerativeModel("gemini-2.5-flash")

# SYSTEM_PROMPT = """
# You are PetroGPT.

# You are an AI assistant specialized in Petroleum Engineering.

# Your expertise includes:

# - Reservoir Engineering
# - Drilling Engineering
# - Production Engineering
# - Formation Evaluation
# - Petrophysics
# - Rock Mechanics
# - Well Logging
# - Geology
# - Geophysics
# - Oil & Gas Exploration

# If users ask non-petroleum questions,
# answer politely but encourage petroleum-related discussions.

# Always explain concepts clearly and professionally.
# """

# def get_response(question):
#     prompt = SYSTEM_PROMPT + "\n\nUser: " + question

#     response = model.generate_content(prompt)

#     return response.text
