# Data Engineering ETL Pipeline

## Project Overview

This project implements an ETL pipeline using Python, Pandas, SQL and PySpark.

The pipeline extracts employee and order data, cleans and transforms the data, and loads processed datasets for analysis.

## Technologies

- Python
- Pandas
- SQL
- PySpark
- NumPy

## ETL Process

Extract → Transform → Load

### Extract

Employee and order data are extracted from CSV files using Python and Pandas.

### Transform

Data is cleaned, duplicates are removed, data types are converted, and average unit price is calculated.

### Load

The transformed data is saved as processed CSV files.

### PySpark Processing

PySpark is used to calculate product-wise total sales and order count.

## Dataset

- Employee data
- Order data

## Project Structure

```text
data-engineering-etl-pipeline/
├── data/
│   ├── raw/
│   │   ├── employees.csv
│   │   └── orders.csv
│   └── processed/
│       ├── employees_processed.csv
│       └── orders_processed.csv
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── pipeline.py
│   └── spark_processing.py
├── sql/
│   ├── queries.sql
│   └── analysis.sql
├── screenshots/
├── requirements.txt
├── .gitignore
├── README.md
└── LICENSE
```

## Output

The ETL pipeline generates processed employee and order datasets in the `data/processed` folder.

The processed order data includes the calculated `Average_Unit_Price` field.

## SQL Analysis

SQL queries are included to analyze employee salary data and product-wise sales.

- Department-wise average salary
- Product-wise total sales

## Project Status

The ETL pipeline has been successfully executed using Python, Pandas and PySpark.
