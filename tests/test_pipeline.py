
import pandas as pd

from src.preprocessing import clean_customer_data


def test_pipeline_with_synthetic_data():

    # Create artificial customer records
    df = pd.DataFrame({
        "Customer_ID": ["C001", "C002", "C002", "C003"],
        "Employment_Status": [
            " employed ",
            "unemployed",
            "unemployed",
            " self-employed "
        ],
        "Delinquent_Account": [0, 1, 1, 2]
    })

    # Run preprocessing
    cleaned = clean_customer_data(df)

    # Check duplicate removal
    assert len(cleaned) == 2

    # Check target values
    assert cleaned["Delinquent_Account"].isin([0, 1]).all()

    # Check category cleaning
    assert "Employed" in cleaned["Employment_Status"].values
    assert "Self-Employed" in cleaned["Employment_Status"].values

    # Check original data is unchanged
    assert len(df) == 4


def test_empty_dataset():

    df = pd.DataFrame({
        "Customer_ID": [],
        "Delinquent_Account": []
    })

    cleaned = clean_customer_data(df)

    assert cleaned.empty
