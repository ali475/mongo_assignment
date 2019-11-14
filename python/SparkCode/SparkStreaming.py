import sys
from pyspark.sql.functions import udf
from pyspark.sql import SparkSession


if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("StructuredNetworkWordCount") \
        .config("spark.mongodb.input.uri", "mongodb://10.128.0.19:27017/twitter.test") \
        .config("spark.mongodb.output.uri", "mongodb://10.128.0.19:27017/twitter.test") \
        .getOrCreate()
    events = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "10.128.0.19:9092,10.128.0.16:9092,10.128.0.20:9092") \
        .option("subscribe", "testo") \
        .load()
    events = events.selectExpr("CAST(value as String)")

    mongooutput = events \
        .writeStream \
        .format("com.mongodb.spark.sql.DefaultSource") \
        .option("com.mongodb.spark.sql.DefaultSource", "mongodb://localhost:27017/twitter.test") \
        .start()
    mongooutput.awaitTermination()
