# Local PySpark development environment

This branch provides a Visual Studio Code Dev Container for Python and Apache Spark (PySpark) in **local mode**.

## Requirements

- Docker-compatible container runtime
- Visual Studio Code with the **Dev Containers** extension

## Start

1. Clone the repository and check out `training-pyspark`.
2. Open the repository folder in Visual Studio Code.
3. Run **Dev Containers: Reopen in Container** from the Command Palette.
4. Wait for the image build and the `postCreateCommand` to finish.
5. Run `python pyspark-environment/smoke_test.py` in the integrated terminal.

The container includes Python 3.12, OpenJDK 17 and PySpark 4.0.1. It does not require an external Spark cluster, Hadoop installation, or cloud service.

## Local Spark

Use `SparkSession.builder.master("local[*]")` to run Spark locally. This starts Spark execution in the container and uses the available CPU cores. It is suitable for training and small data sets, but it is not a distributed multi-node cluster.

To use an interactive Python shell, run `pyspark --master 'local[*]'`.

## Notes

- The training examples and exercises can be added later; this directory only provides the environment and a smoke test.
- The original `training` branch is not changed.
- Docker must have sufficient memory available; at least 4 GB is recommended for the training environment.
