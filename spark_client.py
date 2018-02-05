from pyspark import SparkContext
from pyspark import SparkConf

from pyspark.streaming import StreamingContext

# Create a local StreamingContext with two working thread
# and batch interval of 1 second
conf = SparkConf().setMaster("local[2]").setAppName("SparkTwitter")
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")

ssc = StreamingContext(sc, 1)
# setting a checkpoint to allow RDD recovery
ssc.checkpoint("checkpoint_TwitterApp")

# Create a DStream that will connect to hostname:port, like localhost:50001
hashtag = ssc.socketTextStream("localhost", 50001)

tags_RDD = hashtag.map(lambda word: (word, 1)).reduceByKey(lambda x, y: x + y)

tags_RDD.pprint()

ssc.start()
ssc.awaitTermination()