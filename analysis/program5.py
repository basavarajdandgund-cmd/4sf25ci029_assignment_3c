#5. Data Aggregation 
#Create a Pandas DataFrame with 2 columns: 'Category' and 'Value'. Fill the 'Category' column with random categories ('A', 'B', 'C') and the 'Value' column with random integers. Group the DataFrame by 'Category' and compute the sum and mean of 'Value' for each category.
import pandas as pd
import numpy as np
df = pd.DataFrame({
    'Category': np.random.choice(['A', 'B', 'C'], size=10),
    'Value': np.random.randint(10, 100, size=10)
})

print(df)

result = df.groupby('Category')['Value'].agg(['sum', 'mean'])

print(result)