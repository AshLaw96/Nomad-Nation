import requests
import os
from django.core.cache import cache

API_KEY = os.environ.get("EXCHANGE_RATE_API_KEY")

API_URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/GBP'


def get_exchange_rates():
    """
    Fetches exchange rates from the API and caches them.
    """
    cached_rates = cache.get("exchange_rates")
    if cached_rates:
        # Use cached rates
        return cached_rates

    response = requests.get(API_URL)
    try:
        # Attempt to parse JSON
        data = response.json()
        print("API Response:", data)

        # Check if the API response contains "rates"
        if "rates" in data:
            # Cache for 1 hour
            cache.set("exchange_rates", data["rates"], timeout=3600)
            return data["rates"]
        else:
            print("Error: API response does not contain 'rates'.", data)
            # Return empty rates to avoid KeyError
            return {}

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return {}

    except ValueError:
        print("Error: Failed to decode JSON from API response.")
        return {}


def convert_currency(amount, target_currency):
    """
    Converts an amount from GBP to the target currency.
    """
    rates = get_exchange_rates()
    if target_currency in rates:
        return round(amount * rates[target_currency], 2)
    return amount
