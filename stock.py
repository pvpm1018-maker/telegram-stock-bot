from pykrx import stock
from datetime import datetime


def get_stock_price(ticker):
    today = datetime.today().strftime("%Y%m%d")

    try:
        df = stock.get_market_ohlcv_by_date(today, today, ticker)

        if df.empty:
            return None

        current = int(df.iloc[-1]["종가"])
        open_price = int(df.iloc[-1]["시가"])

        change = current - open_price
        percent = round(change / open_price * 100, 2)

        return {
            "price": current,
            "change": change,
            "percent": percent
        }

    except Exception:
        return None
