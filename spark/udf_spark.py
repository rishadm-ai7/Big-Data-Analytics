from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType
#we importing this to convert
from pyspark.sql.functions import udf

def age_category(age):
    if age>=20 and age<=40:
        return 'Young'
    elif age>40 and age<50:
        return 'MidAge'
    else :
        return 'Old'

spark = SparkSession.builder.appName("UDF").getOrCreate()

df = spark.read.options(sep =';',header=True).csv("/home/rishad/inputdata/spark/people.csv")

df.show()
df.printSchema()

df = df.withColumn('age1',df['age'].cast(IntegerType()))

age_udf = udf(age_category)
#registering the function

df1 = df.withColumn('age Category',age_udf(df['age1']))
df1.show()
