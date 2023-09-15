from pyspark.sql import SparkSession, Window
from pyspark.sql.functions import rank, row_number, dense_rank, ntile, percent_rank
spark = SparkSession.builder.appName('Spark_windowing').getOrCreate()


simpleData = (("James", "Sales", 3000), ("Michael", "Sales", 4600), ("Robert", "Sales", 4100),
              ("Maria", "Finance", 3000), ("James", "Sales", 3000), ("Scott", "Finance", 3300), ("Jen", "Finance", 3900),
              ("Jeff", "Marketing", 3000), ("Kumar", "Marketing", 2000), ("Saif", "Sales", 4100)
              )

columns = ["employee_name", "department", "salary"]
df = spark.createDataFrame(data=simpleData, schema=columns)
df.printSchema()
df.show(truncate=False)

windowed_data = Window.partitionBy("department").orderBy("Salary")

# applying function over window
df = df.withColumn("Row number", row_number().over(windowed_data))
df = df.withColumn("Shallow Rank", rank().over(windowed_data))
df = df.withColumn("Dense Rank", dense_rank().over(windowed_data))
df = df.withColumn("Percentage", percent_rank().over(windowed_data))
df = df.withColumn("nth tile", ntile(n=4).over(windowed_data))
df.show(truncate=False)