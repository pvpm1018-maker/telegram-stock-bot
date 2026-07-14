import yfinance as yf

# portfolio.json의 종목코드와 연결될 티커
TICKERS = {
    "000660": "000660.KS",   # SK하이닉스
    "005930": "005930.KS",   # 삼성전자
    "028260": "028260.KS",   # 삼성물산
    "031330": "031330.KQ",   # 에스에이엠티
    "034220": "034220.KS",   # LG디스플레이
    "240810": "240810.KQ",   # 원익IPS
    "402340": "402340.KS"    # SK스퀘어
}


def get_stock_price(code):
    ticker = yf.Ticker(TICKERS[code])

    data = ticker.history(period="2d")

    if len(data) < 2:
        return None

    current = float(data["Close"].iloc[-1])
    previous = float(data["Close"].iloc[-2])

    change = current - previous
    percent = (change / previous) * 100

    return {
        "price": round(current),
        "change": round(change, 2),
        "percent": round(percent, 2)
    }
