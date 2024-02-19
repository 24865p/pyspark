"""타임스탬프를 검사하고, 기준에 따라 최신 데이터인지 확인"""

from pyspark.sql.functions import col, current_date

from session import spark

file_path = "data/timeliness.csv"
df = spark.read.csv(file_path, header=True, inferSchema=True)

df.show()

# 지난 7일 이내에 발생한 이벤트 필터링
days_threshold = 7
df_timely = df.filter((current_date() - col("EventDate")).cast("int") <= days_threshold)
df_timely.show()
