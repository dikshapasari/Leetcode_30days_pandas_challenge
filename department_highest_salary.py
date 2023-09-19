import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    #rename column, join the tables.
    employee.rename(columns={'id':'employeeId', 'name':'Employee', 'salary': 'Salary'}, inplace=True)
    department.rename(columns={'id':'departmentId', 'name':'Department'}, inplace=True)

    merged_df = pd.merge(employee, department, on='departmentId', how= 'left')
    #find the max salary from each department, then find the employees who match those.
    max_salaries= merged_df.groupby('Department')['Salary'].transform('max')
    result_df= merged_df[merged_df['Salary'] == max_salaries]
    return result_df[['Department','Employee','Salary']]
    
    
