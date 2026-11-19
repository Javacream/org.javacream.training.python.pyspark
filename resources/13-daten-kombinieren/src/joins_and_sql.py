"""Training demonstration; run as a regular Python application."""

from pyspark.sql import SparkSession
from pyspark.sql import functions as F


def main():
    spark = (SparkSession.builder.master("local[2]")
             .appName("PySparkTraining").getOrCreate())
    try:
        people = spark.createDataFrame([(1, "Ada"), (2, "Grace"), (3, "Linus")], ["person_id", "name"])
        orders = spark.createDataFrame([(1, 20.0), (1, 12.0), (2, 8.0)], ["person_id", "amount"])
        joined = people.join(orders, on="person_id", how="left")
        joined.show()
        joined.createOrReplaceTempView("people_orders")
        spark.sql("""SELECT name, COALESCE(SUM(amount), 0) AS total
                     FROM people_orders GROUP BY name ORDER BY name""").show()
    finally:
        spark.stop()


if __name__ == "__main__":
    main()
