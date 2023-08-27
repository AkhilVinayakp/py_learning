from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

conf = SparkConf().setAppName("pairedRDDSample").setMaster("local")
sc = SparkContext(conf=conf)
spark = SparkSession(sc)

rdd = sc.textFile("iris.csv")
header = rdd.first()
rdd = rdd.filter(lambda line: line != header)

# creating paired rdd
rdd_split = rdd.map(lambda x: x.split(","))
available_classes = rdd_split.map(lambda cols: cols[5])
paired_rdd = rdd_split.map(lambda cols: (cols[5], (float(cols[1]), float(cols[2]))))
print("Available classes :", available_classes.distinct().collect())
grp_rdd = paired_rdd.groupByKey()
# print(paired_rdd.collect())
print(grp_rdd.collect())
print("number of groups formed:", grp_rdd.count())
mnc = grp_rdd.map(lambda item: (item[0], list(item[1])))
print(mnc.collect())
