import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    
    # Remove duplicates and sort the salaries in descending order
    sorted_salaries = employee['salary'].unique()
    sorted_salaries = pd.Series(sorted_salaries).sort_values(ascending=False)
    
    # Check if there are at least n distinct salaries
    if len(sorted_salaries) >= N:
        nth_highest_salary = sorted_salaries.iloc[N - 1]
        result_df = pd.DataFrame({'Nth_Highest_Salary': [nth_highest_salary]})
        return result_df
    else:
        result_df = pd.DataFrame({'Nth_Highest_Salary': [None]})
        return result_df
    
