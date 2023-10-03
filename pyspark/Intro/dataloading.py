from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("data loading").getOrCreate()
# data = spark.read.parquet("../Data/userdata1.parquet")
# data.show()
with open("../Data/userdata.avsc") as file:
    avroSchema = file.read()
data_avro = spark.read \
            .format("avro") \
            .option("avroSchema", avroSchema) \
            .load("../Data/userdata1.avro")
data_avro.show()
