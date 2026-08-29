# myExchangeRate

A lightweight Python package to fetch and retrieve currency exchange rates reliably. Built with robust built-in error handling to manage network requests and API downtimes safely.

## Features

- **Automated Data Fetching**: Retrieves current exchange rates directly upon initialization.
- **Robust Exception Handling**: Protects your application from hanging or crashing due to network issues, timeouts, or invalid server responses.
- **Easy Lookup**: Quick rate retrieval using standard currency quote identifiers (e.g., "USD").
- **Data Integrity**: Built-in validation ensures API responses are safely parsed as JSON.

## Installation

Ensure you have the required dependencies installed:

```bash
pip install requests
```

Make sure your project structure includes the required definition file `myExchangeRateDefinitions.py` containing the API URL and timeout configuration:

```python
# myExchangeRateDefinitions.py Example
STR_URL_2_EXCHANGE_DATA = "https://example.com"
INT_RESPONSE_TIME_OUT = 5
```

## Quick Start

Here is how you can use `myExchangeRate` in your script:

```python
from myExchangeRate import MyExchangeRate

# Initialize the client (automatically fetches the data)
exchange = MyExchangeRate()

# Retrieve a specific exchange rate
usd_rate = exchange.get_exchange_rate("USD")

if usd_rate is not None:
    print(f"Current USD Exchange Rate: {usd_rate}")
else:
    print("Exchange rate not found or API request failed.")
```

## Error Handling Details

The class safely encapsulates network actions. If the remote API is down, timed out, or returns bad data, the class logs the specific error to the console and initializes an empty dataset without crashing your main application thread. It gracefully catches:
- HTTP status errors (4xx, 5xx)
- Connection drops and DNS failures
- Request timeouts
- Malformed/Non-JSON API payloads

## Authors & License

- **Author**: Oliver Rudow
- **Version**: 0.1.0
- **Copyright**: Copyright 2026, Brain Center Höfen
