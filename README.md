# Prediction Market Resolution Bot

## Overview

This project is a Python bot that queries blockchain data from the Sepolia testnet and uses a Chainlink oracle price feed to determine the outcome of a simulated prediction market.

## Features

- Connects to the Ethereum Sepolia testnet using JSON-RPC
- Fetches the latest Ethereum block number
- Retrieves the latest ETH/USD price from the Chainlink Oracle
- Simulates the resolution of a prediction market based on the oracle price
- Displays the result in a simple and readable format

## Technologies Used

- Python 3
- Ethereum Sepolia Testnet
- Chainlink Oracle
- Alchemy JSON-RPC API

## Installation

Clone the repository:

```bash
git clone https://github.com/narulapinaki-svg/<YOUR-REPOSITORY-NAME>.git
cd <YOUR-REPOSITORY-NAME>
```

This project uses only Python's standard library, so no additional packages need to be installed.

## Usage

Run the bot using:

```bash
python bot.py
```

## Sample Output

```text
🤖 Prediction Market Bot
==================================================

📦 Latest Sepolia Block: 9123456

🔮 Chainlink Oracle — ETH/USD Price Feed
   Current ETH Price: $3,245.81
   Oracle Address: 0x694AA1769357215DE4FAC081bf1f309aDC325306
   Network: Sepolia Testnet

📊 Simulated Prediction Market:
   Question: Will ETH be above $3000?
   Resolution: ✅ YES

==================================================
Bot run complete!
```

## Project Structure

```
.
├── bot.py
└── README.md
```

## Objective

This project was developed as part of **Week 3 – Information Economies & Security**.

The objective was to build a Python bot capable of querying blockchain data and using an oracle to determine the resolution state of a prediction market scenario, demonstrating the role of prediction markets and decentralized oracles in blockchain ecosystems.

## Author

**Pinaki Narula**
