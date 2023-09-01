from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("EDA_TEST").getOrCreate()
emp = [
    (1, "smith", -1, "2018", "10", "M", 3000),
    (2, "Rose", 1, "2010", "20", "F", 4000),
    (3, "Jones", 2, "2005", "10", "M", 6000)
]
emp_cols = ["emp_id", "name", "superior_emp_id", "year_joined", "emp_dept_id", "gender", "salary"]
empDF = spark.createDataFrame(data=emp, schema=emp_cols)
empDF.printSchema()
empDF.show()