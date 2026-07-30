# AI Personal Finance Advisor

An AI-powered personal finance advisor that analyzes a user's monthly income, expenses, savings, debt, financial goals, and risk appetite to generate a simple and actionable financial report.

The project uses Google Gemini 2.5 Flash to provide personalized financial insights through an easy-to-use Gradio web interface.

Disclaimer: This project provides educational financial information only and is not professional financial advice.

## Features

* Analyze monthly income
* Analyze monthly expenses
* Evaluate current savings
* Analyze existing debt
* Consider personal financial goals
* Consider investment risk appetite
* AI-powered financial analysis using Google Gemini
* Generate a structured financial report
* Provide practical saving suggestions
* Provide beginner-friendly investment suggestions
* Provide debt management recommendations
* Generate a monthly action plan
* Simple and interactive Gradio interface

## How It Works

The application follows this workflow:

```text
User Financial Details
        |
        v
Gradio Interface
        |
        v
Prompt Generation
        |
        v
Google Gemini 2.5 Flash
        |
        v
Financial Analysis
        |
        v
Structured AI Report
```

The user provides:

* Monthly Income
* Monthly Expenses
* Current Savings
* Current Debt
* Financial Goal
* Risk Appetite

The application sends these details to Gemini with a structured prompt.

Gemini generates a financial report containing:

1. Financial Health Score
2. Budget Analysis
3. Spending Analysis
4. Savings Suggestions
5. Investment Suggestions
6. Debt Management
7. Monthly Action Plan
8. Conclusion

## Technologies Used

| Technology               | Purpose                             |
| ------------------------ | ----------------------------------- |
| Python                   | Core programming language           |
| Google Gemini 2.5 Flash  | AI-powered financial analysis       |
| Google Generative AI SDK | Communication with Gemini           |
| Gradio                   | Web-based user interface            |
| python-dotenv            | Loading environment variables       |
| Git and GitHub           | Version control and project hosting |

## Project Structure

```text
ai-finance-advisor/
|
├── app.py
├── advisor.py
├── prompt.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

### app.py

Creates the Gradio interface and collects the user's financial information.

### advisor.py

Connects the application to Google Gemini and generates the financial analysis.

### prompt.py

Contains the prompt-generation function that structures the user's financial information and defines the format of the AI response.

### .env

Stores the Gemini API key locally.

This file should never be uploaded to GitHub.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-finance-advisor.git
```

Move into the project directory:

```bash
cd ai-finance-advisor
```

### 2. Create a Virtual Environment

For Windows:

```bash
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If requirements.txt has not been created yet:

```bash
pip install gradio google-generativeai python-dotenv
```

## Gemini API Configuration

The project requires a Google Gemini API key.

Create an API key through Google AI Studio.

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_api_key_here
```

The application loads the key using:

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
```

### Security

Never commit your `.env` file to GitHub.

Add the following to `.gitignore`:

```gitignore
.env
venv/
__pycache__/
```

## Running the Application

After activating your virtual environment and configuring your API key, run:

```bash
python app.py
```

Gradio will start the application and provide a local URL.

Open the URL in your browser to use the AI Finance Advisor.

## User Inputs

The application provides the following inputs.

### Monthly Income

Enter your monthly income in Indian Rupees.

Example:

```text
50000
```

### Monthly Expenses

Enter your average monthly expenses.

Example:

```text
30000
```

### Current Savings

Enter your current savings.

Example:

```text
100000
```

### Current Debt

Enter your existing debt.

Example:

```text
50000
```

### Financial Goal

Describe your financial goal.

Example:

```text
Buy a house in 5 years
```

### Risk Appetite

Select one of the following:

* Low
* Medium
* High

## AI Response

The AI generates a report using the following structure:

```text
Financial Health Score

Budget Analysis

Spending Analysis

Savings Suggestions

Investment Suggestions

Debt Management

Monthly Action Plan

Conclusion
```

The generated response is designed to be:

* Simple
* Short
* Practical
* Beginner-friendly
* Action-oriented

## Prompt Engineering

The project uses a custom prompt-generation function.

The user's financial information is dynamically inserted into the prompt:

```python
prompt = create_prompt(
    income,
    expenses,
    savings,
    debt,
    goal,
    risk
)
```

The prompt instructs Gemini to:

* Use simple English
* Avoid complex financial terminology
* Use short bullet points
* Provide actionable suggestions
* Give a financial health score
* Analyze spending and budgeting
* Suggest saving strategies
* Provide general investment suggestions
* Provide debt management strategies
* Create a monthly action plan

This makes the output more consistent and easier for users to understand.

## Example Input

```text
Monthly Income: Rs. 50,000

Monthly Expenses: Rs. 30,000

Current Savings: Rs. 1,00,000

Current Debt: Rs. 20,000

Financial Goal:
Buy a car in 3 years

Risk Appetite:
Medium
```

The AI analyzes these details and generates a personalized financial report.

## Environment Variables

The application uses the following environment variable:

```text
GOOGLE_API_KEY
```

Example:

```env
GOOGLE_API_KEY=your_api_key
```

Do not share your API key publicly.

## Requirements

Example `requirements.txt`:

```text
gradio
google-generativeai
python-dotenv
```

## Future Improvements

### Financial Dashboard

Add graphs and charts for:

* Income
* Expenses
* Savings
* Debt
* Monthly cash flow

### Database Integration

Store user financial information and previous reports using:

* SQLite
* MongoDB
* PostgreSQL
* Firebase

### Expense Tracking

Allow users to categorize expenses such as:

```text
Food
Travel
Shopping
Bills
Entertainment
Education
Healthcare
```

### Monthly Tracking

Allow users to enter financial data every month and compare their progress.

### Financial Progress Graphs

Show how savings, expenses, and debt change over time.

### User Authentication

Add secure login and user accounts.

### Improved AI Financial Analysis

Future versions could calculate:

* Savings rate
* Expense-to-income ratio
* Debt-to-income ratio
* Emergency fund status
* Financial health score

### Financial Report Export

Allow users to download their AI-generated financial report as:

* PDF
* CSV
* Excel

## Disclaimer

This application is an educational project designed to demonstrate the use of Generative AI in personal finance analysis.

The information generated by the AI should not be considered professional financial, investment, tax, or legal advice.

Always consult a qualified financial professional before making important financial decisions.

## Author

Sarthak Bansal

AI and Generative AI Project

## Future Vision

The goal of this project is to evolve from a simple AI financial advisor into a complete AI-powered personal finance management platform that can help users understand their spending, manage savings and debt, track financial goals, and make better-informed financial decisions.
