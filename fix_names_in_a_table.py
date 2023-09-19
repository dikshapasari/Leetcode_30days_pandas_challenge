import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name']= users['name'].str[0].str.upper() + users['name'].str[1:].str.lower()
    return users[['user_id','name']].sort_values(by = 'user_id', ascending= True)
