from pyspark.sql import SparkSession, Window
from pyspark.sql.functions import lag, lead
spark = SparkSession.builder.appName('Spark_windowing').getOrCreate()


simpleData = (("James", "Sales", 3000), ("Michael", "Sales", 4600), ("Robert", "Sales", 4100),
              ("Maria", "Finance", 3000), ("James", "Sales", 3000), ("Scott", "Finance", 3300), ("Jen", "Finance", 3900),
              ("Jeff", "Marketing", 3000), ("Kumar", "Marketing", 2000), ("Saif", "Sales", 4100)
              )

columns = ["employee_name", "department", "salary"]
df = spark.createDataFrame(data=simpleData, schema=columns)
df.printSchema()
df.show(truncate=False)

# applying windowing with lead and log functionalities
windowed_data = Window.partitionBy("department").orderBy("Salary")
df = df.withColumn("lag_val", lag(df['salary'], offset=2).over(windowed_data))

df = df.withColumn("lead_value", lead(df['salary'], offset=1).over(windowed_data))
df.show()


