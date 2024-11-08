"""The supposed stream producer."""
import random
import pickle
import os
import logging
from time import sleep
from json import dumps

from kafka  import KafkaProducer
TOPIC_A = 'TopicA-0'

def encode_to_json(x_train, y_train):
    """Create data dumps."""
    x = dumps(x_train.tolist())
    y = dumps(y_train.tolist())
    jsons_comb = [x, y]

    return jsons_comb


def generate_stream(**kwargs):
    """Generate data stream."""
    # Set up producer
    producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
        value_serializer=lambda x: dumps(x).encode('utf-8'))
    # load stream sample file
    stream_sample = pickle.load(open(os.getcwd() + kwargs['path_stream_sample'], "rb"))
    # the stream sample consists of 20000 observations -
    # and along this setup 200 samples are selected randomly
    rand = random.sample(range(0, 20000), 200)

    x_new = stream_sample[0]
    y_new = stream_sample[1]

    logging.info('Partitions: %s', producer.partitions_for(TOPIC_A))

    for i in rand:
        # pick observation and encode to JSON
        json_comb = encode_to_json(x_new[i], y_new[i])
        # send encoded observation to Kafka topic
        producer.send(TOPIC_A, value=json_comb)
        logging.info("Sent number:%f", y_new[i])
        sleep(1)

    producer.close()
