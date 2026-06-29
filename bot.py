import urllib.request
import json
import ssl

# UMA Optimistic Oracle on Sepolia
# Query assertion events to find prediction market resolutions

ALCHEMY_URL = "https://eth-sepolia.g.alchemy.com/v2/IZYEU2cWBgnFmgiTAgpWD"

def rpc_call(method, params):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    payload = json.dumps({
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": 1
    }).encode()
    
    req = urllib.request.Request(
        ALCHEMY_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    
    with urllib.request.urlopen(req, context=ctx) as response:
        return json.loads(response.read())

def main():
    print("🤖 Prediction Market Bot")
    print("=" * 50)
    
    # Get latest block
    result = rpc_call("eth_blockNumber", [])
    block = int(result['result'], 16)
    print(f"\n📦 Latest Sepolia Block: {block}")
    
    # Get ETH price from Chainlink oracle on Sepolia
    # ETH/USD price feed: 0x694AA1769357215DE4FAC081bf1f309aDC325306
    CHAINLINK_ETH_USD = "0x694AA1769357215DE4FAC081bf1f309aDC325306"
    
    # latestRoundData() function selector
    data = "0xfeaf968c"
    
    result = rpc_call("eth_call", [{
        "to": CHAINLINK_ETH_USD,
        "data": data
    }, "latest"])
    
    raw = result['result']
    # Parse price (second 32 bytes, 8 decimals)
    price_hex = raw[66:130]
    price = int(price_hex, 16) / 10**8
    
    print(f"\n🔮 Chainlink Oracle — ETH/USD Price Feed")
    print(f"   Current ETH Price: ${price:,.2f}")
    print(f"   Oracle Address: {CHAINLINK_ETH_USD}")
    print(f"   Network: Sepolia Testnet")
    
    # Simulate prediction market resolution
    print(f"\n📊 Simulated Prediction Market:")
    print(f"   Question: Will ETH be above $3000?")
    
    if price > 3000:
        print(f"   Resolution: ✅ YES (ETH = ${price:,.2f} > $3000)")
    else:
        print(f"   Resolution: ❌ NO (ETH = ${price:,.2f} < $3000)")
    
    print(f"\n{'=' * 50}")
    print("Bot run complete!")

if __name__ == "__main__":
    main()
