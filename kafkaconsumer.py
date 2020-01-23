'''
Created on Jan 22, 2020

@author: ashish
'''
from kafka import KafkaConsumer
consumer=KafkaConsumer('sample')
for message in consumer:
    print(message)
