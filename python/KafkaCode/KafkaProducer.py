import argparse

from kafka import KafkaProducer


def parse_arguments():
    parser = argparse.ArgumentParser()
    # INPUT DETAILS
    parser.add_argument("--topic_name", type=str, required=True)
    parser.add_argument('--test_size', type=int, required=True)
    parser.add_argument('--bootstrap_servers', type=str, required=True)

    return parser.parse_args()


def create_test_records(size):
    records = []
    for i in range(size):
        # 1 kb massage
        tmp = """
  Before the 2014–15 season, Salah's future with Chelsea looked to be in a balance after reports suggested he could be forced to return to Egypt to carry out military service after his registration for an education scheme was rescinded by the Egyptian Minister of Higher Education.[45] He was spared of military service after the meeting with the then Egyptian prime minister Ibrahim Mahlab, the Minister of Higher Education and the Egyptian national manager Shawky Gharib.[46] Salah changed squad numbers from 15 to 17 for the start of the season, with his new number having been vacated by Eden Hazard changing to number 10.[47]
Salah was rarely used during the season. On 28 October 2014, in a 2–1 win at League Two club Shrewsbury Town in the fourth round of the League Cup, he took a shot that went so far off target that it went for a throw-in.[48] After the game, he and fellow winger André Schürrle were criticized publicly by manager José Mourinho.[49] Although Salah only made three league appearances before his
        """
        records.append(tmp)
    return records


def publish_message(producer_instance, topic_name, value):
    try:
        value_bytes = bytes(value, encoding='utf-8')
        producer_instance.send(topic_name, value=value_bytes)
        producer_instance.flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))


def connect_kafka_producer(bootstrap_servers):
    _producer = None
    try:
        _producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer


if __name__ == '__main__':
    args = parse_arguments()
    insert_size = args.test_size
    topic_name = args.topic_name
    bootstrap_server = args.bootstrap_servers.split(",")
    data = create_test_records(insert_size)
    kafka_producer = connect_kafka_producer(bootstrap_server)
    print(topic_name)
    for record in data:
        publish_message(topic_name=topic_name, value=record, producer_instance=kafka_producer)




