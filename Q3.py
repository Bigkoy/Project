def find_max_profit(filename):
    with open(filename, "r") as f:
        prices = [float(line.strip()) for line in f.readlines()]
    
    max_profit_val = 0
    current_max_val = float("-inf")
    
    for price in reversed(prices):
        current_max_val = max(current_max_val, price)
        potential_profit = current_max_val - price
        max_profit_val = max(max_profit_val, potential_profit)
    
    print(f"Maximum Possible Profit: ${max_profit_val:.2f}")
find_max_profit("sample_AAPL.txt")
