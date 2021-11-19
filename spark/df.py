from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("spark session example").getOrCreate()

emp = spark.read.options(sep=',',header = True).csv("/home/rishad/inputdata/hive/emp.csv")

emp.show()

emp_count = emp.count()
print(emp_count)

emp.createTempView("emp")
spark.sql("select * from emp where name=='joe'").show()
