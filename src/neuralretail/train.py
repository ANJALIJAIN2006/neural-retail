from joblib import dump
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import mean_absolute_percentage_error, roc_auc_score
from sklearn.model_selection import train_test_split

from .data import make_synthetic_retail_data
from .features import build_features
from .config import MODELS_DIR

def train_models():
    df = make_synthetic_retail_data()
    df, feature_cols = build_features(df)

    X = df[feature_cols].fillna(0)
    y_churn = df["churn"]
    y_sales = df["sales"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y_churn, test_size=0.2, random_state=42, stratify=y_churn
    )
    _, _, y_sales_train, y_sales_test = train_test_split(
        X, y_sales, test_size=0.2, random_state=42
    )

    clf = RandomForestClassifier(n_estimators=300, random_state=42)
    reg = RandomForestRegressor(n_estimators=300, random_state=42)

    clf.fit(X_train, y_train)
    reg.fit(X_train, y_sales_train)

    churn_auc = roc_auc_score(y_test, clf.predict_proba(X_test)[:, 1])
    demand_mape = mean_absolute_percentage_error(y_sales_test, reg.predict(X_test))

    dump(clf, MODELS_DIR / "churn_model.joblib")
    dump(reg, MODELS_DIR / "demand_model.joblib")

    return {"churn_auc": churn_auc, "demand_mape": demand_mape}

if __name__ == "__main__":
    print(train_models())