import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customers.rename(columns={'id':'customerId', 'name': 'Customers'}, inplace =True)
    orders.rename(columns={'id': 'orderId', 'customerId': 'customerId'}, inplace = True)
    merged_data= pd.merge(customers, orders, on='customerId', how= 'left')
    result= merged_data[pd.isnull(merged_data['orderId'])]
    return result[['Customers']]
