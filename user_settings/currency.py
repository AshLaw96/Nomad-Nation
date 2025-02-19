import os
import requests


def convert_currency(amount, from_currency, to_currency):
    """
    Converts an amount from one currency to another using the
    ExchangeRate API.
    """
    api_key = os.environ.get('EXCHANGE_RATE_API_KEY')
    url = (
        f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}'
    )
    response = requests.get(url)
    data = response.json()

    if 'conversion_rates' not in data:
        raise KeyError(f"Key 'conversion_rates' not found in response: {data}")

    rate = data['conversion_rates'][to_currency]

    return amount * rate
