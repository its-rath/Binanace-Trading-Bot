
# 🧠 MASTER PROMPT — Simplified Binance Trading Bot (Python Project)

## 🎯 Overview
You are an expert **Python developer specializing in algorithmic trading and Binance API integration**.  
Your task is to **design and implement a Simplified Trading Bot** using the **Binance Futures Testnet**.  
Follow all specifications carefully and produce **fully functional, modular, and production-ready code** with complete explanations.

---

## ⚙️ PROJECT REQUIREMENTS

### Goal
Build a Python-based trading bot capable of placing **market and limit orders** (buy and sell) on **Binance Futures Testnet (USDT-M)** using the official API.

---

## 🧩 TECHNICAL SPECIFICATIONS

**Environment:**
- Language: Python  
- Binance Testnet Base URL: `https://testnet.binancefuture.com`  
- Libraries: `python-binance` (preferred) or REST API calls  

**Core Functionalities:**
1. **Initialize the Client**
   - Register and activate a Binance Futures Testnet account  
   - Generate API Key and Secret  
   - Connect via `Client(api_key, api_secret, testnet=True)`  

2. **Order Management**
   - Place **Market Orders** (Buy/Sell)  
   - Place **Limit Orders** (Buy/Sell)  
   - Output execution status and full order details  

3. **User Interface (CLI)**
   - Accept and validate user input (order type, side, symbol, quantity, price)  
   - Clear and structured command-line prompts  
   - Display confirmation and order feedback  

4. **Logging and Error Handling**
   - Log all **API requests, responses, and errors** to a file  
   - Include timestamped events and error tracebacks  

---

## 🧠 STRUCTURE AND DESIGN

### Class Definition
```python
from binance import Client

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret, testnet=testnet)
        # Complete implementation here
```

### Design Principles
- Clean modular code  
- Clear input/output separation  
- Reusable methods for different order types  
- Proper error messages and exception handling  

---

## 💡 BONUS FEATURES (Optional Enhancements)

1. Add a **third order type**, such as:
   - Stop-Limit  
   - OCO  
   - Grid or TWAP  

2. Create a **simple UI**:
   - Enhanced CLI menu or lightweight frontend (Tkinter or Streamlit)

---

## 📤 FINAL OUTPUT EXPECTATIONS

- Fully implemented Python script or module (`trading_bot.py`)  
- Command-line example of how to run and place an order  
- Detailed docstrings and inline comments  
- Log file showcasing request/response tracking  
- Optional: demo script for extended features  

---

## 💬 DELIVERABLES
1. `BasicBot` class implementation  
2. Command-line interface integration  
3. Logging system  
4. Example output of order execution  
5. Optional extended features  

---

## 🧠 ROLE SETUP FOR AI

> *You are an expert Python trading engineer. Build the Binance Futures Testnet trading bot as per the full specification above, ensuring correct API integration, input validation, and robust logging.*

---
