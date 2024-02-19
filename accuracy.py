from pyspark.sql.functions import col, when

from session import spark

# ------ accuracy ------ #
file_path = "data/accuracy.csv"

df = spark.read.csv(file_path, header=True, inferSchema=True)

df.show()

# 정확도 체크 : Age column의 오류 식별 처리 (잘못된 값 -50 -> NULL)
df_cleaned = df.withColumn(
    "Age",
    when((col("Age").cast("int").isNull()) | (col("Age") <= 0), None).otherwise(
        col("Age")
    ),
)

df_cleaned.show()
