import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    total_count= len(delivery['delivery_id'])
    filtered_df= delivery[delivery['order_date']== delivery['customer_pref_delivery_date']]
    count_immediate= len(filtered_df['delivery_id'])
    imm_percentage= (count_immediate/total_count)*100
    result_df= pd.DataFrame({'immediate_percentage':[round(imm_percentage,2)]})
    return result_df
