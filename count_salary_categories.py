import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    #create dataframe for each category using the condition
    # find the length of the series that will give us the count
    lowsal_df = accounts[accounts['income']<20000]
    #lowsalaccounts = len(lowsal_df['account_id'])
    avgsal_df = accounts[(accounts['income']>= 20000) & (accounts['income']<= 50000)]
    #avgsalaccounts= len(avgsal_df['account_id'])
    highsal_df = accounts[accounts['income']>50000]
    #highsalaccounts= len(highsal_df['account_id'])
     
    result_df= pd.DataFrame({'category':['High Salary','Low Salary','Average Salary'],'accounts_count':[len(highsal_df['account_id']),len(lowsal_df['account_id']),len(avgsal_df['account_id'])]})
    return result_df 
