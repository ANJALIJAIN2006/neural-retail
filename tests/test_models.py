from src.neuralretail.train import train_models

def test_training_runs():
    metrics = train_models()
    assert 0 <= metrics["churn_auc"] <= 1
    assert metrics["demand_mape"] >= 0