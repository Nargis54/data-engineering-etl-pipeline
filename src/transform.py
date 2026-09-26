import pandas as pd


def clean_employees(df):
    df = df.copy()

    df["Employee_Name"] = df["Employee_Name"].str.strip()
    df["Department"] = df["Department"].str.strip()
    df["City"] = df["City"].str.strip()

    df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

    df = df.drop_duplicates()

    return df


def clean_orders(df):
    df = df.copy()

    df["Product"] = df["Product"].str.strip()
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
    df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

    df = df.drop_duplicates()

    return df


def transform_orders(df):
    df = df.copy()

    df["Average_Unit_Price"] = (
        df["Amount"] / df["Quantity"]
    ).round(2)

    return df
