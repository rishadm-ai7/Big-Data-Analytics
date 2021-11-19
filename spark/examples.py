from pyspark import SparkContext
sc=SparkContext("local","Word Count")
input = sc.textFile('hdfs://localhost:9000/hadoop_46/wordcnt.txt')

word_count = input.flatMap(lambda l:(l.split(' '))).map(lambda l:(l,1)).reduceByKey(lambda k,v:k+v).sortByKey()

for i in word_count.collect():
    print(i)
