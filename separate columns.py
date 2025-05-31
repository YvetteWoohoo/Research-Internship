import pandas as pd

# Load the CSV file
df = pd.read_csv('/Users/yvette/Desktop/film/production companies.csv')

# Split the 'production_companies' column into multiple columns
split_companies = df['production_companies'].str.split(', ', expand=True)

# Rename the columns
split_companies.columns = [f'pro_com_{i+1}' for i in range(split_companies.shape[1])]

# Concatenate the original DataFrame with the new columns
result_df = pd.concat([df['id'], split_companies], axis=1)

# Save the result to a new CSV file
result_df.to_csv('separated_production_companies.csv', index=False)