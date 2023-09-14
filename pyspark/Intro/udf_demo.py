
from __future__ import annotations
from pyspark.sql import SparkSession
from typing import TYPE_CHECKING
from pyspark.sql.functions import udf
from pyspark.sql.types import FloatType

# creating a spark session.
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()


def hike(current_salary) -> float:
    """ revise the salary according to constant
    :param current_salary:
    :return:
    """
    return current_salary * 1.10


simpleData = (("James", "Sales", 3000), ("Michael", "Sales", 4600), ("Robert", "Sales", 4100),
              ("Maria", "Finance", 3000), ("James", "Sales", 3000), ("Scott", "Finance", 3300),
              ("Jen", "Finance", 3900),
              ("Jeff", "Marketing", 3000), ("Kumar", "Marketing", 2000), ("Saif", "Sales", 4100)
              )

columns = ["employee_name", "department", "salary"]
df = spark.createDataFrame(data=simpleData, schema=columns)
hike_fn = udf(hike, FloatType())
# if the datatype mismatched then it will fill with null values.
df = df.withColumn("after-Hike", hike_fn(df['salary']))
df.show()
