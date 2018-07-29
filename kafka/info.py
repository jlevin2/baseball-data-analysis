from kafka.cluster import ClusterMetadata

def main():
    c = ClusterMetadata(bootstrap_servers='192.168.0.17:9092')
    print(c.brokers())
    print(c.topics())

if __name__ == "__main__":
    main()