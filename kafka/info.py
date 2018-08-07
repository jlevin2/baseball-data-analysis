from kafka.cluster import ClusterMetadata

def main():
    c = ClusterMetadata(bootstrap_servers='localhost:9092,localhost:9093,localhost:9094')
    #c = KafkaClient(bootstrap_servers='localhost:9092,localhost:9093,localhost:9094')

    c.request_update()

    #print(c.update_metadata())

    print(c.brokers())
    print(c.broker_metadata(1))
    print(c.broker_metadata(2))
    print(c.broker_metadata(3))

if __name__ == "__main__":
    main()