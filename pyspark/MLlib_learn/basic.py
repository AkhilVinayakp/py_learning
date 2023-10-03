from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
spark = SparkSession.builder.appName("ML").getOrCreate()
data = spark.read.csv("../Data/Housing.csv", inferSchema=True, header=True)
print("sample data")
data.show()
# exploring the schema
data.printSchema()
data.describe().toPandas().transpose()

features = ['area', 'bedrooms', 'stories', 'parking', 'bathrooms']
target = "price"

vector_assembler = VectorAssembler(inputCols=features, outputCol="feature_input")
pdf = vector_assembler.transform(data)
print("entire dataset with transformation.")
pdf.show()
# showing only selected features along with the target
pdf.select(['feature_input', 'price']).show()
# filtering out.
data_flt = pdf.select(['feature_input', 'price'])

# splitting the dataset for training and testing
train, test = data_flt.randomSplit([0.8, 0.2], seed=42)

# printing sample
print("sample training data")
train.show(5)
print("sample testing data")
test.show(5)
