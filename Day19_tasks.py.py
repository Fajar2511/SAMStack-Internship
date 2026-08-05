import numpy as np
import pandas as pd

print("TASK 1: Data Cleaning")

data = {
    'Emp_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Ali', 'Sara', 'Ahmad', 'Zainab', 'Bilal', 'Fatima', 'Usman', 'Ayesha', 'Hassan', 'Mariam'],
    'Salary': [12000, 34990, np.nan, np.nan, 6700, 7800, 5600, 77000, 45009, np.nan], 
    'Department': ['Engineering', 'HR', 'Engineering', np.nan, 'Sales', 'Engineering', 'HR', 'Sales', 'Tech', np.nan],  
    'Experience': [2, 5, 3, 4, 1, 6, 2, 7, 4, 3],
    'Join_Date': ['2020-4-30', '2021-5-12', '2022-1-20', '2020-11-05', '2023-3-15', 
                  '2021-8-22', '2022-9-10', '2020-2-28', '2023-6-01', '2021-12-19'] 
}
df = pd.DataFrame(data) 
print("Original Data:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

salary_mean = df['Salary'].mean() 
df.loc[:, 'Salary'] = df['Salary'].fillna(salary_mean)

df.loc[:, 'Department'] = df['Department'].fillna("Unassigned")
df.loc[:, 'Join_Date'] = pd.to_datetime(df['Join_Date'])

print("Cleaned Data:")
print(df)
print("Join_Date Data Type:", df['Join_Date'].dtype)

print(" 2: GroupBy")

avg_salary = df.groupby('Department')['Salary'].mean()
print("Average Salary per Department:")
print(avg_salary)
agg_result = df.groupby('Department').agg({
    'Salary': ['mean', 'max'],
    'Experience': 'sum'
})
print("Multiple Aggregations:")
print(agg_result)

print("TASK 3: Merging")
df_employees = pd.DataFrame({
    'Emp_ID': [1, 2, 3, 4, 5],
    'Name': ['Ali', 'Sara', 'Ahmad', 'Zainab', 'Bilal'],
    'Dept_ID': [101, 102, 103, 101, 104] 
})

df_departments = pd.DataFrame({
    'Dept_ID': [101, 102, 103],
    'Dept_Name': ['Engineering', 'Sales', 'HR'],
    'Location': ['Lahore', 'Karachi', 'Islamabad']
})

inner_merge = pd.merge(df_employees, df_departments, on='Dept_ID', how='inner')
print("Inner Join Result:")
print(inner_merge)

left_merge = pd.merge(df_employees, df_departments, on='Dept_ID', how='left')
print("Left Join Result:")
print(left_merge)