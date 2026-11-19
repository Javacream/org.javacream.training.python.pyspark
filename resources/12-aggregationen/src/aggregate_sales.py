"""Training demonstration; run as a regular Python application."""

from pyspark.sql import SparkSession
from pyspark.sql import functions as F


def main():
    spark = (SparkSession.builder.master("local[2]")
             .appName("PySparkTraining").getOrCreate())
    try:
        sales = spark.createDataFrame([("books", 12.5), ("food", 5.0), ("books", 7.5), ("food", 8.0)], ["category", "amount"])
        summary = (sales.groupBy("category")
                   .agg(F.count("*").alias("transactions"), F.round(F.sum("amount"), 2).alias("total"))
                   .orderBy(F.desc("total")))
        summary.show()
    finally:
        spark.stop()


if __name__ == "__main__":
    main()
