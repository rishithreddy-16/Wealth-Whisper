import streamlit as st
import time
import pandas as pd
from engine import check_stock_price, get_impacted_clients, load_data
from ai_agent import generate_email

def send_email_action(name, email):
    """Callback function to simulate sending email."""
    st.toast(f"🚀 Email sent to {name} ({email})!", icon="✅")
    time.sleep(1) # Small delay so user sees it


# --- PAGE CONFIG ---
st.set_page_config(page_title="Wealth-Whisper", page_icon="💸", layout="wide")

# --- CUSTOM CSS (To make it look like a Bank Portal) ---
st.markdown("""
<style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #4CAF50;
    }
    .alert-card {
        background-color: #ffebee;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #ff4444;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.title("💸 Wealth-Whisper: Client Guardian")
st.markdown("### Intelligent Portfolio Monitoring System")
st.divider()

# --- SIDEBAR (Controls) ---
# --- SIDEBAR (Controls) ---
with st.sidebar:
    st.header("🔍 Market Scanner")
    ticker_input = st.text_input("Enter Stock Ticker:", value="TSLA").upper()
    
    # Initialize session state if not exists
    if 'scan_triggered' not in st.session_state:
        st.session_state['scan_triggered'] = False

    # The Button updates the state
    if st.button("🚀 Scan Market", type="primary"):
        st.session_state['scan_triggered'] = True


# --- MAIN LOGIC ---
if st.session_state.get('scan_triggered'):
    
    # 1. Get Real-Time Data
    with st.spinner(f"📡 Connecting to Market Data for {ticker_input}..."):
        time.sleep(1) # Dramatic pause for effect
        market_data = check_stock_price(ticker_input)
    
    if market_data:
        # Display Market Data
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Current Price", f"${market_data['price']}")
        with col2:
            st.metric("Daily Change", f"{market_data['change']}%", delta=market_data['change'])
        with col3:
            status = "CRASH DETECTED" if market_data['change'] < -5 else "Normal Volatility"
            if market_data['change'] < -5:
                st.error(status)
            else:
                st.success(status)

        
        st.divider()
        
        # 2. Find Clients
        clients_df = load_data()
        impacted_clients = get_impacted_clients(clients_df, ticker_input)
        
        if not impacted_clients.empty:
            st.subheader(f"🎯 Impacted Clients ({len(impacted_clients)})")
            
            # Show Table
            st.dataframe(impacted_clients[['Name', 'Email', 'Risk_Tolerance']], width=1000)
            
            st.write("---")
            st.subheader("🤖 AI Action Center")
            
            # 3. AI Drafting Station
            for index, row in impacted_clients.iterrows():
                with st.expander(f"✉️ Draft Email for: {row['Name']} ({row['Risk_Tolerance']} Risk)"):
                    
                    # Call the AI Agent
                    with st.spinner("Writing email..."):
                        email_draft = generate_email(
                            row['Name'], 
                            ticker_input, 
                            market_data, 
                            row['Risk_Tolerance']
                        )
                    
                    st.text_area("AI Draft:", value=email_draft, height=200, key=f"email_{index}")
                    
                    c1, c2 = st.columns([1, 4])
                    
                    # The Button with a Callback
                    st.button(
                        "✅ Approve & Send", 
                        key=f"btn_{index}",
                        on_click=send_email_action,
                        args=(row['Name'], row['Email'])
                    )
                    
                    with c2:
                        st.caption("Action will log to CRM.")


            
    else:
        st.error("Ticker not found. Please check the symbol.")

# --- FOOTER ---
else:
    st.info("👈 Enter a Ticker in the sidebar and hit 'Scan Market' to start.")
