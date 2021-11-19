from pyspark.sql import SparkSession
from pyspark.sql.functions import split,explode

spark = SparkSession.builder.appName("word count").getOrCreate()

lines = spark.readStream.format("socket").option("host","localhost").option("port",9999).load()

words = lines.select(explode(split(lines.value," ")).alias('word'))

word_count = words.groupBy('word').count()

query = word_count.writeStream.outputMode("complete").format("console").start()
#format console cuz we have to print it in terminal thats why

query.awaitTermination()


