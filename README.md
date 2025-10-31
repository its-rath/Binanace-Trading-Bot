# 🤖 Binance Futures Trading Bot

This is a Python-based trading bot that allows you to place market, limit, and stop-limit orders on the Binance Futures Testnet.

## ✨ Features

- Place Market Orders (Buy/Sell)
- Place Limit Orders (Buy/Sell)
- Place Stop-Limit Orders (Buy/Sell)
- Interactive Command-Line Interface (CLI)
- Robust Logging

## 🚀 Getting Started

### Prerequisites

- Python 3.6+
- pip

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/Binanace-Trading-Bot.git
   cd Binanace-Trading-Bot
   ```

2. **Install the required libraries:**
   ```sh
   pip install -r requirements.txt
   ```

## ⚙️ Configuration

1. Open the `config.py` file.
2. Replace `"YOUR_API_KEY"` and `"YOUR_API_SECRET"` with your actual Binance Testnet API key and secret.

   **Note:** You can generate an API key and secret on the [Binance Testnet website](https://testnet.binancefuture.com).

## ▶️ Usage

To start the trading bot, run the following command:

```sh
python main.py
```

The bot will present you with a menu of options to choose from:

```
Select an option:
1. Place Market Order
2. Place Limit Order
3. Place Stop-Limit Order
4. Exit
```

Follow the on-screen prompts to place your desired order.

## 📝 Logging

All trading activities, API requests, and errors are logged in the `trading_bot.log` file. This file is useful for debugging and tracking the bot's performance.

## ⚠️ Disclaimer

This trading bot is for educational purposes only. Trading cryptocurrencies involves significant risk. Use this bot at your own risk. The author is not responsible for any financial losses.
