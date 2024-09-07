import numpy as np
import matplotlib.pyplot as plt

# Possible outcomes for each coin
coin = ["Heads", "Tails"]
number_of_throws = 1000

# Simulate 1000 tosses for two coins
coin_throws_1 = np.random.choice(coin, number_of_throws)
coin_throws_2 = np.random.choice(coin, number_of_throws)

# Count the occurrences of each outcome
HH_count = np.sum((coin_throws_1 == "Heads") & (coin_throws_2 == "Heads"))
HT_count = np.sum((coin_throws_1 == "Heads") & (coin_throws_2 == "Tails"))
TH_count = np.sum((coin_throws_1 == "Tails") & (coin_throws_2 == "Heads"))
TT_count = np.sum((coin_throws_1 == "Tails") & (coin_throws_2 == "Tails"))
print(f'HH counts: {HH_count}')
print(f'HT counts: {HT_count}')
print(f'TH counts: {TH_count}')
print(f'TT counts: {TT_count}')

#Probabilities
prob_HH = HH_count / number_of_throws
prob_HT = HT_count / number_of_throws
prob_TH = TH_count / number_of_throws
prob_TT = TT_count / number_of_throws
print(f'Probability of HH: {prob_HH}')
print(f'Probability of HT: {prob_HT}')
print(f'Probability of TH: {prob_TH}')
print(f'Probability of TT: {prob_TT}')

# Bar chart for frequencies
outcomes = ["HH", "HT", "TH", "TT"]
counts = [HH_count, HT_count, TH_count, TT_count]
plt.bar(outcomes, counts, color=['blue', 'orange', 'green', 'red'])
plt.title("Frequencies of Outcomes in Coin Tosses")
plt.xlabel("Outcomes")
plt.ylabel("Frequency")
plt.show()


