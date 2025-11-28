import os

import pandas as pd


def load_to_dataframe(dir_path: str, file: str) -> pd.DataFrame:
    csv_path = os.path.join(dir_path, file)
    df = pd.read_csv(csv_path)
    return df
