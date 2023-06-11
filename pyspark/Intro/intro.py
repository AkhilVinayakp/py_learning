# setting up the session in pyspark
from pyspark.sql import SparkSession

# setting up the spark session
spark_session = SparkSession.builder.appName(name="test").getOrCreate()
print(f"Current Session: ", spark_session)