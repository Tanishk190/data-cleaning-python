import pandas as pd
import numpy as np

df=pd.read_csv("C:\\Users\\radad\\OneDrive\\Desktop\\Pandas\\practice\\dirty2.csv")
print(df.head())
print(df.shape)
df.columns = df.columns.str.strip()
print(df.isnull().sum())

df=df.fillna({'Branch': 'Not Assigned',
              'Physics': 0,
              'Chemistry': 0,
              'Maths': 0,
              'Computer': 0,
              })
print("\nDataFrame after filling null values:")
print(df.head())
df.to_csv("C:\\Users\\radad\\OneDrive\\Desktop\\Pandas\\practice\\cleaned_data2.csv", index=False)
print("\nTotal null values in the DataFrame after filling:")
print(df.isnull().sum())