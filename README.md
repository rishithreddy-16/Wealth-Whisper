# Wealth-Whisper

AI-powered portfolio monitoring and client communication assistant for wealth managers, built with Streamlit.

## Live App

👉 https://wealth-whisper-mbkr5i3bdjwkhnauzseb7f.streamlit.app

## What It Does

- Monitors a stock ticker in real time
- Detects which clients hold that stock
- Generates risk-aware email drafts using LLMs
- Keeps the advisor in control with a review + approve step

This turns a stressful “market just moved, I have 50+ clients in this name” moment into a guided workflow.

## Key Features

- **Market Scanner:** Real-time price and daily change via yFinance  
- **Client Impact Engine:** Filters a portfolio CSV to find affected clients  
- **AI Email Agent:** Groq-powered drafts tailored to each client’s risk profile  
- **Advisor Console:** Streamlit UI with per-client expander, editable draft, and “Approve & Send” action

## Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **Data:** Pandas, CSV portfolios  
- **Market Data:** yFinance  
- **LLM:** Groq API (Llama 3)  
- **Deploy:** Streamlit Community Cloud

## Run Locally

```bash
git clone https://github.com/rishithreddy-16/Wealth-Whisper.git
cd Wealth-Whisper
pip install -r requirements.txt

# Set your Groq key (or use a .env)
export GROQ_API_KEY=your_key_here

streamlit run app.py
```

## Project Structure

```text
app.py                # Streamlit UI
engine.py             # Data load + stock + client matching
ai_agent.py           # Groq LLM email generation
client_portfolios.csv # Sample portfolio data
requirements.txt
```

## Notes

- Sample data only; no real client information
- Email “send” is simulated for now (demo-safe)
- All AI drafts are meant to be reviewed by a human advisor

---

Built as a hands-on finance + AI project by **Rishith Reddy Nomula** (M.S. Data Science).  
If you’d like a quick walkthrough of the design or code, I’m happy to walk you through it.
📧 [rishithreddy1652@gmail.com](mailto:rishithreddy1652@gmail.com)  
💼 [LinkedIn](https://linkedin.com/in/rishithreddy-16)
