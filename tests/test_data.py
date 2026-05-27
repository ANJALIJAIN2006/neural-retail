from src.neuralretail.data import make_synthetic_retail_data

def test_data_shape():
    df = make_synthetic_retail_data(100)
    assert len(df) == 100
    assert "sales" in df.columns