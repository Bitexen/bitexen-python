<div align="center">
  <img src="https://statics.bitexen.com/assets/logos/_logo_blue_black.svg" alt="Bitexen Logo" width="300"/>

  **Official Python Client for Bitexen Cryptocurrency Exchange**

  [![PyPI version](https://badge.fury.io/py/bitexen-client.svg)](https://badge.fury.io/py/bitexen-client)
  [![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
  [![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

  [Documentation](https://github.com/Bitexen/bitexen-python) • [API Reference](https://www.bitexen.com/api) • [Examples](examples/)
</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Configuration](#-configuration)
- [API Reference](#-api-reference)
- [Examples](#-examples)
- [Security](#-security)
- [Support](#-support)

---

## 🎯 Overview

`bitexen-python` is the official Python client library for Bitexen Cryptocurrency Exchange. It provides a simple, intuitive interface for interacting with the exchange's API endpoints, including market data, order management, and account operations.

## 📦 Installation

### From PyPI (Recommended)

```bash
pip install bitexen-client
```

### From Source

```bash
git clone https://github.com/Bitexen/bitexen-python.git
cd bitexen-python
pip install -e .
```

### Requirements

- Python 3.7 or higher
- `requests` library (automatically installed)

## 🚀 Quick Start

### Public Endpoints (No Authentication)

```python
from bitexen_client import API

# Initialize client
api = API()

# Get market information
market_info = api.get_market_info("BTCTRY")
print(market_info)

# Get ticker data
ticker = api.get_ticker("BTCTRY")
print(f"Last Price: {ticker.last_price}")

# Get order book
order_book = api.get_order_book("BTCTRY")
print(f"Bids: {order_book.buyers}")
print(f"Asks: {order_book.sellers}")
```

### Private Endpoints (Authentication Required)

```python
from bitexen_client import API

# Initialize with credentials
api = API(
    uri="https://www.bitexen.com/",
    key="your_api_key",
    secret="your_api_secret",
    username="your_username",
    pass_phrase="your_passphrase"
)

# Get account balance
balance = api.get_balance()
print(balance.data)

# Get open orders
orders = api.get_open_orders(account_name="Main", market_code="BTCTRY")
print(orders.data.orders)

# Create a limit buy order
order = api.create_order(
    account_name="Main",
    market_code="BTCTRY",
    buy_sell="B",  # "B" for buy, "S" for sell
    order_type="limit",
    volume=0.001,
    price=50000
)
print(f"Order created: {order.data.order_number}")

# Cancel an order
result = api.cancel_order(order_number="123456")
print(result)
```

## ⚙️ Configuration

### Option 1: Settings File (Recommended)

Create a `bitexen_client_settings.py` file in your project root:

```python
key = "your_api_key"
secret = "your_api_secret"
api_uri = "https://www.bitexen.com"
pass_phrase = "your_passphrase"
username = "your_username"
LOG_LEVEL = 10  # Optional: logging level
```

Then use the client without passing credentials:

```python
from bitexen_client import API
api = API()  # Automatically loads from settings file
```

### Option 2: Constructor Parameters

```python
from bitexen_client import API

api = API(
    uri="https://www.bitexen.com/",
    key="your_api_key",
    secret="your_api_secret",
    username="your_username",
    pass_phrase="your_passphrase",
    timeout=5  # Optional: request timeout in seconds
)
```

### Configuration Priority

Constructor parameters > Settings file

## 📚 API Reference

### Public Endpoints

| Method | Description | Parameters |
|--------|-------------|------------|
| `get_market_info(market_code)` | Get market information | `market_code`: e.g., "BTCTRY" |
| `get_ticker(market_code)` | Get ticker data | `market_code`: e.g., "BTCTRY" |
| `get_order_book(market_code)` | Get order book (bids/asks) | `market_code`: e.g., "BTCTRY" |

### Private Endpoints (Authentication Required)

| Method | Description | Parameters |
|--------|-------------|------------|
| `get_balance(account_name)` | Get account balance | `account_name`: default "Main" |
| `get_open_orders(account_name, market_code)` | Get open orders | `account_name`, `market_code` |
| `get_closed_orders(account_name, market_code)` | Get closed orders | `account_name`, `market_code` |
| `get_order_status(order_number)` | Get specific order status | `order_number`: order ID |
| `create_order(...)` | Create new order | See [Order Creation](#order-creation) |
| `cancel_order(order_number)` | Cancel an order | `order_number`: order ID |
| `withdraw_request(currency_code, amount, alias)` | Request withdrawal | `currency_code`, `amount`, `alias` |

### Order Creation

```python
api.create_order(
    account_name="Main",       # Account name (default: "Main")
    market_code="BTCTRY",      # Market pair
    buy_sell="B",              # "B" for buy, "S" for sell
    order_type="limit",        # "limit", "market", "stop"
    volume=0.001,              # Order volume
    price=50000,               # Order price (required for limit orders)
    stop_price=None            # Stop price (for stop orders)
)
```

### Response Format

All methods return a `dotdict` object with dot-notation access:

```python
result = api.get_ticker("BTCTRY")

# Access with dot notation
print(result.status)      # "success" or "error"
print(result.data.last)   # Last price
print(result.data.high)   # 24h high

# Or dictionary access
print(result['data']['last'])
```

### Error Handling

```python
from bitexen_client import APIException

try:
    order = api.create_order(...)
except APIException as e:
    print(f"Error code: {e.code}")
    print(f"Error message: {e.value}")
```

## 💡 Examples

Check the [examples/](examples/) directory for complete working examples:

```bash
python examples/example.py
```

Available example functions:
- `order_book()` - Fetch order book data
- `ticker()` - Get ticker information
- `market_info()` - Market details
- `balance()` - Account balance (requires auth)
- `open_orders()` - List open orders (requires auth)
- `closed_orders()` - List order history (requires auth)
- `create_order()` - Place an order (requires auth)
- `cancel_order()` - Cancel an order (requires auth)

## 🔐 Security

### Best Practices

- ✅ **Never commit credentials** - Use environment variables or settings files
- ✅ **Add to .gitignore** - Exclude `bitexen_client_settings.py`
- ✅ **Use HTTPS** - Always use `https://www.bitexen.com/`
- ✅ **Rotate API keys** - Regularly update your API credentials
- ✅ **Limit permissions** - Only grant necessary API permissions

### Authentication Flow

The client uses HMAC-SHA256 signature-based authentication:

```
Signature = HMAC-SHA256(
    apikey + username + passphrase + timestamp + request_body,
    secret_key
)
```

Headers sent with each private request:
- `ACCESS-KEY`: Your API key
- `ACCESS-USER`: Your username
- `ACCESS-PASSPHRASE`: Your passphrase
- `ACCESS-TIMESTAMP`: Request timestamp
- `ACCESS-SIGN`: HMAC signature

### Rate Limiting

The client includes automatic rate limit handling:
- Detects `429 Too Many Requests` responses
- Waits 5 seconds before retrying
- Automatically retries once

## 🆘 Support

- **Documentation:** [GitHub Repository](https://github.com/Bitexen/bitexen-python)
- **API Documentation:** [Bitexen API Docs](https://docs.bitexen.com/)
- **Issues:** [GitHub Issues](https://github.com/Bitexen/bitexen-python/issues)
- **Email:** development@bitexen.com

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
