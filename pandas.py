# From a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Paris', 'London']
}

df = pd.DataFrame(data)

# Creating a Series
ages = pd.Series([25, 30, 35])
# Selecting a column
df['Name']

# Selecting multiple columns
df[['Name', 'City']]

# Selecting a row by index
df.iloc[0]         # First row
df.loc[1]          # Row with index label 1

# Conditional selection
df[df['Age'] > 30]
# Add new column
df['Salary'] = [50000, 60000, 70000]

# Modify existing column
df['Age'] = df['Age'] + 1

# Drop a column
df = df.drop('Salary', axis=1)

# Rename columns
df = df.rename(columns={'Name': 'Full Name'})
