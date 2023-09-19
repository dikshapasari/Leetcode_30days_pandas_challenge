import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sorted = employee['salary'].unique()
    sorted = pd.Series(sorted).sort_values(ascending =False)

    if len(sorted)>=2:

        secondhighest= sorted.iloc[1]
        result_df= pd.DataFrame({'SecondHighestSalary': [secondhighest]})
        return result_df
    else:
        result_df= pd.DataFrame({'SecondHighestSalary': [None]})
        return result_df
