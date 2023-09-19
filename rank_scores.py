import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores_sorted = scores.sort_values(by='score', ascending=False)

    # Calculate the rank based on 'score'
    scores_sorted['rank'] = scores_sorted['score'].rank(method='dense', ascending=False).astype(int)

    # Reorder columns and reset the index
    result_df = scores_sorted[['score', 'rank']].reset_index(drop=True)

    return result_df

