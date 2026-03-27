import yfinance as yf

def check_stock_drop(ticker, threshold_percent=5.0):
    """
    Checks if a stock has dropped by more than the threshold today.
    Returns: (True/False, current_price, percent_change)
    """
    print(f"🔍 Checking real-time data for {ticker}...")
    stock = yf.Ticker(ticker)
    
    # Get today's data
    history = stock.history(period="1d")
    current_price = history['Close'].iloc[-1]
    open_price = history['Open'].iloc[-1]
    
    # Calculate percentage change
    change = ((current_price - open_price) / open_price) * 100
    
    print(f"📉 {ticker} is at ${current_price:.2f} (Change: {change:.2f}%)")
    
    # Check if the drop is "bad enough" (e.g., -5%)
    if change <= -threshold_percent:
        return True, current_price, change
    else:
        return False, current_price, change

# Test it immediately
if __name__ == "__main__":
    # Let's pretend TSLA is crashing. 
    # (In reality, it might not be, so we will set a positive threshold just to see it work for now)
    alert, price, drop = check_stock_drop("TSLA", threshold_percent=0.1) 
    
    if alert:
        print("🚨 ALERT: Significant movement detected!")
    else:
        print("✅ Market is stable.")
