import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    type_one = patients['conditions'].str.contains(r'\bDIAB1', case = False)
    output = patients[type_one]
    return output
