import argparse
import timeit

from pymongo import MongoClient


def parse_arguments():
    parser = argparse.ArgumentParser()
    # INPUT DETAILS
    parser.add_argument('--test_size', type=int, required=True)

    return parser.parse_args()


def create_rand(insert_size):
    result = []
    for i in range(insert_size):
        result.append({
            "name": "test name",
            "number": "18225318682"
        })
    return result


def bulk_insert(create_test):
    mongo_client = MongoClient()
    db = mongo_client.replicasetdb
    col = db.mycollection
    col.insert_many(create_test)


if __name__ == '__main__':
    args = parse_arguments()

    insert_size = args.test_size
    create_test = create_rand(insert_size)
    # get currant time
    start_time = timeit.default_timer()
    bulk_insert(create_test)
    end_time = timeit.default_timer()
    print("total time took {}".format(end_time-start_time))