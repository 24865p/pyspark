from pyspark.sql.functions import col, sum

from session import spark

# ------ Uniqueness ------ #
file_path = "data/employee_uniqueness.csv"

# PySpark DataFrame으로 CSV 파일 로드
df = spark.read.csv(file_path, header=True, inferSchema=True)

df.show()


# 모든 columns의 중복 값이 있는 row 표시
df.exceptAll(df.dropDuplicates()).show()

# 'name' 또는 'age' columnes에 중복된 값이 있는 row 표시
df.exceptAll(df.dropDuplicates(["name", "age"])).show()
# ----------- #

# ----- Completeness ------ #
# PySpark로 누락된 값/ null값 처리
completeness_path = "data/employee_completeness.csv"
com_df = spark.read.csv(completeness_path, header=True, inferSchema=True)
com_df.select(  # 누락 값 찾기
    *(sum(col(c).isNull().cast("int")).alias(c) for c in com_df.columns)
).show()
