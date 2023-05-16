import numpy as np

def simulate_coin_toss():
   
    coins = np.random.randint(0, 2, 3)  
    
   
    num_heads = np.sum(coins)
    
    return num_heads

num_simulations = 100000
no_heads_count = 0

for i in range(num_simulations):
    num_heads = simulate_coin_toss()
    if num_heads == 0:
        no_heads_count += 1

probability_no_heads = no_heads_count / num_simulations

print("Probability of no heads:", probability_no_heads)
