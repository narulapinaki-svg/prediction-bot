# Prediction Market Resolution Bot

## Overview

This project is a Python bot that queries the resolution state of an active prediction market contract. It connects to the blockchain, retrieves market information, and checks whether the selected prediction market has been resolved.

## Features

- Query an active prediction market
- Fetch the current resolution status
- Display the result in a simple, readable format
- Built using Python

## Technologies Used

- Python 3
- Web3.py
- Requests

## Installation

Clone the repository:

```bash
git clone https://github.com/narulapinaki-svg/<YOUR-REPO-NAME>.git
cd <YOUR-REPO-NAME>
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the bot using:

```bash
python bot.py
```

## Example Output

```text
Prediction Market Status
------------------------
Market ID: 0x...
Resolved: True
Outcome: YES
```

## Project Structure

```
.
├── bot.py
├── README.md
└── requirements.txt
```

## Objective

This project was developed as part of **Week 3 – Information Economies & Security**. The goal was to build a Python bot capable of querying the resolution state of an active prediction market contract and understanding the role of oracles and prediction markets in blockchain ecosystems.

## Author

Pinaki Narula
