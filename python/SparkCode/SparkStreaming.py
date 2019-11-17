import os

os.environ['PYSPARK_SUBMIT_ARGS'] = '--jars ~/spark-streaming-kafka-0-8-assembly_2.11-2.4.4 pyspark-shell'

import sys
import time
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

from pyspark.sql import SparkSession
n_secs = 1
topic = "testo"
spark_session = SparkSession.builder \
    .appName("myApp") \
    .config("spark.mongodb.input.uri", "mongodb://10.128.0.20/test.coll") \
    .config("spark.mongodb.output.uri", "mongodb://10.128.0.20/test.coll") \
    .getOrCreate()
sc = spark_session.sparkContext
sc.setLogLevel("WARN")
ssc = StreamingContext(sc, n_secs)
kafkaStream = KafkaUtils.createStream(ssc, "10.128.0.16:2181","kafkaReaders", {topic: 3})
lines = kafkaStream.map(lambda x: x[1])
counts = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b).toDF()
counts.write.format("mongo").mode("append").save()
ssc.start()
ssc.awaitTermination()