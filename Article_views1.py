import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views.rename(columns={'author_id': 'id'}, inplace= True)
    data= views[views['id'] == views['viewer_id']]
    result = data[['id']].drop_duplicates().sort_values(by= 'id', ascending = True)
    return result
