
import pandas as pd


# Step 1: DataFrame banao
data = {
    'Name': ['Ali', 'Sara', 'Usman', 'Ayesha', 'Bilal'],
    'Math': [78, 45, 90, 56, 66],
    'Science': [88, 67, 95, 49, 72],
    'English': [92, 50, 85, 60, 70]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Step 2: Basic Analysis
# Har student ka total aur average
df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)
df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1)

print("\nWith Total & Average:")
print(df)

# Topper ka pata lagao
topper = df.loc[df['Total'].idxmax()]
print("\nTopper Student:")
print(topper)

# Har subject ka highest aur lowest marks
print("\nSubject-wise Highest Marks:")
print(df[['Math', 'Science', 'English']].max())

print("\nSubject-wise Lowest Marks:")
print(df[['Math', 'Science', 'English']].min())

# Har subject ka average
print("\nSubject-wise Average Marks:")
print(df[['Math', 'Science', 'English']].mean())
