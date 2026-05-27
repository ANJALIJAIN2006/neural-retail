import pandas as pd

def build_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    feature_cols = [c for c in out.columns if c.startswith("f")]
    out["rfm_score"] = (out["f0"] - out["f1"] + out["f2"]).rank(pct=True)
    out["sales_lag_1"] = out["sales"].shift(1).fillna(out["sales"].mean())
    out["sales_roll_7"] = out["sales"].rolling(7, min_periods=1).mean()
    out["sales_roll_30"] = out["sales"].rolling(30, min_periods=1).mean()
    return out, feature_cols + ["rfm_score", "sales_lag_1", "sales_roll_7", "sales_roll_30"]