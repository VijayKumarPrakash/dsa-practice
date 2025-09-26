
import numpy as np

def calculate_revenue(prices, algo, k):
    revenue = 0
    n = len(prices)
    
    income = np.sum(prices * algo)
    expense = np.sum(prices * (1 - algo))
    
    return income - expense

def calculate_override_index(prices, algo, k):
    n = len(prices)
    max_profit = 0
    override_index = 0

    for i in range(n-k):
        algo_sub = algo[i:i+k]

        if 0 in algo_sub:
            prices_sub = prices[i:i+k]
            additional_profit = np.sum(prices_sub * (1-algo_sub))

            if additional_profit > max_profit:
                max_profit = additional_profit
                override_index = i

    return override_index

prices = np.array([5, 3, 8, 2, 6, 4, 9, 2, 3, 7])
algo   = np.array([1, 0, 0, 1, 0, 1, 0, 1, 0, 0])
k = 3

print(f"Prices:    {prices}")
print(f"Algorithm: {algo}")
print(f"Window Size (k): {k}")

baseline_profit = calculate_revenue(prices, algo, k)
print(f"Baseline Profit: {baseline_profit}")

override_index = calculate_override_index(prices, algo, k)
print(f"Override Index: {override_index}")

revised_algo = algo.copy()
revised_algo[override_index:override_index+k] = 1
print(f"Revised Algorithm: {revised_algo}")

potential_profit = calculate_revenue(prices, revised_algo, k)
print(f"Potential Profit after Override: {potential_profit}")
