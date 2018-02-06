# spark_twitter
It's a playground for using Twitter streaming api and trying Apache Spark.

Answering the question: What are the current most popular hashtags in tweets mentioning Toronto?

1. Run *twitter_client.py*: it creates a socket on *localhost:50001* and listens. 
2. Run *spark_client.py*: it connects to *localhost:50001*. 
*twitter_client.py* connects to Twitter API and takes tweets where *toronto* is mentioned and then sends hashtags of the tweet to spark stream.

With the help of Spark hashtags are being counted (constantly updating as tweets come) and 20 the most popular tags are displayed in console as a data frame.
