from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, count


spark = SparkSession.builder \
    .appName("ETLDataProcessing") \
    .master("local[*]") \
    .getOrCreate()


orders = spark.read.csv(
    "data/raw/orders.csv",
    header=True,
    inferSchema=True
)

print("Orders Data:")
orders.show()


product_summary = orders.groupBy("Product").agg(
    sum("Amount").alias("Total_Sales"),
    count("Order_ID").alias("Order_Count")
)

print("Product-wise Sales Summary:")
product_summary.show()


spark.stop()
