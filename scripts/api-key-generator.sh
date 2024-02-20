#!/usr/bin/env bash

# Generate a random string
random_string="us.robinhood-$(LC_ALL=C tr -dc 'a-zA-Z0-9' </dev/urandom | head -c 32)"

echo "BTC_APP_ROBINHOOD_API_KEY=${random_string}" > ../.api_key
