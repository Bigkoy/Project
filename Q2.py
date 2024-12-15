import matplotlib.pyplot as plt

def plot_stock_prices(filename):
    with open(filename, "r") as f:
        prices = [float(line.strip()) for line in f.readlines()]
    
    days = list(range(1, len(prices) + 1))
    
    plt.figure(figsize=(10, 6))
    plt.plot(days, prices, label="Apple Stock Price", color="blue")
    plt.title("Apple Stock Price, Nov 2019 to Nov 2020")
    plt.xlabel("Day")
    plt.ylabel("Trading Price")
    plt.grid(True)
    plt.legend()
    plt.savefig("apple_stock_prices.png")
    plt.show()
plot_stock_prices("sample_AAPL.txt")
