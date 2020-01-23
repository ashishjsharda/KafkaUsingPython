'''
Created on Jan 22, 2020

@author: ashish
'''
from kafka import KafkaProducer
producer=KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('sample', b'Hello World')
producer.send('sample', key=b'message-two', value=b'This is Kafka-Python')
