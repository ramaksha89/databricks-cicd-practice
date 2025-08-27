# example_notebook.py (exported version) #new comment # kotha comment malli add chedhaam
#adding a new sample comment line
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

# Batch example: Load sample CSV
df = spark.read.csv("/databricks-datasets/learning-spark-v2/people/people-10m.csv", header=True, inferSchema=True)

df_transformed = df.filter(df.age > 30).select("name", "age")
df_transformed.show(5)

# Streaming example (later extension)
# stream_df = spark.readStream.format("rate").option("rowsPerSecond", 10).load()
# transformed = stream_df.withColumnRenamed("value", "my_value")
# query = transformed.writeStream.format("console").start()
