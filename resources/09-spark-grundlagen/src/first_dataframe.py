"""Training demonstration; run as a regular Python application."""

from pyspark.sql import SparkSession
from pyspark.sql import functions as F


def main():
    spark = (SparkSession.builder.master("local[2]")
             .appName("PySparkTraining").getOrCreate())
    try:
        print("Spark version:", spark.version)
        print("Spark master:", spark.sparkContext.master)
        people = spark.createDataFrame([("Ada", 36), ("Grace", 29), ("Linus", 17)], ["name", "age"])
        people.show()
        print("Number of records:", people.count())
        print("Columns:", people.columns)
    finally:
        spark.stop()


if __name__ == "__main__":
    main()
