import yfinance as yf
import pandas as pd

def run_backtest(ticker):
    print(f"Descargando datos de {ticker}...")
    data = yf.download(ticker, start="2010-01-01", end="2025-06-26", auto_adjust=False)
    data.index = pd.to_datetime(data.index)

    # Precio mensual
    monthly_close = data['Close'].resample('ME').last()

    # Si viene con multi-columnas, tomar el precio correcto
    if isinstance(monthly_close, pd.DataFrame):
        if ticker in monthly_close.columns:
            price_series = monthly_close[ticker]
        else:
            price_series = monthly_close.iloc[:, 0]
    else:
        price_series = monthly_close

    price_df = pd.DataFrame({'Price': price_series})
    price_df['Month'] = price_df.index.month
    price_df['Year'] = price_df.index.year

    # Precio promedio por mes (para detectar el mejor mes histórico)
    avg_price_by_month = price_df.groupby('Month')['Price'].mean()

    month_cheapest = avg_price_by_month.idxmin()
    month_expensive = avg_price_by_month.idxmax()

    print(f"Mes históricamente más barato para comprar: {month_cheapest}")
    print(f"Mes históricamente más caro para vender: {month_expensive}")

    # Resultados año por año
    results = []

    for year in price_df['Year'].unique():
        try:
            buy_price = price_df[(price_df['Year'] == year) &
                                 (price_df['Month'] == month_cheapest)]['Price'].values[0]

            # Si el mes de venta es anterior al de compra, se vende el año siguiente
            if month_expensive > month_cheapest:
                sell_price = price_df[(price_df['Year'] == year) &
                                      (price_df['Month'] == month_expensive)]['Price'].values[0]
            else:
                sell_price = price_df[(price_df['Year'] == year + 1) &
                                      (price_df['Month'] == month_expensive)]['Price'].values[0]

            ret = (sell_price - buy_price) / buy_price
            results.append({
                'Year': year,
                'Buy Month': month_cheapest,
                'Sell Month': month_expensive,
                'Return (%)': ret * 100     # ← CORREGIDO
            })
        except IndexError:
            continue

    results_df = pd.DataFrame(results)
    print(results_df)

    # Métricas finales
    avg_return = results_df['Return (%)'].mean()
    cum_return = (results_df['Return (%)'] / 100 + 1).prod() - 1

    print(f"\nRetorno promedio anual: {avg_return:.2f}%")
    print(f"Retorno acumulado total: {cum_return*100:.2f}%")

if __name__ == "__main__":
    ticker_input = input("Ingrese el ticker de la acción que quiere analizar (ejemplo: AAPL): ").upper().strip()
    run_backtest(ticker_input)
