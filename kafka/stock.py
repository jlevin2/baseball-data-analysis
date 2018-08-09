from kafka import KafkaProducer
import requests
import logging
import datetime
import hashlib
import json
from threading import Timer
from multiprocessing import Process

loger = logging.getLogger('Stocks')

class Stock(Process):

    def __init__(self, ticker):
        super(P, self).__init__()
        self.ticker = ticker
        # TODO setup config files for kafka and other fields

    def getRequest(self, url):
        loger.debug('Making API request for url: ' + url)

        resp = requests.get(url)

        if resp.status_code != 200:
            loger.warning('Failed api request:' + resp.text)
            return {}

        loger.debug('Successfully made api request. Returned: ' + resp.text)

        return resp.json()

    def goInfo(self):
        resp = self.getRequest(
            'https://api.iextrading.com/1.0/stock/{0}/company'.format(self.ticker))
        if len(resp) == 0:
            loger.warning('Resp returned no data')
            return

        key = hashlib.sha256(self.ticker + str(datetime.datetime.now()) + 'info')

        self.producer.send(
            topic='Stocks_Company_Info',
            key=key,
            value=bytes(json.dumps(resp), encoding='utf-8')
        )

    def goPrice(self):
        self.producer = KafkaProducer(
            bootstrap_servers=['localhost:9092', 'localhost:9093', 'localhost:9094'],
            client_id='stock-unit-' + self.ticker
        )
        loger.info('Fetching Price for stock {0}'.format(self.ticker))
        resp = self.getRequest(
            'https://api.iextrading.com/1.0/stock/{0}/chart/1d'.format(self.ticker))
        if len(resp) == 0:
            loger.warning('Resp returned no data')
            return

        key = hashlib.sha256(self.ticker + str(datetime.datetime.now()) + 'price')

        self.producer.send(
            topic='Stocks_Price',
            key=key,
            value=bytes(json.dumps(resp), encoding='utf-8')
        )

        loger.info('Sent Price for stock {0} to Kafka'.format(self.ticker))

    # TODO add historicals here!

    def run(self):
        while True:
            t1 = Timer(60.0, self.goPrice)
            # Company info is daily
            #t2 = Timer(86400.0, goInfo)
            t1.start()
            #t2.start()

