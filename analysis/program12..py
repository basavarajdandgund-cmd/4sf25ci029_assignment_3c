#12. Working with Text Data
#Create a Pandas Series with 5 random text strings. Convert all the strings to uppercase.
import pandas as pd
import numpy as np
s = pd.Series(['apple', 'mango', 'orange', 'grapes', 'banana'])

print("Original Series:")
print(s)

print("Uppercase Series:")
print(s.str.upper())