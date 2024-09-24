from kafka import KafkaConsumer

# Kafka configuration
KAFKA_SERVER = 'localhost:9092'
TOPIC = 'test-topic'

# Create a Kafka consumer
consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=KAFKA_SERVER,
    auto_offset_reset='earliest',
    group_id='my-group'
)

for message in consumer:
    print(f'Received message: {message.value.decode("utf-8")}')