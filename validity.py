"""데이터 유효성 강화. 'Occupation' column의 유효성 확인 => 미리 정의된 유효한 직업이어야 함"""

from pyspark.sql.functions import col, when

from session import spark

file_path = "data/validity.csv"

df = spark.read.csv(file_path, header=True, inferSchema=True)

valid_occupations = [
    "Engineer",
    "Teacher",
    "Software Developer",
    "Accountant",
    "Marketing Manager",
]

# 유효한 Occupation에 속하지 않는 row 제외
df_valid = (
    df.withColumn(
        "Occupation",
        when(col("Occupation").isin(valid_occupations), col("Occupation")).otherwise(
            None
        ),
    )
    .filter(col("Occupation").isNotNull())
    .show()
)
