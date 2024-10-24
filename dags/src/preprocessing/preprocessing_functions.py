"""Represents a preprocessor function."""
import logging


def preprocessing(**kwargs):
    """Computes preprocessing for data"""
    ti = kwargs['ti']
    loaded = ti.xcom_pull(task_ids='load_data')
    logging.info('variables successfully fetched from previous task')
    new_samples = loaded[0]
    test_set = loaded[1] # Once we have loaded the
    # new data we could do some preprocessing and
    # pass on the preprocessed variables
	# Left this section open as no further preprocessing 
    # is required
    logging.info('preprocessed the data')
    return[new_samples, test_set]
