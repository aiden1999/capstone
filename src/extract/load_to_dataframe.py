import os

import pandas as pd


def load_to_dataframe(dir_path: str, file: str) -> pd.DataFrame:
    csv_path = os.path.join(dir_path, file)
    try:
        df = pd.read_csv(csv_path)
    except Exception as e:
        raise Exception(f"Error: {e}")
    return df
