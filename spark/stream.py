from pyspark import SparkContext

from pyspark.streaming import StreamingContext

sc = SparkContext("local[2]","Streaming sample")

ssc = StreamingContext(sc,4)

lines = ssc.socketTextStream('localhost',9999)
#we use netcat it has port no. 9999

word = lines.flatMap(lambda l:(l.split(' '))).map(lambda l:(l,1)).reduceByKey(lambda k,v:k+v)

word.pprint()
#printing the dstream

ssc.start()
#start streaming

ssc.awaitTermination()
#kill streaming

