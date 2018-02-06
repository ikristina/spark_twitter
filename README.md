# spark_twitter
It's a playground for using Twitter streaming api and trying Apache Spark.

Answering the question: What are the current most popular hashtags in tweets mentioning Toronto?

1. Run *twitter_client.py*: it creates a socket on *localhost:50001* and listens. 
2. Run *spark_client.py*: it connects to *localhost:50001*.

*twitter_client.py* connects to Twitter API and takes tweets where *toronto* is mentioned and then sends hashtags of the tweet to spark stream.

With the help of Spark hashtags are being counted (constantly updating as tweets come) and 20 the most popular tags are displayed in console as a data frame.

***

###### _spoiler_: #toronto is usually 7-10 times as popular as any other hashtag

Example (proof):

|       hashtag|hashtag_count|
|--------------|-------------|
|       toronto|           37|
|  bobmarleyday|            5|
|    realestate|            5|
|        canada|            5|
|         sales|            5|
|          fake|            4|
|        topoli|            4|
|      hamilton|            4|
|        design|            4|
|         eluta|            3|
|       startup|            3|
|reggaetonlento|            3|
|          sale|            3|
|     bestremix|            3|
|  iheartawards|            3|
|       forsale|            3|
|   mississauga|            3|
|        online|            2|
|          shop|            2|
|         store|            2|

