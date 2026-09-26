# Data Engineering ETL Pipeline

## Project Overview

This project implements an ETL pipeline using Python, Pandas, SQL and PySpark.

The pipeline extracts employee and order data, cleans and transforms the data, and loads the processed datasets for further analysis.

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
Data is cleaned by removing duplicates, trimming text values, converting data types, and creating an average unit price.

### Load
The transformed data is saved as processed CSV files.

### PySpark Processing
PySpark is used to process order data and generate product-wise sales and order-count summaries.

## Dataset

- Employee data
- Order data

## Project Structure

```text
data-engineering-etl-pipeline/
├── data/
│   ├── raw/
│   └── processed/
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
