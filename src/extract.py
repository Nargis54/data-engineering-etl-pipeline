import pandas as pd


def extract_employees():
    return pd.read_csv("data/raw/employees.csv")


def extract_orders():
    return pd.read_csv("data/raw/orders.csv")


if __name__ == "__main__":
    employees = extract_employees()
    orders = extract_orders()

    print("Employees Data:")
    print(employees.head())

    print("\nOrders Data:")
    print(orders.head())
