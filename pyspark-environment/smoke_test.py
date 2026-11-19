"""Verify that local PySpark can create and process a DataFrame."""

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = (
    SparkSession.builder
    .appName("PySparkEnvironmentSmokeTest")
    .master("local[2]")
    .config("spark.ui.enabled", "false")
    .getOrCreate()
)

try:
    people = spark.createDataFrame(
        [("Ada", 36), ("Grace", 29), ("Linus", 17)],
        ["name", "age"],
    )
    adults = people.filter(F.col("age") >= 18)
    adults.show()
    assert adults.count() == 2
    print("Local PySpark environment is working.")
finally:
    spark.stop()
