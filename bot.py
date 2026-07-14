print("=== NEW BOT VERSION ===")

from briefing import create_briefing
from telegram_sender import send_message


def main():
    message = create_briefing()
    send_message(message)


if __name__ == "__main__":
    main()
