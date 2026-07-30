def create_prompt(income, expenses, savings, debt, goal, risk):

    prompt = f"""
You are a personal finance assistant.

Analyse the user's financial details and provide a short, clear, and easy-to-understand report.

User Financial Details:

Monthly Income: ₹{income}

Monthly Expenses: ₹{expenses}

Current Savings: ₹{savings}

Current Debt: ₹{debt}

Financial Goal:
{goal}

Risk Appetite:
{risk}


Instructions for your response:

- Use simple English.
- Do not write long paragraphs.
- Use short bullet points.
- Keep the total response under 500 words.
- Give practical and actionable suggestions.
- Avoid complex financial terms.
- Use headings for better readability.


Generate the report in this format:


## Financial Health Score
Give a score out of 100 and one short reason.


## Budget Analysis
- Mention if spending is healthy or needs improvement.
- Give 2-3 points only.


## Spending Analysis
- Identify good and bad spending habits.
- Give short suggestions.


## Savings Suggestions
- Provide 3 simple saving tips.


## Investment Suggestions
- Suggest options based on risk level.
- Keep it general and beginner-friendly.


## Debt Management
- Give simple steps to manage debt.


## Monthly Action Plan
Give 4-5 actions the user can follow.


## Conclusion
Give a short summary in 2-3 lines.


Important:
End with this disclaimer:

"This advice is for educational purposes only and is not professional financial advice."
"""

    return prompt
    
    
