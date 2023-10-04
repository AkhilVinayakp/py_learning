from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator

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

# modeling -> predicting price.
lr = LinearRegression(featuresCol='feature_input', labelCol='price', regParam=0.03)
lr_model = lr.fit(train)

# evaluation
model_eval = RegressionEvaluator(labelCol='price', predictionCol="prediction", metricName="rmse")
predictions = lr_model.transform(test)
rmse = model_eval.evaluate(predictions)
print("Rmse score ", rmse)

print("Test dataset (sample) with prediction >>")
predictions.show(10)

# prediction on new datapoint
inp_test_data = spark.createDataFrame([(7000, 4, 1, 2, 1)], ['area', 'bedrooms', 'stories', 'parking', 'bathrooms'])
print("Sample input data point")
inp_test_data.show()

inp_features = vector_assembler.transform(inp_test_data)
print("data with feature vector")
inp_features.show()

print("data point with prediction")
pred = lr_model.transform(inp_features)
pred.show()
