# creating the spark_ context
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("alpha").getOrCreate()
data = spark.sparkContext.textFile("../Data/loan_data_set.csv")
# cells = data.flatMap(lambda line: line.split(" "))
# table_data = cells.map(lambda line: line.split(","))
header = data.first()  # gathering the header part
# filtering out the headers from the original rdd
data = data.filter(lambda line: line != header)
data = data.map(lambda line: line.split(","))

personal_header = ("Loan_ID", "Gender", "Married", "Dependents", "Education", "Self_Employed", "ApplicantIncome",
                   "Co-applicantIncome", "Credit_History", "Property_Area")
load_header = ("Loan_ID", "Loan Amount", "Loan_Amount_Term", "Loan_Status")

personal_data_header = spark.sparkContext.parallelize([personal_header])
personal_data = data.map(lambda val: (val[0], val[1], val[2], val[3], val[4], val[5], val[6], val[7]))
loan_data = data.map(lambda val: (val[0], val[8], val[9], val[12]))
personal_data = personal_data_header.union(personal_data)
loan_data_header = spark.sparkContext.parallelize([load_header])
loan_data = loan_data_header.union(loan_data)
print("created loan_data with total count :", loan_data.count())
print("created personal_data with total count :", personal_data.count())
# loan_data.saveAsTextFile('file:///d:/spark_temp/loan_data.txt')
# personal_data.saveAsTextFile("file:///d:/spark_temp/personal_data.txt")
