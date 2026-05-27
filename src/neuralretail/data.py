import pandas as pd
import numpy as np


def generate_data():

    df = pd.DataFrame({
        "sales": np.random.randint(100, 500, 100),
        "customers": np.random.randint(10, 100, 100)
    })

    return df