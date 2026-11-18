
import pandas as pd

from src.preprocessing import clean_customer_data


def test_pipeline_with_synthetic_data():

    df = pd.DataFrame({
        "Customer_ID": ["C001", "C002", "C002", "C003", "C004"],
        "Employment_Status": [
            " employed ",
            "unemployed",
            "unemployed",
            " self-employed ",
            "student"
        ],
        "Delinquent_Account": [0, 1, 1, 1, 2]
    })

    cleaned = clean_customer_data(df)

    # Check duplicate removal and invalid target removal
    assert len(cleaned) == 3

    # Check valid target values
    assert cleaned["Delinquent_Account"].isin([0, 1]).all()

    # Check category cleaning
    assert "Employed" in cleaned["Employment_Status"].values
    assert "Self-Employed" in cleaned["Employment_Status"].values

    # Check original data remains unchanged
    assert len(df) == 5


def test_empty_dataset():

    df = pd.DataFrame({
        "Customer_ID": [],
        "Delinquent_Account": []
    })

    cleaned = clean_customer_data(df)

    assert cleaned.empty
