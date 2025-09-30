"""
You're given:
- An array prices[0..n-1]
- A binary array algo[0..n-1], where algo[i] = 0 means a buy (so you subtract prices[i] from revenue) and algo[i] = 1 means a sell (so you add prices[i] to revenue)
- An integer k

You are allowed to pick a consecutive subarray of length k (say from i to i+k-1) and force all their corresponding algo[j] to be 1 (i.e. make them all sells). You want to choose the position of that length-k block to maximize the total revenue (overall, with those changes applied).

Example:
prices = [5, 3, 8, 2, 6, 4]
algo   = [1, 0, 0, 1, 0, 1]
k = 3

base revenue = +5-3-8+2-6+4 = -6

Answer = 22
You'd choose window starting at index 2 (positions 2,3,4) to force those algos to sell; revenue = 22
"""

import numpy as np
from collections import deque

def calculate_revenue(prices, algo, k):
    revenue = 0
    n = len(prices)
    
    income = np.sum(prices * algo)
    expense = np.sum(prices * (1 - algo))
    
    return income - expense

def calculate_override_index(prices, algo, k):
    prices_copy = prices.copy()
    n = len(prices_copy)
    max_profit = 0
    override_index = 0

    # Transform prices so that sells are 0, buys remain unchanged
    for i in range(n):
        if algo[i] == 1:
            prices_copy[i] = 0

    # Create and populate queue
    my_queue = deque()
    my_queue.extend(prices_copy[:k])
    current_sum = sum(my_queue)

    for i in range(k, n):
        my_queue.popleft()
        my_queue.append(prices_copy[i])

        current_sum = sum(my_queue)
        if current_sum > max_profit:
            max_profit = current_sum
            override_index = i - k + 1

    return override_index

# Test 1
# prices = np.array([5, 3, 8, 2, 6, 4])
# algo = np.array([1, 0, 0, 1, 0, 1])
# k = 3

# Test 2
prices = np.array([5, 3, 8, 2, 6, 4, 9, 2, 3, 7])
algo   = np.array([1, 0, 0, 1, 0, 1, 0, 1, 0, 0])
k = 3

print(f"Prices:    {prices}")
print(f"Algorithm: {algo}")
print(f"Window Size (k): {k}")

baseline_revenue = calculate_revenue(prices, algo, k)
print(f"Baseline Revenue: {baseline_revenue}")

override_index = calculate_override_index(prices, algo, k)
print(f"Override Index: {override_index}")

revised_algo = algo.copy()
revised_algo[override_index:override_index+k] = 1
print(f"Revised Algorithm: {revised_algo}")

potential_revenue = calculate_revenue(prices, revised_algo, k)
print(f"Potential Revenue after Override: {potential_revenue}")
