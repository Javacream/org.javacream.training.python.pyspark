"""Training demonstration; run as a regular Python application."""

from pyspark.sql import SparkSession
from pyspark.sql import functions as F


def main():
    spark = (SparkSession.builder.master("local[2]")
             .appName("PySparkTraining").getOrCreate())
    try:
        people = spark.createDataFrame([("Ada", 36), ("Grace", None), ("Linus", 17)], ["name", "age"])
        result = (people
                  .withColumn("age", F.coalesce(F.col("age"), F.lit(0)))
                  .withColumn("category", F.when(F.col("age") >= 18, "adult").otherwise("minor"))
                  .filter(F.col("age") >= 18)
                  .select("name", "age", "category"))
        result.show()
    finally:
        spark.stop()


if __name__ == "__main__":
    main()
