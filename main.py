
import logging
from trading_bot import BasicBot
from config import API_KEY, API_SECRET
from rich.console import Console
from rich.prompt import Prompt

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("trading_bot.log"),
        ]
    )

def main():
    setup_logging()
    console = Console()

    if API_KEY == "YOUR_API_KEY" or API_SECRET == "YOUR_API_SECRET":
        console.print("[bold red]Please replace 'YOUR_API_KEY' and 'YOUR_API_SECRET' in config.py with your actual Binance API key and secret.[/bold red]")
        return

    bot = BasicBot(api_key=API_KEY, api_secret=API_SECRET)

    while True:
        console.print("\n[bold cyan]Select an option:[/bold cyan]")
        console.print("1. Place Market Order")
        console.print("2. Place Limit Order")
        console.print("3. Place Stop-Limit Order")
        console.print("4. Exit")

        choice = Prompt.ask("Enter your choice", choices=["1", "2", "3", "4"], default="4")

        if choice == '1':
            symbol = Prompt.ask("Enter symbol (e.g., BTCUSDT)").upper()
            side = Prompt.ask("Enter side", choices=["BUY", "SELL"]).upper()
            quantity = float(Prompt.ask("Enter quantity"))
            bot.place_market_order(symbol, side, quantity)
        elif choice == '2':
            symbol = Prompt.ask("Enter symbol (e.g., BTCUSDT)").upper()
            side = Prompt.ask("Enter side", choices=["BUY", "SELL"]).upper()
            quantity = float(Prompt.ask("Enter quantity"))
            price = float(Prompt.ask("Enter price"))
            bot.place_limit_order(symbol, side, quantity, price)
        elif choice == '3':
            symbol = Prompt.ask("Enter symbol (e.g., BTCUSDT)").upper()
            side = Prompt.ask("Enter side", choices=["BUY", "SELL"]).upper()
            quantity = float(Prompt.ask("Enter quantity"))
            price = float(Prompt.ask("Enter price"))
            stop_price = float(Prompt.ask("Enter stop price"))
            bot.place_stop_limit_order(symbol, side, quantity, price, stop_price)
        elif choice == '4':
            break

if __name__ == "__main__":
    main()
