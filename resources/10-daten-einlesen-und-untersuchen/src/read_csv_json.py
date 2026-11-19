"""Read small CSV and JSON data sets with an explicit schema."""

from pathlib import Path
from tempfile import TemporaryDirectory
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType


def main():
    spark = SparkSession.builder.master("local[2]").appName("ReadSources").getOrCreate()
    try:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "people.csv").write_text("name,age\nAda,36\nGrace,29\nLinus,17\n", encoding="utf-8")
            (root / "people.json").write_text('{"name":"Ada","age":36}\n{"name":"Grace","age":29}\n', encoding="utf-8")
            schema = StructType([StructField("name", StringType()), StructField("age", IntegerType())])
            csv_df = spark.read.option("header", True).schema(schema).csv(str(root / "people.csv"))
            json_df = spark.read.schema(schema).json(str(root / "people.json"))
            csv_df.printSchema()
            csv_df.show()
            json_df.show()
    finally:
        spark.stop()


if __name__ == "__main__":
    main()
