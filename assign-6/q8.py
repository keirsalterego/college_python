
prices = {"laptop": 55000, "phone": 25000, "tablet": 18000}


max_product = max(prices, key=prices.get)
max_price = prices[max_product]

print(f"The product with maximum price is '{max_product}' with price ₹{max_price}")

