from kafka import KafkaProducer


if __name__ == "__main__":
    pro = KafkaProducer(bootstrap_servers='localhost:9092')

    for i in range(0, 100):
        print(pro.send('numbers2', i.to_bytes(1, byteorder='little')))

    #pro.send('test-topic-blah', b'this is random text!!')

    pro.close()



