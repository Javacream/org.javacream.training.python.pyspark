"""Optional JDBC example; requires an external database and its JDBC driver JAR."""

import os
from pyspark.sql import SparkSession


def main():
    url = os.getenv("TRAINING_JDBC_URL")
    table = os.getenv("TRAINING_JDBC_TABLE")
    driver = os.getenv("TRAINING_JDBC_DRIVER")
    if not all([url, table, driver]):
        print("Optional demo: set TRAINING_JDBC_URL, TRAINING_JDBC_TABLE and TRAINING_JDBC_DRIVER.")
        print("Also add the matching JDBC driver JAR to Spark's classpath.")
        return
    spark = SparkSession.builder.master("local[2]").appName("JDBCRead").getOrCreate()
    try:
        data = (spark.read.format("jdbc").option("url", url)
                .option("dbtable", table).option("driver", driver).load())
        data.printSchema()
        data.show(10)
    finally:
        spark.stop()


if __name__ == "__main__":
    main()
