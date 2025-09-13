

import pandas as pd

# L
df1 = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Name": ["Ali", "Sara", "Ahmed", "Zara"]
})


df2 = pd.DataFrame({
    "ID": [2, 3, 4, 5],
    "Department": ["IT", "HR", "Finance", "Marketing"]
})


print("Inner Join:\n", pd.merge(df1, df2, on="ID", how="inner"), "\n")


print("Left Join:\n", pd.merge(df1, df2, on="ID", how="left"), "\n")


print("Right Join:\n", pd.merge(df1, df2, on="ID", how="right"), "\n")

print("Outer Join:\n", pd.merge(df1, df2, on="ID", how="outer"), "\n")


df3 = pd.DataFrame({
    "Emp_ID": [1, 2, 3],
    "Salary": [50000, 60000, 70000]
})
print("Different column names:\n", pd.merge(df1, df3, left_on="ID", right_on="Emp_ID"), "\n")

