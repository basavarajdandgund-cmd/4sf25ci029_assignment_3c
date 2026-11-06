#6. Create a Pandas DataFrame with 3 columns: 'Product', 'Category', and 'Sales'. Fill the DataFrame with random data. Group the DataFrame by 'Category' and compute the total sales for each category.
import pandas as pd
import numpy as np
df = pd.DataFrame({
    'Product': np.random.choice(['Pen', 'Book', 'Bag'], size=8),
    'Category': np.random.choice(['Stationery', 'Accessories'], size=8),
    'Sales': np.random.randint(100, 1000, size=8)
})

print(df)

result = df.groupby('Category')['Sales'].sum()

print("Total sales by category:")
print(result)