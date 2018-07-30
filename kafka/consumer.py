import kafka
from kafka import KafkaConsumer


if __name__ == "__main__":
    consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                             auto_offset_reset='earliest',
                             consumer_timeout_ms=1000)

    consumer.subscribe(['numbers2'])


    print(consumer.topics())

    print(consumer.partitions_for_topic('numbers2'))

    tp = kafka.TopicPartition(
        'numbers2',
        0
    )

    consumer.seek(tp, 0)

    print(consumer.poll())

    #resp = consumer.poll(max_records=1000)

    #print(resp)

    for message in consumer:
        print(message)
        #print(str(int.from_bytes(message, byteorder='little')))

    consumer.close()



