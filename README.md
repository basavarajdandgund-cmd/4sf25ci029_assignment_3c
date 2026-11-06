# Pandas DataFrame Operations and Data Analysis

## 📌 Project Overview

This project contains 13 Python programs demonstrating various operations using the **Pandas and NumPy libraries**. It covers DataFrame creation, data manipulation, aggregation, merging, MultiIndex operations, applying functions, and working with text data.

The main objective of this project is to understand how to create, manipulate, analyze, and transform data using Python.

## 🎯 Objectives

- Create and manipulate Pandas DataFrames.
- Perform mathematical operations on DataFrames.
- Handle missing values (NaN).
- Perform data aggregation using GroupBy.
- Merge multiple DataFrames.
- Understand MultiIndex DataFrames.
- Apply functions and lambda expressions.
- Perform string operations using Pandas.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Library 1:** Pandas
- **Library 2:** NumPy
- **Platform:** Jupyter Notebook / Google Colab / VS Code

## 📦 Required Libraries

Install the required libraries using:

```bash
pip install pandas numpy
```

Import the libraries in Python:

```python
import pandas as pd
import numpy as np
```

## 📚 Programs Included

### 1. DataFrame Creation and Product Calculation
- Create a Pandas DataFrame with 3 columns and 5 rows.
- Fill the DataFrame with random integers.
- Add a new column containing the product of the first two columns.

### 2. Row-wise and Column-wise Sum
- Create a DataFrame with 3 columns and 4 rows.
- Calculate the sum of each row.
- Calculate the sum of each column.

### 3. Handling Missing Values (NaN)
- Create a DataFrame with 3 columns and 5 rows.
- Introduce some missing values (NaN).
- Replace missing values with the mean of their respective columns.

### 4. Dropping Missing Values
- Create a DataFrame with 4 columns and 6 rows.
- Introduce some NaN values.
- Remove all rows containing at least one missing value.

### 5. Data Aggregation Using GroupBy
- Create a DataFrame with Category and Value columns.
- Generate random categories (A, B, C) and integer values.
- Group the data by Category.
- Calculate the sum and mean of each category.

### 6. Grouping Products by Category
- Create a DataFrame with Product, Category, and Sales columns.
- Generate random product and sales data.
- Group the DataFrame by Category.
- Calculate the total sales for each category.

### 7. Merging DataFrames
- Create two Pandas DataFrames with a common column.
- Merge both DataFrames using the common column.
- Display the merged DataFrame.

### 8. MultiIndex DataFrame
- Create a DataFrame with a hierarchical (MultiIndex) index.
- Perform basic indexing and slicing operations.
- Access specific rows and groups of data.

### 9. MultiIndex with Category and SubCategory
- Create a MultiIndex DataFrame using Category and SubCategory.
- Fill the DataFrame with random values.
- Calculate the sum of values for each Category and SubCategory combination.

### 10. Applying Functions
- Create a DataFrame with 3 columns and 5 rows.
- Apply a function to double every value in the DataFrame.
- Display the original and modified DataFrames.

### 11. Applying Lambda Functions
- Create a DataFrame with 3 columns and 6 rows.
- Use a lambda function to calculate the sum of existing columns.
- Store the result in a new column.

### 12. Working with Text Data – Uppercase
- Create a Pandas Series containing 5 text strings.
- Convert all strings into uppercase using the `.str.upper()` method.

### 13. Extracting Characters from Strings
- Create a Pandas Series containing 5 text strings.
- Extract the first three characters from each string using `.str[:3]`.

## 📖 Concepts Covered

| No. | Concept | Pandas Methods |
|---|---|---|
| 1 | DataFrame Creation | `pd.DataFrame()` |
| 2 | Mathematical Operations | `sum()` |
| 3 | Missing Value Handling | `fillna()`, `mean()` |
| 4 | Removing Missing Values | `dropna()` |
| 5 | Data Aggregation | `groupby()`, `agg()` |
| 6 | Grouping and Summation | `groupby()`, `sum()` |
| 7 | Merging DataFrames | `merge()` |
| 8 | MultiIndex | `MultiIndex`, `loc[]` |
| 9 | Hierarchical Indexing | `groupby()` |
| 10 | Applying Functions | `apply()` |
| 11 | Lambda Functions | `lambda` |
| 12 | String Operations | `str.upper()` |
| 13 | String Slicing | `str[:3]` |

## ▶️ How to Run the Programs

1. Install Python on your computer.
2. Install Pandas and NumPy libraries.
3. Open Jupyter Notebook, Google Colab, or VS Code.
4. Open the Python notebook or program files.
5. Execute each program individually.
6. Observe the output generated for each operation.

## 📂 Project Structure

```text
Pandas-Assignment/
│
├── README.md
│
├── Program_01_Product.ipynb
├── Program_02_Row_Column_Sum.ipynb
├── Program_03_Fill_NaN.ipynb
├── Program_04_Drop_NaN.ipynb
├── Program_05_Data_Aggregation.ipynb
├── Program_06_GroupBy_Sales.ipynb
├── Program_07_Merging.ipynb
├── Program_08_MultiIndex.ipynb
├── Program_09_Category_SubCategory.ipynb
├── Program_10_Apply_Function.ipynb
├── Program_11_Lambda_Function.ipynb
├── Program_12_Uppercase_Text.ipynb
└── Program_13_String_Extraction.ipynb
```

*Note: The above filenames are suggested. You can change them according to your actual assignment files.*

## ✅ Expected Learning Outcomes

After completing these 13 programs, students will be able to:

- Understand Pandas DataFrame and Series operations.
- Perform data cleaning and preprocessing.
- Handle missing data efficiently.
- Analyze and summarize datasets.
- Combine and merge datasets.
- Work with hierarchical indexing.
- Apply built-in and custom functions.
- Perform text manipulation and string extraction.

## 👨‍💻 Conclusion

This assignment provides practical knowledge of Pandas and NumPy libraries in Python. By completing these 13 programs, we gain a better understanding of data manipulation, data aggregation, missing value handling, indexing, and text processing.

These concepts are useful for Data Analysis, Data Science, and real-world data processing applications.

---

**Project:** Pandas DataFrame Operations and Data Analysis  
**Language:** Python  
**Libraries:** Pandas, NumPy  
**Total Programs:** 13

**Thank You!**
