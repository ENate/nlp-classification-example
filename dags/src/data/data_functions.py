"""Data functions file."""
import os
import time
import logging
import pickle
from json import loads
import numpy as np
from kafka import KafkaConsumer #, TopicPartition


def decode_json(jsons_comb):
    """Imports training data samples."""
    x_train = loads(jsons_comb[0])
    y_train = loads(jsons_comb[1])
    return x_train, y_train


def get_data_from_kafka(**kwargs):
    """Gets data from kafka  topic"""
    consumer = KafkaConsumer(
        kwargs['topic'],                     # specify topic to consume from
        bootstrap_servers=[kwargs['client']],
        # break connection if the consumer has fetched anything
        # for 3 seconds (e.g. in case of an empty topic)
        consumer_timeout_ms=3000,
        # automatically reset the offset to the earliest offset
        # (should the current offset be deleted or anything)
        auto_offset_reset='earliest',
        # offsets are committed automatically by the consumer
        enable_auto_commit=True,
        #group_id='my-group',
        value_deserializer=lambda x: loads(x.decode('utf-8')))


    logging.info('Consumer constructed')
    try:
        xs = []
        ys = []
        for message in consumer: # loop over messages
            logging.info( "Offset: %s", message.offset)
            message = message.value
            x, y = decode_json(message) # decode JSON
            xs.append(x)
            ys.append(y)
            logging.info('Image retrieved from topic')

        # xs = np.array(xs).reshape(-1, 28, 28, 1)
        # # put Xs in the right shape for our CNN
        xs = np.expand_dims(np.array(xs), -1)
        ys = np.array(ys).reshape(-1) # put ys in the right shape for our CNN
        new_samples = [xs, ys]
        pickle.dump(new_samples, open(
            # write data
            os.getcwd()+kwargs[
                'path_new_data']+str(time.strftime("%Y%m%d_%H%M"))+"_new_samples.p", "wb"))

        logging.info(xs.shape[0], '%s new samples retrieved')
        consumer.close()

    except Exception as e:
        print(e)
        logging.info('Error: %s', e)


def load_data(**kwargs):
    """The load data function with parameters from kwargs
    Returns:
        _type_: a dict of input parameters.
    """
    # Load the Kafka-fetched data that is stored in the to_use_for_model_update folder

    for file_d in os.listdir(os.getcwd()+kwargs['path_new_data']):

        if 'new_samples.p' in file_d:
            new_samples = pickle.load(open(os.getcwd()+kwargs['path_new_data'] + file_d, "rb"))
            test_set = pickle.load(open(os.getcwd()+kwargs['path_test_set'], "rb"))
            logging.info('data loaded')
            return [new_samples, test_set]

        else:
            logging.info('no data found')
