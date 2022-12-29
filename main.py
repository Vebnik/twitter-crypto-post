# libs
from dotenv import load_dotenv; load_dotenv()

# module
from src.bot.Bot import Bot


def bot_main() -> None:
  bot = Bot()
  