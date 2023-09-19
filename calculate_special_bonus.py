import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    condition = ((employees['employee_id'])%2 !=0 ) & (employees['name'].str.startswith('M')== False) 
    employees['bonus'] = employees['salary'] * condition.astype(int)

    return employees[['employee_id','bonus']].sort_values(by= 'employee_id', ascending = True)
