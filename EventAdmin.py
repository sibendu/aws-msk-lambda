import json
import boto3

from kafka import KafkaAdminClient, KafkaConsumer, KafkaProducer
from kafka.admin import NewTopic
        
def lambda_handler(event, context):
    
    bootstrap = '<>'
    topic_name = 'orders'
    
    print(event)
        
    try:
        admin = KafkaAdminClient(bootstrap_servers=bootstrap)
        print(admin)
        topic = NewTopic(name=topic_name,num_partitions=1,replication_factor=2)
        admin.create_topics([topic])
        msg = 'topic created'
        print(msg)
    except Exception as err:
        msg = "Error in creating topic: {0}".format(err)
        print(msg)
        pass
        
    try:
        producer = KafkaProducer(bootstrap_servers=bootstrap)
        print(producer)
        payload = json.dumps(event).encode('utf-8')
        producer.send(topic_name, payload)
        producer.close()
        msg = 'Message sent to topic'
        print(msg)
    except Exception as err:
        msg = "Error in sending message to topic: {0}".format(err)
        print(msg)
        pass
        
    """
    try:
        consumer = KafkaConsumer(bootstrap_servers=bootstrap,auto_offset_reset='earliest',consumer_timeout_ms=1000)
        consumer.subscribe([topic_name])
        while not self.stop_event.is_set():
            for message in consumer:
                print(message)
                if self.stop_event.is_set():
                    break
        consumer.close()
    
    except Exception as err:
        print('Error in consuming message from topic')
        print("Error: {0}".format(err))
        pass
    
    """        
    
    return {
        'statusCode': 200,
        'body': json.dumps('Success!')
    }
