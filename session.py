from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("data-quality-checks").getOrCreate()

# Reduce logging
spark.sparkContext.setLogLevel("WARN")
