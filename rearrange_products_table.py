import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
     # Use the melt function to unpivot the table and keep only non-null values
    melted_df = pd.melt(products, id_vars=['product_id'], var_name='store', value_name='price')
    
    # Drop rows where price is null
    result_df = melted_df.dropna(subset=['price'])
    
    return result_df
