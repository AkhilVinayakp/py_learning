from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext

from utils.initializer import init_spark_objs
from utils.data_loader import file_loader
from pyspark.sql.functions import regexp_replace
import matplotlib.pyplot as plt
import seaborn as sns

spark, sc = init_spark_objs()
data = file_loader(spark, path="../Data/Iris.csv")

# preprocessing the iris dataset
# TASK
# 1. remove id
# 2. remove 'iris' word in the Species column
data = data.drop('Id')
data = data.withColumn('Species', regexp_replace('Species', 'Iris-', ""))
print(">> changed Species col \n")
data.select('Species').show(5)
print(">>Sample Data")
data.show(3)

# generating EDA graphs
# - data distribution

