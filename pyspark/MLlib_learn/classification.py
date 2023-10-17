from pyspark.mllib.regression import LabeledPoint
from pyspark.sql import SparkSession
from pyspark.mllib.classification import LogisticRegressionWithLBFGS

spark = SparkSession.builder.appName("Test").getOrCreate()
sparkContext = spark.sparkContext
iris_data = sparkContext.textFile("../Data/iris.csv")
header = iris_data.first() # taking only the header inside the csv file. used to filter out the line from further
# processing
iris_data = iris_data.filter(lambda line: line != header)
# splitting the rdd based on ,
iris_data_split = iris_data.map(lambda x: x.split(','))
# converting the type of each valuei
iris_data_conv = iris_data_split.map(lambda x:(float(x[1]),float(x[2]), float(x[3]), float(x[4]), x[5]))
# performing label encoding using the index
categories = iris_data_conv.map(lambda x: x[4]).distinct().collect()
mapping = {category: index for index, category in enumerate(categories)}
iris_data_labled = iris_data_conv.map(lambda x: LabeledPoint(mapping[x[4]],x[:4]))
training, testing = iris_data_labled.randomSplit([0.7, 0.3], seed=42)

# creating the model
# model = LogisticRegressionWithLBFGS.train(iris_data_labled, iterations=10, numClasses=3)
# model.predict(iris_data_conv.map(lambda x: x[:4])).take(20)
model = LogisticRegressionWithLBFGS.train(training, iterations=10, numClasses=3)

# testing
test_features = testing.map(lambda x: x.features)
test_labels = testing.map(lambda x: x.label)
prediction = model.predict(test_features)

print("printing first 10 prediction")
meta_header = ['Features', 'actual', 'predicted']
reverse_mapping = {value:key for key,value in mapping.items()}
actual_labels = test_labels.map(lambda label: reverse_mapping.get(int(label))).take(10)
predicted_labels = prediction.map(lambda label: reverse_mapping.get(int(label))).take(10)