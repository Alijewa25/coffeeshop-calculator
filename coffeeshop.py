import requests
import json

def fetch_data(url):
    response = requests.get(url)
    return response.text

def deserialize_data(json_data):
    return json.loads(json_data)

def get_data_from_key(data, key):
    return data[key]

def get_price(prices, item):
    return prices[item]

def calculate_day(day_data, prices):
    total = 0
    for item, count in day_data["drinks"].items():
        total += get_price(prices, item) * count
    for item, count in day_data["desserts"].items():
        total += get_price(prices, item) * count
    return total

def calculate_week(week_data, prices):
    total = 0
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    for day in days:
        day_data = get_data_from_key(week_data, day)
        total += calculate_day(day_data, prices)
        total += day_data["tips"]
    return total

url = "https://raw.githubusercontent.com/ruslanhamidov/coffee_data/main/coffeeshop.json"
raw = fetch_data(url)
data = deserialize_data(raw)
prices = get_data_from_key(data, "prices")
print(calculate_week(data, prices))