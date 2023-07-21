
---

# Crypto Checkout Program Using NOWPayments API

This program is used to create a cryptocurrency checkout using the NOWPayments API. The objective of this program is to get the checkout URL after the checkout is successfully created.

## Getting Started

### Prerequisites

- Python 3.6 or higher.
- An account with [NOWPayments](https://nowpayments.io/).

### Instructions

#### 1. Getting your API Key

- Log into your NOWPayments account.
- Navigate to the API keys section.
- Generate or copy your existing API Key.

#### 2. Setting Up the Program

- Clone this repository to your local machine.
- Install the required Python packages using pip:

```bash
pip install requests python-dotenv pytz
```

- Create a file named `.env` in the project root directory.
- Paste your API Key into the `.env` file in the following format:

```bash
NOW_API=your_api_key
```

Replace `your_api_key` with the actual API Key you obtained from NOWPayments.

#### 3. Running the Program

- Navigate to the project directory in your terminal.
- Run the program using Python:

```bash
python main.py
```

- When prompted, input the product title and price.
- The program will then generate a checkout and return a URL for this checkout. You can use this URL to view and complete the checkout process.

---
-------------------------------------------------------------------------------------------------
Title: Crypto Checkout Program Using NOWPayments API
Author: @MrStarBoy
Date (IST): 21-07-2023
-------------------------------------------------------------------------------------------------
This program is used to create a cryptocurrency checkout using the NOWPayments API. The objective
of this program is to get the checkout URL after the checkout is successfully created.
-------------------------------------------------------------------------------------------------

That's it! If you have any issues, please submit an issue on this GitHub repository.

