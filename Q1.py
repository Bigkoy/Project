f = open('sample_AAPL.txt', "r")
listItems = f.read().splitlines()
appleprices=listItems
for i in range(0, len(listItems)):
 appleprices[i] = float(listItems[i])
import numpy as np

def compute_mean_std(filename):
    with open(filename, "r") as f:
        prices = [float(line.strip()) for line in f.readlines()]
    
    mean_price = np.mean(prices)
    std_dev_price = np.std(prices)
    
    print(f"Mean: {mean_price}")
    print(f"Standard Deviation: {std_dev_price}")
compute_mean_std("sample_AAPL.txt")
