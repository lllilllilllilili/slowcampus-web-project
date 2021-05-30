from google.cloud import pubsub_v1
from google.cloud import bigquery
import time
# TODO(developer)
project_id = "fluid-crane-284202"
topic_id = "test"

# Construct a BigQuery client object.
client = bigquery.Client()

# Configure the batch to publish as soon as there is ten messages,
# one kilobyte of data, or one second has passed.
batch_settings = pubsub_v1.types.BatchSettings(
    max_messages=10,  # default 100
    max_bytes=1024,  # default 1 MB
    max_latency=1,  # default 10 ms'

)
publisher = pubsub_v1.PublisherClient(batch_settings)
topic_path = publisher.topic_path(project_id, topic_id)

query = """
    SELECT *
FROM `fluid-crane-284202.prototyping_dataset.category_streaming`
"""
query_job = client.query(query)

# Resolve the publish future in a separate thread.
def callback(topic_message):
    message_id = topic_message.result()
print("The query data:")
for row in query_job:
    data = u"category={}, language={}, year={}".format(row[0], row[1], row[2])
    print(data)
    splited = data.split(",")
    splited[0]=splited[0][9:]
    splited[1]=splited[1][10:]
    splited[2]=splited[2][6:]

    for x in splited[1].split(' '):
        data = u"category={}, language={}, count={}, year={}".format(splited[0], x, 1, splited[2])
        data = data.encode("utf-8")
        print(data)
        time.sleep(1)
        topic_message = publisher.publish(topic_path, data=data)
        topic_message.add_done_callback(callback)

print("Published messages with batch settings.")