from django.test import TestCase
from unittest.mock import patch
from decimal import Decimal
from user_settings.currency import get_exchange_rates, convert_currency


class CurrencyConversionTest(TestCase):
    @patch("user_settings.currency.requests.get")
    def test_get_exchange_rates(self, mock_get):
        """
        Test the behavior of fetching exchange rates from an external API.
        This test mocks the API response to simulate receiving an exchange
        rate for USD. It then checks if the `get_exchange_rates` function
        correctly returns the expected rate (1.25) for USD.
        """
        # Mock API response
        mock_get.return_value.json.return_value = {
            "conversion_rates": {"USD": 1.25}
        }

        # Call the function to fetch the exchange rate for USD
        rate = get_exchange_rates("USD")
        # Assert that the fetched rate is the expected value of 1.25
        self.assertEqual(rate, 1.25)

    @patch("user_settings.currency.get_exchange_rates")
    def test_convert_currency(self, mock_get_exchange_rates):
        """
        Test the currency conversion functionality when a valid exchange rate
        is returned.
        This test ensures that the `convert_currency` function correctly
        converts a given amount (e.g., 100) to the target currency using
        the mocked exchange rate (1.25 for USD). The expected output should
        be 125.00 (100 * 1.25).
        """
        mock_get_exchange_rates.return_value = 1.25

        # Call the function to convert 100 units of currency into USD
        converted_amount = convert_currency(Decimal("100"), "USD")
        # Assert that the converted amount is 100 * 1.25 = 125.00
        self.assertEqual(converted_amount, Decimal("125.00"))

    @patch("user_settings.currency.get_exchange_rates")
    def test_convert_currency_no_rate(self, mock_get_exchange_rates):
        """
        Test the currency conversion behavior when no exchange rate is found.
        This test simulates a scenario where no exchange rate is returned
        (an empty dictionary). It checks that the `convert_currency` function
        returns the original amount unchanged (100.00) when no rate is
        available.
        """
        mock_get_exchange_rates.return_value = {}

        # Call the function to convert 100 units of currency with no rate
        # available
        converted_amount = convert_currency(Decimal("100"), "USD")
        # Assert that the original amount is returned,
        # as no exchange rate is available
        self.assertEqual(converted_amount, Decimal("100.00"))
