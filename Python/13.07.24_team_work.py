#Task 1: Create a bar chart that shows the count of transactions for each unique value in the 'Gender' column (including NaN values). - **easy**


import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv('/content/transaction_dataset.csv')
df = dataset['Gender'].value_counts(dropna=False).reset_index()
df.columns = ['Gender', 'Count']
df['Gender'] = df['Gender'].astype(str)
plt.bar(df['Gender'], df['Count'], color=('blue', 'green', 'orange'))
plt.title('Count of Transactions by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()


#Task 2: Create a horizontal bar chart that shows the top 5 most frequent names in the DataFrame,based on the 'name' column. 
#(First, create a grouped DataFrame (name_df), then filter it using iloc, and finally create the visualization.) -medium

dataset['Name'].value_counts().reset_index()
name_df = dataset['Name'].value_counts().reset_index()
name_df.columns = ['Name','Count']
name_df = name_df.iloc[:5]
plt.barh(name_df['Name'], name_df['Count'], color='green')
plt.gca().invert_yaxis()
plt.title('Top 5 Most Frequent Names')
plt.xlabel('Count')
plt.ylabel('Name')
plt.show()


#Task 3: Create a filtered DataFrame that includes Category == 'Clothing' and Gender == 'M'. How many rows are there in this filtered DataFrame? 
#Format the result as follows: The filtered DataFrame has XXXX rows. - hard

is_clothing = dataset['Category'] == 'Clothing'
is_male = dataset['Gender'] == 'M'
df2 = dataset[is_clothing & is_male]
print(f"The filtered DataFrame has {df2.shape[0]} rows.")

