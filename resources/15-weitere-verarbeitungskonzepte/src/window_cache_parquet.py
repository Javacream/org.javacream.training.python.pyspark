"""Window functions, caching, and Parquet output in a temporary directory."""

from tempfile import TemporaryDirectory
from pyspark.sql import SparkSession, Window
from pyspark.sql import functions as F


def main():
    spark = SparkSession.builder.master("local[2]").appName("WindowAndParquet").getOrCreate()
    try:
        sales = spark.createDataFrame([("books", "A", 15), ("books", "B", 25), ("food", "C", 8)], ["category", "item", "amount"])
        window = Window.partitionBy("category").orderBy(F.desc("amount"))
        ranked = sales.withColumn("rank", F.row_number().over(window)).cache()
        ranked.show()
        print("Cached rows:", ranked.count())
        with TemporaryDirectory() as directory:
            path = directory + "/ranked.parquet"
            ranked.write.mode("overwrite").parquet(path)
            spark.read.parquet(path).show()
        ranked.unpersist()
    finally:
        spark.stop()


if __name__ == "__main__":
    main()
