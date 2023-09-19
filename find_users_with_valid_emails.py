import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r'^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$'
    valid_check = users['mail'].str.contains(pattern)
    output = users[valid_check]
    return output
