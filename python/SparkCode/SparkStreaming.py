import os

from pyspark.shell import sqlContext

os.environ['PYSPARK_SUBMIT_ARGS'] = '--jars ~/spark-streaming-kafka-0-8-assembly_2.11-2.4.4 pyspark-shell'
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

from pyspark.sql import SparkSession


def write_mongo(rdd):
    print("entering function with data ")
    print(rdd)
    try:
        df = sqlContext.createDataFrame(rdd, ["word", "count"])
        df.write.format("mongo").mode("append").save()

    except Exception as e:
        print("error{}".format(e))
        pass


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
kafkaParams = {
    "metadata.broker.list": "10.128.0.20:9092,10.128.0.19:9092,10.128.0.16:9092",
    "auto.offset.reset": "smallest"
}
kafkaStream = KafkaUtils.createDirectStream(ssc, [topic], kafkaParams)
lines = kafkaStream.map(lambda x: x[1])
lines.map(lambda word: (word, 1)).foreachRDD(lambda rdd: write_mongo(rdd))
counts = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b) \
    .foreachRDD(lambda rdd: write_mongo(rdd))

ssc.start()
ssc.awaitTermination()
