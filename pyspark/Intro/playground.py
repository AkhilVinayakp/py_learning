# sample play ground file for testing functions
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

conf = SparkConf().setAppName("Playground").setMaster("local")
sc = SparkContext(conf=conf)
spark = SparkSession(sparkContext=sc)

# reduceByKey
rdd = sc.parallelize([("alpha", 1.34), ("gamma", 2.5), ("omega", 5.2), ("alpha", 4.34), ("gamma", 3.5)])

# finding the average value for each key
rdd_avg = rdd.reduceByKey(lambda x, y: (x + y) / 2)
# here x represent the intermediate value and the y the next value to process in the
# current key processing
print(rdd_avg.collect())
print("current partition :", rdd_avg.getNumPartitions())
# sorting
# task: sort the rdd_avg based on the key
sorted_avg_rdd = rdd_avg.sortByKey(ascending=True, numPartitions=3)
print("sorted :", sorted_avg_rdd.collect(), "  partitions: ", sorted_avg_rdd.getNumPartitions())
# sorting based on the average value
sorted_avg_rdd = rdd_avg.sortBy(keyfunc=lambda x: x[1], ascending=False, numPartitions=1)
print(sorted_avg_rdd.collect())

# task
# perform square of values only
rdd_sq = sorted_avg_rdd.mapValues(lambda val: val ** 2)
print("powered :", rdd_sq.collect())

# find the average of values on all keys

# collect values only
val_rdd = rdd_sq.map(lambda x: x[1])
# reduce
total_sum = val_rdd.reduce(lambda x, y: x + y)
len_val = rdd_sq.count()
print(total_sum/len_val)
