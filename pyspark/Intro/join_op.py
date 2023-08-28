from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("PairedRDD_join").setMaster("local")
sc = SparkContext(conf=conf)
rdd1 = sc.parallelize(["cat1, 123", "cat2, 43", "cat3, 53"])
rdd2 = sc.parallelize(["cat1, 91", "cat2, 63", "cat5, 33"])
rdd3 = sc.parallelize(["r1,12", "r2,90", "r3,89"])

rdd1 = rdd1.map(lambda line: line.split(",")).map(lambda list_: (list_[0], int(list_[1])))
rdd2 = rdd2.map(lambda line: line.split(",")).map(lambda list_: (list_[0], int(list_[1])))
rdd3 = rdd3.map(lambda line: line.split(",")).map(lambda list_: (list_[0], int(list_[1])))

# joining
# rdd 1 and rdd 2; both contains similar keys
rdd_temp = rdd1.join(rdd2)
print("joined [sim keys] :", rdd_temp.collect())
# $ joined [sim keys] : [('cat1', (123, 91)), ('cat2', (43, 63))]

# check for any difference in ordering
rdd_temp = rdd2.join(rdd1)
print("joined [sim keys, order changed] :", rdd_temp.collect())
# $ joined [sim keys, order changed] : [('cat1', (91, 123)), ('cat2', (63, 43))]

# counting
print("key count :", rdd_temp.countByKey())
print("value count :", rdd_temp.countByValue())
py_dict = rdd_temp.collectAsMap()
print("rdd as dict:", py_dict)


# joining 2 RDDs having no similar keys
rdd_temp = rdd1.join(rdd3)
print("joined [no sim keys] :", rdd_temp.collect())
# $ out: will be empty

# performing right outer join
rdd_temp = rdd1.rightOuterJoin(rdd2)
print(f"Right outer join of rdd left {rdd1.collect()} and right {rdd2.collect()} [sim keys] :{rdd_temp.collect()}")

# performing left outer join
rdd_temp = rdd1.leftOuterJoin(rdd2)
print(f"Left outer join of rdd left {rdd1.collect()} and right {rdd2.collect()} [sim keys] :{rdd_temp.collect()}")
