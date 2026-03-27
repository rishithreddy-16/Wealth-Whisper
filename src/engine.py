import pandas as pd
import yfinance as yf

# 1. Load the Data
def load_data():
    """Loads the client CSV into a Pandas DataFrame."""
    # Ensure the path is correct based on where you run the script
    # If running from root: "data/client_portfolios.csv"
    try:
        df = pd.read_csv("client_portfolios.csv")
        return df
    except FileNotFoundError:
        return pd.read_csv("../data/client_portfolios.csv") # Backup for testing inside src

# 2. Check the Market
def check_stock_price(ticker):
    """
    Returns the current price and % change of a stock.
    """
    try:
        stock = yf.Ticker(ticker)
        # fast_info is faster than history() for current price
        current_price = stock.fast_info['last_price']
        prev_close = stock.fast_info['previous_close']
        
        change_percent = ((current_price - prev_close) / prev_close) * 100
        
        return {
            "ticker": ticker,
            "price": round(current_price, 2),
            "change": round(change_percent, 2)
        }
    except Exception as e:
        print(f"Error fetching {ticker}: {e}")
        return None

# 3. The Matchmaker (Logic)
def get_impacted_clients(df, ticker):
    """
    Filters the DataFrame to find clients who own the specific ticker.
    """
    # We use string contains to find the ticker in the "Holdings" column
    # case=False makes it case-insensitive (tsla = TSLA)
    impacted_df = df[df['Holdings'].str.contains(ticker, case=False, na=False)]
    return impacted_df

# --- TESTING BLOCK (Runs only if you run this file directly) ---
if __name__ == "__main__":
    print("--- 🚀 Testing Engine ---")
    
    # 1. Test Data Load
    clients = load_data()
    print(f"✅ Loaded {len(clients)} clients.")
    
    # 2. Test Market Data
    ticker_to_check = "TSLA"
    market_data = check_stock_price(ticker_to_check)
    print(f"📊 Market Data: {market_data}")
    
    # 3. Test Client Filtering
    affected = get_impacted_clients(clients, ticker_to_check)
    print(f"🎯 Found {len(affected)} clients with {ticker_to_check}:")
    print(affected[['Name', 'Holdings']])
