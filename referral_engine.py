import pandas as pd

lawyers_df = pd.read_csv("lawyers.csv")

def get_lawyers(city, category):
    filtered = lawyers_df[
        (lawyers_df["City"] == city) &
        (lawyers_df["Firm Specialty"] == category)
    ]

    return filtered["Law Firm Name"].tolist()