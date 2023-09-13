# outlier detection
from utils.initializer import init_spark_objs
from utils.data_loader import file_loader
from utils.dataparser import parse_continuous_fields

spark, sc = init_spark_objs(appname="OLD")
df = file_loader(spark, path="../Data/sample_data.csv")
df.show(5, truncate=False)
# getting the continuous fields
