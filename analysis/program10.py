#10. Applying Functions Create a Pandas DataFrame with 3 columns and 5 rows filled with random integers. Apply a function that doubles the values of the DataFrame.
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randint(1, 10, size=(5, 3)),
                  columns=['A', 'B', 'C'])

print("Original DataFrame:")
print(df)

result = df.map(lambda x: x * 2)

print("Doubled DataFrame:")
print(result)