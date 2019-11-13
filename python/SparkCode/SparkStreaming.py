import argparse
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

from uuid import uuid1


# sc = SparkContext(appName="PythonSparkStreamingKafka")
# sc.setLogLevel("WARN")
mongo_url = "mongodb://{}:27017/"

def parse_arguments():
    parser = argparse.ArgumentParser()
    # INPUT DETAILS
    parser.add_argument("--topic_name", type=str, required=True)
    parser.add_argument('--ZK_opt', type=str, required=True)
    parser.add_argument('--mongo_server', type=str, required=True)
    return parser.parse_args()




def printing(word):
    print(word)
    return word


if __name__ == '__main__':
    args = parse_arguments()
    my_spark = SparkSession\
        .builder\
        .appName("streaming from kafka to mongo")\
        .config("spark.mongodb.input.uri", "mongodb://{}/sparkkafka.stream".format(args.mongo_server)).getOrCreate()
    sparkContext = my_spark.sparkContext
    ssc = StreamingContext(sparkContext, 2)
    kvs = KafkaUtils.createStream(ssc=ssc, zkQuorum=args.ZK_opt, topics={args.topic_name: 3})
    kvs.pprint()
    ssc.start()
    ssc.awaitTermination()
