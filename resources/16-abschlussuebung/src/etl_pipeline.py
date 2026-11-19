"""End-to-end ETL demonstration using generated CSV/JSON and Parquet output."""

from pathlib import Path
from tempfile import TemporaryDirectory
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType


def main():
    spark = SparkSession.builder.master("local[2]").appName("TrainingETL").getOrCreate()
    try:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "people.json").write_text('{"person_id":1,"name":"Ada"}\n{"person_id":2,"name":"Grace"}\n', encoding="utf-8")
            (root / "orders.csv").write_text("person_id,amount\n1,20.5\n1,10.0\n2,8.0\n2,\n", encoding="utf-8")
            person_schema = StructType([StructField("person_id", IntegerType()), StructField("name", StringType())])
            order_schema = StructType([StructField("person_id", IntegerType()), StructField("amount", DoubleType())])
            people = spark.read.schema(person_schema).json(str(root / "people.json"))
            orders = spark.read.option("header", True).schema(order_schema).csv(str(root / "orders.csv"))
            totals = (orders.filter(F.col("amount").isNotNull())
                      .groupBy("person_id").agg(F.round(F.sum("amount"), 2).alias("total")))
            result = people.join(totals, "person_id", "left").fillna({"total": 0.0}).orderBy("person_id")
            result.show()
            output = str(root / "output.parquet")
            result.write.mode("overwrite").parquet(output)
            print("Read back the ETL result:")
            spark.read.parquet(output).show()
    finally:
        spark.stop()


if __name__ == "__main__":
    main()
