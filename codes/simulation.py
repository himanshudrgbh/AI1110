import random


def simulate_coin_toss():

    coins = [random.randint(0, 1) for _ in range(3)]

    num_heads = coins.count(1)

    return num_heads



num_simulations = 100000
no_heads_count = 0

for _ in range(num_simulations):
    num_heads = simulate_coin_toss()
    if num_heads == 0:
        no_heads_count += 1


probability_no_heads = no_heads_count / num_simulations

print("Probability of no heads:", probability_no_heads)

