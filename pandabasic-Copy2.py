{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "08928896",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0     4\n",
      "1     8\n",
      "2    15\n",
      "3    16\n",
      "4    23\n",
      "5    42\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "#Q1. Create a Pandas Series that contains the following data: 4, 8, 15, 16, 23, and 42. Then, print the series.\n",
    "import pandas as pd\n",
    "\n",
    "# Create the Series\n",
    "data = [4, 8, 15, 16, 23, 42]\n",
    "series = pd.Series(data)\n",
    "\n",
    "# Print the Series\n",
    "print(series)\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "82bf2041",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0     1\n",
      "1     3\n",
      "2     5\n",
      "3     7\n",
      "4     9\n",
      "5    11\n",
      "6    13\n",
      "7    15\n",
      "8    17\n",
      "9    19\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "#Q2Create a variable of list type containing 10 elements in it, and apply pandas.Series function on the\n",
    "#variable print it.\n",
    "import pandas as pd\n",
    "\n",
    "# Create a list with 10 elements\n",
    "data_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]\n",
    "\n",
    "# Convert the list to a Pandas Series\n",
    "series = pd.Series(data_list)\n",
    "\n",
    "# Print the Series\n",
    "print(series)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "0af383d7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "     Name  Age  Gender\n",
      "0   Alice   25  Female\n",
      "1     Bob   30    Male\n",
      "2  Claire   27  Female\n"
     ]
    }
   ],
   "source": [
    "#Q3. Create a Pandas DataFrame that contains the following data:\n",
    "import pandas as pd\n",
    "\n",
    "# Create a dictionary containing the data\n",
    "data = {\n",
    "    'Name': ['Alice', 'Bob', 'Claire'],\n",
    "    'Age': [25, 30, 27],\n",
    "    'Gender': ['Female', 'Male', 'Female']\n",
    "}\n",
    "\n",
    "# Create the Pandas DataFrame\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "# Print the DataFrame\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "3389b9cf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Series:\n",
      " 0    10\n",
      "1    20\n",
      "2    30\n",
      "3    40\n",
      "dtype: int64\n",
      "\n",
      "DataFrame:\n",
      "       Name  Age  Salary\n",
      "0    Alice   25   50000\n",
      "1      Bob   30   60000\n",
      "2  Charlie   35   70000\n",
      "3    David   40   80000\n"
     ]
    }
   ],
   "source": [
    "#Q4 What is ‘DataFrame’ in pandas and how is it different from pandas.series? Explain with an example.\n",
    "'''A DataFrame in pandas is a 2-dimensional labeled data structure, similar to a table in SQL or an Excel spreadsheet. It consists of rows and columns, where:\n",
    "\n",
    "Rows represent observations or records.\n",
    "Columns represent features or variables.'''\n",
    "import pandas as pd\n",
    "\n",
    "# Creating a Series\n",
    "data_series = pd.Series([10, 20, 30, 40])\n",
    "\n",
    "# Creating a DataFrame\n",
    "data_dict = {\n",
    "    'Name': ['Alice', 'Bob', 'Charlie', 'David'],\n",
    "    'Age': [25, 30, 35, 40],\n",
    "    'Salary': [50000, 60000, 70000, 80000]\n",
    "}\n",
    "data_frame = pd.DataFrame(data_dict)\n",
    "\n",
    "# Print the Series\n",
    "print(\"Series:\\n\", data_series)\n",
    "\n",
    "# Print the DataFrame\n",
    "print(\"\\nDataFrame:\\n\", data_frame)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "842ca1ce",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      Name Department   Age        Salary\n",
      "0    Alice         HR  25.0  55000.000000\n",
      "1      Bob         IT  30.0  66000.000000\n",
      "2  Charlie         IT  35.0  69666.666667\n",
      "3    David         HR   NaN  88000.000000\n"
     ]
    }
   ],
   "source": [
    "'''Q5. What are some common functions you can use to manipulate data in a Pandas DataFrame? Can\n",
    "you give an example of when you might use one of these functions?\n",
    "Ans-- head() / tail() \n",
    "info()\n",
    "describe()\n",
    "shape\n",
    "drop()'''\n",
    "import pandas as pd\n",
    "\n",
    "# Sample DataFrame\n",
    "data = {\n",
    "    'Name': ['Alice', 'Bob', 'Charlie', 'David'],\n",
    "    'Department': ['HR', 'IT', 'IT', 'HR'],\n",
    "    'Age': [25, 30, 35, None],\n",
    "    'Salary': [50000, 60000, None, 80000]\n",
    "}\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "# Fill missing salary with mean\n",
    "df['Salary'].fillna(df['Salary'].mean(), inplace=True)\n",
    "\n",
    "# Calculate average salary by department\n",
    "avg_salary = df.groupby('Department')['Salary'].mean()\n",
    "\n",
    "# Apply 10% raise to all salaries\n",
    "df['Salary'] = df['Salary'].apply(lambda x: x * 1.1)\n",
    "\n",
    "print(df)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "d9e1da3f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Q6. Which of the following is mutable in nature Series, DataFrame, Panel?\\nAns -- Series – Mutable\\nDataFrame – Mutable\\nPanel – Mutable (although Panels are deprecated in Pandas 1.0 and later, replaced by MultiIndex DataFrames)\\nExplanation:\\nMutable means the object can be changed after its creation.\\nBoth Series and DataFrame allow modifications to their data, index, and structure.\\nPanels (before deprecation) were also mutable, but they were rarely used compared to DataFrames.\\nFor multidimensional data, MultiIndex DataFrames are now recommended over Panels.'"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''Q6. Which of the following is mutable in nature Series, DataFrame, Panel?\n",
    "Ans -- Series – Mutable\n",
    "DataFrame – Mutable\n",
    "Panel – Mutable (although Panels are deprecated in Pandas 1.0 and later, replaced by MultiIndex DataFrames)\n",
    "Explanation:\n",
    "Mutable means the object can be changed after its creation.\n",
    "Both Series and DataFrame allow modifications to their data, index, and structure.\n",
    "Panels (before deprecation) were also mutable, but they were rarely used compared to DataFrames.\n",
    "For multidimensional data, MultiIndex DataFrames are now recommended over Panels.'''\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "c3648db7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      Name  Age  Salary\n",
      "0    Alice   25   50000\n",
      "1      Bob   30   60000\n",
      "2  Charlie   35   70000\n",
      "3    David   40   80000\n"
     ]
    }
   ],
   "source": [
    "'''Q7. Create a DataFrame using multiple Series. Explain with an example.'''\n",
    "import pandas as pd\n",
    "\n",
    "# Create Series for each column\n",
    "names = pd.Series(['Alice', 'Bob', 'Charlie', 'David'])\n",
    "ages = pd.Series([25, 30, 35, 40])\n",
    "salaries = pd.Series([50000, 60000, 70000, 80000])\n",
    "\n",
    "# Create DataFrame by combining Series\n",
    "df = pd.DataFrame({\n",
    "    'Name': names,\n",
    "    'Age': ages,\n",
    "    'Salary': salaries\n",
    "})\n",
    "\n",
    "# Print the DataFrame\n",
    "print(df)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ce59a364",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
