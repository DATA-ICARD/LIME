# Example written based on the official 
# Confluent Kakfa Get started guide https://github.com/confluentinc/examples/blob/7.1.1-post/clients/cloud/python/consumer.py

from confluent_kafka import Consumer
import ccloud_lib
import time
from sqlalchemy import create_engine, text
import psycopg2
import pandas as pd


# Initialize configurations from "python.config" file
CONF = ccloud_lib.read_ccloud_config("python.config")
TOPIC = "my_lime_07_16_topic" 

# Create Consumer instance
# 'auto.offset.reset=earliest' to start reading from the beginning of the
# topic if no committed offsets exist
consumer_conf = ccloud_lib.pop_schema_registry_params_from_config(CONF)
consumer_conf['group.id'] = 'my_stations_consumer'
consumer_conf['auto.offset.reset'] = 'earliest' # This means that you will consume latest messages that your script haven't consumed yet!
consumer = Consumer(consumer_conf)

# Subscribe to topic
consumer.subscribe([TOPIC])

# Process messages
try:
    while True:
        msg = consumer.poll(1.0) # Search for all non-consumed events. It times out after 1 second
        if msg is None:
            # No message available within timeout.
            # Initial message consumption may take up to
            # `session.timeout.ms` for the consumer group to
            # rebalance and start consuming
            print("Waiting for message or event/error in poll()")
            continue
        elif msg.error():
            print('error: {}'.format(msg.error()))
        else:
            # Check for Kafka message
            record_key = msg.key()
            record_value = msg.value().decode('utf-8')
            data = record_value

            df = pd.read_json(data, orient='split')
            print(df)

#            conn_string = "host= dbname='' user='' password=''"
#            conn = psycopg2.connect(conn_string)
#            cursor = conn.cursor(df_sql)

            USERNAME = {{username}}
            PASSWORD = {{password}}
            HOSTNAME = 'ec2-34-242-8-97.eu-west-1.compute.amazonaws.com'
            DBNAME = 'd94bbpnen8i78h'
        # Create engine will create a connection between a SQLlite DB and python
            engine = create_engine(f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOSTNAME}/{DBNAME}", echo=True)
            df_sql = df.to_sql('Stations_07_16', con=engine, if_exists='append')


            print(f"end data are : \n\n{data} \n\n\n\n")
            time.sleep(1) # Wait one second
except KeyboardInterrupt:
    pass
finally:
    # Leave group and commit final offsets
    consumer.close()