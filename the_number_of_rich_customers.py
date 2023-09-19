import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    #to get all the customer_id where amount>500
    #then find the unique customerIds and count them.
    filtered_df = store[store['amount']>500]
    richcount= len(filtered_df['customer_id'].unique())
    result= pd.DataFrame({'rich_count': [richcount]})
    return result
