
import logging
from trading_bot import BasicBot
from config import API_KEY, API_SECRET
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.table import Table
from rich import print as rprint
import validators

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("trading_bot.log"),
        ]
    )

def print_order_summary(symbol, side, type, quantity, price=None, stop_price=None):
    console = Console()
    table = Table(title="Order Request Summary")
    table.add_column("Parameter", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")

    table.add_row("Symbol", symbol)
    table.add_row("Side", side)
    table.add_row("Type", type)
    table.add_row("Quantity", str(quantity))
    if price:
        table.add_row("Price", str(price))
    if stop_price:
        table.add_row("Stop Price", str(stop_price))
    
    console.print(table)

def print_order_response(order):
    console = Console()
    if order:
        table = Table(title="Order Response Details", style="green")
        table.add_column("Field", style="cyan")
        table.add_column("Value", style="white")

        table.add_row("Order ID", str(order.get('orderId', 'N/A')))
        table.add_row("Status", order.get('status', 'N/A'))
        table.add_row("Executed Qty", order.get('executedQty', '0'))
        table.add_row("Avg Price", order.get('avgPrice', '0'))
        
        console.print(table)
        console.print(Panel("[bold green]Order Placed Successfully![/bold green]", expand=False))
    else:
        console.print(Panel("[bold red]Failed to Place Order. Check logs for details.[/bold red]", expand=False))

def get_input(prompt_text, validator_func):
    while True:
        value = Prompt.ask(prompt_text)
        is_valid, result = validator_func(value)
        if is_valid:
            return result
        rprint(f"[bold red]Error:[/bold red] {result}")

def main():
    setup_logging()
    console = Console()

    # Basic API Key Check (Note: Real validation happens when making calls)
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
            symbol = get_input("Enter symbol (e.g., BTCUSDT)", validators.validate_symbol)
            side = get_input("Enter side (BUY/SELL)", validators.validate_side)
            quantity = get_input("Enter quantity", validators.validate_quantity)
            
            print_order_summary(symbol, side, "MARKET", quantity)
            if Prompt.ask("Confirm order?", choices=["y", "n"]) == "y":
                order = bot.place_market_order(symbol, side, quantity)
                print_order_response(order)
            else:
                 console.print("[yellow]Order cancelled.[/yellow]")

        elif choice == '2':
            symbol = get_input("Enter symbol (e.g., BTCUSDT)", validators.validate_symbol)
            side = get_input("Enter side (BUY/SELL)", validators.validate_side)
            quantity = get_input("Enter quantity", validators.validate_quantity)
            price = get_input("Enter price", validators.validate_price)

            print_order_summary(symbol, side, "LIMIT", quantity, price=price)
            if Prompt.ask("Confirm order?", choices=["y", "n"]) == "y":
                order = bot.place_limit_order(symbol, side, quantity, price)
                print_order_response(order)
            else:
                 console.print("[yellow]Order cancelled.[/yellow]")

        elif choice == '3':
            symbol = get_input("Enter symbol (e.g., BTCUSDT)", validators.validate_symbol)
            side = get_input("Enter side (BUY/SELL)", validators.validate_side)
            quantity = get_input("Enter quantity", validators.validate_quantity)
            price = get_input("Enter price", validators.validate_price)
            stop_price = get_input("Enter stop price", validators.validate_price)

            print_order_summary(symbol, side, "STOP_LIMIT", quantity, price=price, stop_price=stop_price)
            if Prompt.ask("Confirm order?", choices=["y", "n"]) == "y":
                order = bot.place_stop_limit_order(symbol, side, quantity, price, stop_price)
                print_order_response(order)
            else:
                 console.print("[yellow]Order cancelled.[/yellow]")
                 
        elif choice == '4':
            break

if __name__ == "__main__":
    main()
