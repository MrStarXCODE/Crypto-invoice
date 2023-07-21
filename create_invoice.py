import requests
import json
from dotenv import load_dotenv
import os
# -------------------------------------------------------------------------------------------------
# Title: Crypto Checkout Program Using NOWPayments API
# Author: $Kek (MrStarXCODE)
# Date (IST): 21-07-2023
# -------------------------------------------------------------------------------------------------
# This program is used to create a cryptocurrency checkout using the NOWPayments API. The objective
# of this program is to get the checkout URL after the checkout is successfully created.
# -------------------------------------------------------------------------------------------------
load_dotenv()
NOW_API = os.getenv('NOW_API')

url = "https://api.nowpayments.io/v1/invoice"
product_title = input('Product Title: ')
price_amount = input('Product Price: ')

payload = json.dumps({
  "price_amount": price_amount,
  "price_currency": "usd",
  "order_id": "RGDBP-21314",
  "order_description": product_title,
  "ipn_callback_url": "https://nowpayments.io",
  "success_url": "https://nowpayments.io",
  "cancel_url": "https://nowpayments.io"
})
headers = {
  'x-api-key': f'{NOW_API}',
  'Content-Type': 'application/json'
}

# Send the request to the API
response = requests.post(url, headers=headers, data=payload)

# Check if the request was successful and then extract the invoice_url
if response.status_code == 200:
    data = response.json()
    if "invoice_url" in data:
        print(f"Your invoice URL is: {data['invoice_url']}")
else:
    print("Failed to create an invoice. Please try again.")
