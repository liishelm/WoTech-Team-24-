#Version 1
import pandas as pd
import matplotlib.pyplot as plt 
pokemon_df=pd.read_csv('/content/Pokemon.csv')
#1How many Pokémons are with 'Type 1' == Water as a % of total?
percentage_of_water = round(pokemon_df['Type 1'].value_counts()['Water']/len(pokemon_df)*100)
print(f'There is {percentage_of_water}% of water type pokemons.')
#2What is the maximum 'Speed' value? What is the minimum 'Speed' value? What is the difference between max and min 'Speed'?
max_speed = pokemon_df['Speed'].max()
min_speed = pokemon_df['Speed'].min()
dif_speed = max_speed - min_speed
print(f'The maximum speed of pokemons is {max_speed} and the minimum speed is {min_speed}. The difference between them is {dif_speed}.')
#3Filter the DataFrame to include only the Pokémon with 'Speed' >= 80. How many Pokémon meet this criterion? Display this DataFrame using your preferred visualization method.
speed_df = pokemon_df[pokemon_df['Speed']>=80]
count = speed_df.value_counts().sum()
print(f'The amount of pokemons with speed over 80 is {count}.')
plt.hist(speed_df['Speed'], bins=10, color = 'yellow', edgecolor='black', alpha=0.7)
plt.xlabel('Speed')
plt.ylabel('Frequency')
plt.title('Distribution of Speed')
plt.axvline(speed_df['Speed'].mean(), color='black', linestyle='dashdot', linewidth=1)
plt.show()
#4 Find Pokémon with the longest name (excluding spaces)? What is this pokemons name?
lengths_without_spaces = pokemon_df['Name'].str.replace(' ', '').str.len()
longest_name_index = lengths_without_spaces.idxmax()
longest_name = pokemon_df.loc[longest_name_index, 'Name']
print(f"The longest pokemon name is {longest_name}")


#Version 2
import pandas as pd
import matplotlib.pyplot as plt 
pokemon_df=pd.read_csv('/content/Pokemon.csv')
#1How many Pokémons are with 'Type 1' == Water as a % of total?
water_pokemons = len(pokemon_df[pokemon_df['Type 1'] == 'Water'])
water_percentage = (water_pokemons / total_pokemon) * 100
print(f"Percentage of pokemon with 'Type 1' == Water is:  {water_percentage:.1f}%")
#Percentage of pokemon with 'Type 1' == Water is:  14.0%
#2What is the maximum 'Speed' value? What is the minimum 'Speed' value? What is the difference between max and min 'Speed'?
max_speed = pokemon_df['Speed'].max()
print(f"The maximum speed is: {max_speed}")
#The maximum speed is: 180
min_speed = pokemon_df['Speed'].min()
print(f"The minimum speed is: {min_speed}")
#The minimum speed is: 5
speed_difference = max_speed - min_speed
print(f"Difference between max and min speed is: {speed_difference}")
#Difference between max and min speed is: 175
#3Filter the DataFrame to include only the Pokémon with 'Speed' >= 80. How many Pokémon meet this criterion? Display this DataFrame using your preferred visualization method.
speed_80_pokemon_df = pokemon_df.query('Speed >= 80')
num_speed_80_pokemon = speed_80_pokemon_df.shape[0]
print(f"A total of {num_speed_80_pokemon} pokemons meet this criteria")
#A total of 296 pokemons meet this criteria
speed_counts = speed_80_pokemon_df['Speed'].value_counts().sort_index()
plt.hist(speed_80_pokemon_df['Speed'], color='gold', edgecolor='black', alpha=0.9)
plt.xlabel('Speed')
plt.ylabel('Number of Pokemon')
plt.title('This is a visualization of Pokemon with "Speed" >= 80.')
plt.grid(axis='y', linestyle='dashed', alpha=0.5, color='red')
plt.show()
