from decimal import Decimal, ROUND_HALF_UP
import requests
import os
from django.core.cache import cache

API_KEY = os.environ.get("EXCHANGE_RATE_API_KEY")

API_URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/GBP'


def get_exchange_rates(target_currency):
    """
    Fetches exchange rates from the API and caches them.
    """
    cached_rates = cache.get(target_currency)
    if cached_rates:
        # Use cached rates
        return cached_rates

    response = requests.get(API_URL)
    try:
        # Attempt to parse JSON
        data = response.json()
        print("API Response:", data['conversion_rates'][target_currency])

        # Check if the API response contains "rates"
        if "conversion_rates" in data:
            # Cache for 1 hour
            cache.set(
                target_currency,
                data["conversion_rates"][target_currency],
                timeout=3600
            )

            return data["conversion_rates"][target_currency]
        else:
            print("Error: API response does not contain 'conversion_rates'.")
            print(data)
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
    rates = get_exchange_rates(target_currency)
    if rates:
        rate_decimal = Decimal(str(rates))
        result = amount * rate_decimal
        return result.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return amount
