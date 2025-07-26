import pandas as pd
import numpy as np

# Step 1: Load CSV
df = pd.read_csv("dirty_with_inf_nan_duplicates.csv")

# Step 2: Remove duplicates
df = df.drop_duplicates()

# Step 3: Replace inf/-inf with NaN
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# Step 4: Fill NaN values with the mean of each column
# Option 1: Drop rows with NaNs
#df = df.dropna()
print("Total nan values before filling:")
print(df.isnull().sum())  # Print the number of NaN values per column
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Working_Hours'] = df['Working_Hours'].fillna(df['Working_Hours'].mean())
print("\nAfter filling NaN values:")
print(df.isnull().sum())  # Print the number of NaN values per column after filling
# Save the cleaned data
df.to_csv("cleaned_data.csv", index=False)
