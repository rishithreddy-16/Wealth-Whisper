import os
from groq import Groq
import streamlit as st

# -----------------------------------------
# 🔑 CONFIGURATION
# Paste your Groq API Key inside the quotes
def get_api_key():
    try:
        return st.secrets["GROQ_API_KEY"]  # From Streamlit secrets
    except:
        return os.environ.get("GROQ_API_KEY")  # From environment
# -----------------------------------------

def generate_email(client_name, ticker, stock_data, risk_tolerance):
    """
    Drafts an email using Llama 3 (via Groq).
    """
    price = stock_data['price']
    change = stock_data['change']
    direction = "UP" if change > 0 else "DOWN"
    
    # 1. The Prompt (The Strategy)
    system_instruction = """
    You are a Senior Wealth Manager at Barclays.
    Write a short, professional email to a client about their stock performance.
    - Tone: Reassuring (if down) or Celebratory (if up).
    - Length: Under 100 words.
    - Structure: Salutation -> Context -> Advice -> Sign-off.
    - No subject line in the body.
    """
    
    user_prompt = f"""
    Client: {client_name}
    Stock: {ticker} (Price: ${price}, Change: {change}%).
    Risk Profile: {risk_tolerance}.
    
    If Risk is 'Low' and stock is down, be very empathetic.
    If Risk is 'High', keep it analytical.
    """

    # 2. The Call (Try Real AI first)
    try:
        client = Groq(api_key=GROQ_API_KEY)
        
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # The NEW Fast & Free model
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            max_tokens=250
        )
        return completion.choices[0].message.content

    except Exception as e:
        print(f"⚠️ API Error: {e}")
        return fallback_template(client_name, ticker, change, direction)

def fallback_template(name, ticker, change, direction):
    """Backup in case API fails (keeps the app running)."""
    return f"""
    Dear {name},
    
    I'm writing to update you on {ticker}. It moved {direction} by {change}% today.
    Given market conditions, we are monitoring this closely. Let's discuss if you have concerns.
    
    Best,
    Your Advisor (Offline Mode)
    """

# --- TEST BLOCK ---
if __name__ == "__main__":
    print("Testing AI Agent...")
    # Test with fake data
    result = generate_email("Rishith", "NVDA", {"price": 100, "change": 5.0}, "High")
    print("\n--- RESULT ---")
    print(result)
