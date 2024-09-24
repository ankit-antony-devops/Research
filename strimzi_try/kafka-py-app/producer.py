from kafka import KafkaProducer
import time

# Kafka configuration
KAFKA_SERVER = 'localhost:9092'
TOPIC = 'test-topic'

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

while True:
    message = 'Hello, Kafka!'
    producer.send(TOPIC, value=message.encode('utf-8'))
    print(f'Sent message: {message}')
    time.sleep(5)  # Send a message every 5 seconds