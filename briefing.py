import json
from stock import get_stock_price


def create_briefing():

    with open("portfolio.json", encoding="utf-8") as f:
        portfolio = json.load(f)

    message = "📈 JH Portfolio AI Bot\n"
    message += "=" * 24 + "\n\n"

    for item in portfolio["stocks"]:

        result = get_stock_price(item["ticker"])

        if result is None:
            message += f"❌ {item['name']}\n\n"
            continue

        icon = "🔺" if result["percent"] >= 0 else "🔻"

        message += (
            f"📌 {item['name']}\n"
            f"현재가 : {result['price']:,}원\n"
            f"{icon} {result['percent']}%\n\n"
        )

    return message
