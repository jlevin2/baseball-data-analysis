import kafka
from kafka import KafkaConsumer


def main():
    consumer = KafkaConsumer(
        bootstrap_servers=['localhost:9092','localhost:9093','localhost:9094'],
        auto_offset_reset='earliest',
        client_id='test_fetcher',
        consumer_timeout_ms=1000)

    consumer.subscribe(['Person'])

    print(consumer.topics())

    print(consumer.assignment())
    print(consumer.end_offsets(consumer.assignment()))

    for msg in consumer:
        print(msg.topic)
        print(msg.partition)
        print(msg.offset)
        print(msg.key)
        print(msg.value)



    #resp = consumer.poll(max_records=1000)

    #print(resp)

    # for message in consumer:
    #     print(message)
        #print(str(int.from_bytes(message, byteorder='little')))

    consumer.close()



