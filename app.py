import gradio as gr
from advisor import finance_advisor

demo = gr.Interface(
    fn=finance_advisor,

    inputs=[

        gr.Number(label="Monthly Income (₹)"),

        gr.Number(label="Monthly Expenses (₹)"),

        gr.Number(label="Current Savings (₹)"),

        gr.Number(label="Current Debt (₹)"),

        gr.Textbox(
            label="Financial Goal",
            placeholder="Example: Buy a house in 5 years"
        ),

        gr.Dropdown(
            choices=[
                "Low",
                "Medium",
                "High"
            ],
            label="Risk Appetite"
        )

    ],

    outputs=gr.Markdown(),

    title="AI Personal Finance Advisor",

    description="""
Enter your financial details and receive personalised AI-powered financial advice.
""",

    theme=gr.themes.Soft()

)

demo.launch()

