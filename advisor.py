import os
from dotenv import load_dotenv
import google.generativeai as genai
from prompt import create_prompt

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def finance_advisor(income, expenses, savings, debt, goal, risk):

    prompt = create_prompt(
        income,
        expenses,
        savings,
        debt,
        goal,
        risk
    )

    response = model.generate_content(prompt)

    return response.text


