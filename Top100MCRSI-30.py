import yfinance as yf
import pandas as pd

# =========================================
# Configuración
# =========================================
top100_tickers = ['NVDA','AAPL','GOOGL','MSFT','AMZN','META','AVGO','TSLA','TSM','BRK-B','LLY','WMT','JPM','V','XOM','MA','ORCL','UNH','HD','COST','PG','NFLX','JNJ','BAC','SAP','ABBV','CRM','WFC','ASML','KO','TM','CVX','ACN','MRK','FOC','ADBE','PEP','LIN','SHEL','AMD','TMO','PM','DIS','MCD','ISRG','CSCO','ABT','INTU','BX','GE','CAT','IBM','NOW','TXN','TTE','VZ','AXP','RY','QCOM','AMAT','BKNG','PFE','MS','DHR','NEE','ARM','HSBC','AMX','HON','LOW','RTX','COP','UNP','GS','SPGI','T','UBER','PLTR','TJX','MU','SCHW','SYK','LRCX','BLK','NKE','VRTX','ETN','BSX','ANET','C','ADI','PANW','REGN','DE','BMY','PLD','CB','MDT','GILD','MMC']
INTERVAL = '4h'
RSI_PERIOD = 14
RSI_THRESHOLD = 30
# =========================================

def compute_rsi(series, period=14):
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(window=period, min_periods=period).mean()
    avg_loss = loss.rolling(window=period, min_periods=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def get_rsi_for_ticker(ticker):
    try:
        df = yf.download(ticker, period="60d", interval=INTERVAL, progress=False, auto_adjust=False)
        if df.empty or 'Close' not in df.columns:
            print(f"> No hay datos para {ticker}")
            return None
        close_series = df['Close'].squeeze()  # asegurar que sea 1D
        rsi_series = compute_rsi(close_series, RSI_PERIOD)
        latest_rsi = rsi_series.iloc[-1]
        return latest_rsi
    except Exception as e:
        print(f"Error con {ticker}: {e}")
        return None

# =========================================
# Main
# =========================================
if __name__ == "__main__":
    result = []
    for ticker in top100_tickers:
        rsi_value = get_rsi_for_ticker(ticker)
        if rsi_value is not None:
            print(f"{ticker}: RSI={rsi_value:.2f}")
            if rsi_value < RSI_THRESHOLD:
                result.append((ticker, round(rsi_value,2)))
    
    print("\n⚠️ Tickers con RSI por debajo de", RSI_THRESHOLD)
    for t,r in result:
        print(f"{t} -> RSI = {r}")

