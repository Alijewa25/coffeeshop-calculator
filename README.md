# Coffeeshop Calculator

## About
This program calculates the total weekly earnings of a coffeeshop.
It fetches JSON data from a remote URL, parses it, and computes the total revenue including tips for each day of the week.

## Libraries Used
- `requests` — sends HTTP GET request to fetch JSON data from the URL
- `json` — converts the JSON text response into a Python dictionary

## How It Works
1. `fetch_data(url)` sends a GET request to the given URL and returns the raw JSON text
2. `deserialize_data(json_data)` converts that raw JSON text into a Python dictionary so we can work with it
3. `get_data_from_key(data, key)` retrieves a specific entry from the dictionary by key — used to get a single day's data (e.g. "monday") or the prices
4. `get_price(prices, item)` looks up the price of a single drink or dessert from the prices dictionary
5. `calculate_day(day_data, prices)` loops through all drinks and desserts sold that day, multiplies each item's count by its price, and returns the total for that day
6. `calculate_week(week_data, prices)` loops through all 7 days, calls `calculate_day` for each, adds the tips for that day, and returns the grand total for the week

## How to Run

### Set up virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install requests
```

### Run the program
```bash
python3 coffeeshop.py
```

## Result
The coffeeshop earned **$1897.25** in one week including tips.