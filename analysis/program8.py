#8. MultiIndex DataFrame Create a Pandas DataFrame with a MultiIndex (hierarchical index). Perform some basic indexing and slicing operations on the MultiIndex DataFrame.
import pandas as pd
import numpy as np
index = pd.MultiIndex.from_tuples([
    ('A', 1), ('A', 2), ('B', 1), ('B', 2)
], names=['Category', 'Number'])

df = pd.DataFrame({'Value': [10, 20, 30, 40]}, index=index)

print("Complete DataFrame:")
print(df)

print("Access category A:")
print(df.loc['A'])

print("Access a specific row:")
print(df.loc[('B', 1)])

print("Slice category A to B:")
print(df.loc['A':'B'])