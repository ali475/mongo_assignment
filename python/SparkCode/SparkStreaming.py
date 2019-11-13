import argparse
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from uuid import uuid1


# sc = SparkContext(appName="PythonSparkStreamingKafka")
# sc.setLogLevel("WARN")


def parse_arguments():
    parser = argparse.ArgumentParser()
    # INPUT DETAILS
    parser.add_argument("--topic_name", type=str, required=True)
    parser.add_argument('--ZK_opt', type=str, required=True)
    return parser.parse_args()


def open_streaming(topic, ZK_opt):
    sc = SparkContext(appName="PythonStreamingRecieverKafkaWordCount")
    ssc = StreamingContext(sc, 2)
    kvs =KafkaUtils.createStream(ssc, ZK_opt, 'spark-streaming', {topic: 1})
    return kvs, sc, ssc


if __name__ == '__main__':
    args = parse_arguments()
    kvs, sc, ssc = open_streaming(args.topic_name, args.ZK_opt)
    lines = kvs.map(lambda x: x[1])
    counts = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)
    counts.pprint()
    ssc.start()
    ssc.awaitTermination()
