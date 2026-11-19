"""Training demonstration; run as a regular Python application."""

from pyspark.sql import SparkSession
from pyspark.sql import functions as F


def main():
    spark = (SparkSession.builder.master("local[2]")
             .appName("PySparkTraining").getOrCreate())
    try:
        numbers = spark.range(0, 100)
        print("Initial partitions:", numbers.rdd.getNumPartitions())
        transformed = numbers.filter(F.col("id") % 2 == 0).withColumn("double_id", F.col("id") * 2)
        print("Transformations have been defined; no count action yet.")
        transformed.explain(mode="formatted")
        print("Count action:", transformed.count())
        print("Repartitioned:", transformed.repartition(4).rdd.getNumPartitions())
    finally:
        spark.stop()


if __name__ == "__main__":
    main()
