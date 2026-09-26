from extract import extract_employees, extract_orders
from transform import clean_employees, clean_orders, transform_orders
from load import load_data


def run_pipeline():
    print("Starting ETL Pipeline...")

    # Extract
    employees = extract_employees()
    orders = extract_orders()
    print("Data extraction completed.")

    # Transform
    employees = clean_employees(employees)
    orders = clean_orders(orders)
    orders = transform_orders(orders)
    print("Data transformation completed.")

    # Load
    load_data(employees, "employees_processed.csv")
    load_data(orders, "orders_processed.csv")

    print("ETL Pipeline completed successfully.")


if __name__ == "__main__":
    run_pipeline()
