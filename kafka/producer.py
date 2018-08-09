from kafka import KafkaProducer
import json
import hashlib

if __name__ == "__main__":
    pro = KafkaProducer(
        bootstrap_servers=['localhost:9092','localhost:9093','localhost:9094'],
        client_id='zach'
    )

    zach = {
        'name':'Zach',
        'age':18,
        'school':'Brown'
    }

    # zach = str.encode(json.dumps(zach, sort_keys=True))

    deb = {
        'name': 'Deb',
        'age': 52,
        'school': 'Smith'
    }

    # deb = str.encode(json.dumps(deb, sort_keys=True))

    steve = {
        'name': 'Steve',
        'age': 51,
        'school': 'Dartmouth'
    }

    # steve = str.encode(json.dumps(steve, sort_keys=True))

    # hashlib.sha224(zach).hexdigest()

    pro.send(
        topic='Person',
        key=b'msg1a',
        value=bytes(json.dumps(zach), encoding='utf-8'),
    )

    pro.send(
        topic='Person',
        key=b'msg2a',
        value=bytes(json.dumps(steve), encoding='utf-8'),
    )

    pro.send(
        topic='Person',
        key=b'msg3a',
        value=bytes(json.dumps(deb), encoding='utf-8'),
    )

    # for i in range(0, 100):
    #     print(pro.send('numbers2', i.to_bytes(1, byteorder='little')))

    #pro.send('test-topic-blah', b'this is random text!!')

    print(pro.metrics())

    pro.flush()

    pro.close()



