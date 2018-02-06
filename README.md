# spark_twitter
It's a playground for using Twitter streaming api and trying Apache Spark.

Answering the question: What are the current most popular hashtags in tweets mentioning Toronto?

1. Run *twitter_client.py*: it creates a socket on *localhost:50001* and listens. 
2. Run *spark_client.py*: it connects to *localhost:50001*.

*twitter_client.py* connects to Twitter API and takes tweets where *toronto* is mentioned and then sends hashtags of the tweet to spark stream.

With the help of Spark hashtags are being counted (constantly updating as tweets come) and 20 the most popular tags are displayed in console as a data frame.

***

###### _spoiler_: #toronto is usually around 10 times more popular than any other hashtag

Example (proof):

|     hashtag|hashtag_count|
|------------|-------------|
|     toronto|          240|
|         job|           20|
|      hiring|           18|
|blackpanther|           16|
|      canada|           15|
|       sales|           11|
|        news|           11|
|      topoli|           11|
|     ontario|           10|
| danaigurira|            9|
|bobmarleyday|            9|
|   careerarc|            9|
|    hamilton|            8|
|        fake|            8|
|  mapleleafs|            8|
| mississauga|            8|
|         nhl|            7|
|      design|            7|
|        cats|            7|
|      winter|            7|


