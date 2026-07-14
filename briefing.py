from stock import get_stock_price

import json


def create_briefing():

    with open("portfolio.json", encoding="utf-8") as f:

        portfolio = json.load(f)

    message = "📈 JH Portfolio AI Bot\n\n"

    for stock in portfolio["stocks"]:

        info = get_stock_price(stock["ticker"])

        if info is None:

            continue

        message += (

            f"📌 {stock['name']}\n"

            f"현재가 : {info['price']:,}원\n"

            f"등락률 : {info['percent']}%\n\n"

        )

    return message
