import os

os.environ['PYSPARK_SUBMIT_ARGS'] = '--jars ~/spark-streaming-kafka-0-8-assembly_2.11-2.4.4 pyspark-shell'

import sys
import time
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

n_secs = 1
topic = "testo"
conf = SparkConf().setAppName("KafkaStreamProcessor")
sc = SparkContext(conf=conf)
sc.setLogLevel("WARN")
ssc = StreamingContext(sc, n_secs)
kafkaStream = KafkaUtils.createStream(ssc, "10.128.0.16:2181", {topic: 3})
lines = kafkaStream.map(lambda x: x[1])
counts = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)
counts.pprint()
ssc.start()