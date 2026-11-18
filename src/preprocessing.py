
import pandas as pd


def clean_customer_data(df):
    """
    Basic cleaning and validation of customer data.
    Does not modify the original dataset.
    """

    data = df.copy()

    # Remove duplicate records
    data = data.drop_duplicates()

    # Remove unnecessary spaces from column names
    data.columns = data.columns.str.strip()

    # Handle inconsistent employment status labels
    if "Employment_Status" in data.columns:
        data["Employment_Status"] = (
            data["Employment_Status"]
            .astype("string")
            .str.strip()
            .str.title()
        )

    # Validate target variable
    if "Delinquent_Account" in data.columns:
        data = data[
            data["Delinquent_Account"].isin([0, 1])
        ].copy()

    return data


if __name__ == "__main__":
    print("Geldium preprocessing module loaded successfully.")
