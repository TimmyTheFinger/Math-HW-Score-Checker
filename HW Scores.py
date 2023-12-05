import pandas as pd

# Load the data
df = pd.read_csv('scores.csv')

# Replace '-' with '0' as some imcomplete assignments have it as -/# instead of 0/#.
df['Score'] = df['Score'].replace('-', '0 / 0')

# Split 'Score' column into 'Score' and 'Total'
df[['Score', 'Total']] = df['Score'].str.split(' / ', expand=True)

# Calculate the total score
df['Score'] = df['Score'].astype(float)
df['Total'] = df['Total'].astype(float)
df['Percentage'] = (df['Score'] / df['Total']) * 100

# Print the total score
print("Total Score: ", df['Score'].sum())
print("Total Possible Score: ", df['Total'].sum())
print("Percentage: ", (df['Score'].sum() / df['Total'].sum()) * 100)

