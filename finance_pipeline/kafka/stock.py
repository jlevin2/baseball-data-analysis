from kafka import KafkaProducer
import requests
import logging
import datetime
import hashlib
import json
import threading
from threading import Timer
from multiprocessing import Process
import time

loger = logging.getLogger('Stocks')

class Stock(threading.Thread):

    def __init__(self, ticker):
        super(Stock, self).__init__()
        self.ticker = ticker
        self.setName('Stock-' + self.ticker)
        self.log = {}
        # TODO setup config files for kafka and other fields
        self.producer = KafkaProducer(
            bootstrap_servers=['localhost:9092', 'localhost:9093', 'localhost:9094'],
            client_id='stock-unit-' + self.ticker
        )

    def __del__(self):
        if hasattr(self, 'producer'):
            self.producer.flush()
            self.producer.close()

    def getRequest(self, url):
        loger.debug('Making API request for url: ' + url, extra=self.log)

        resp = requests.get(url)

        if resp.status_code != 200:
            loger.warning('Failed api request:' + resp.text, extra=self.log)
            return {}

        loger.debug('Successfully made api request. Returned: ' + resp.text, extra=self.log)

        return resp.json()

    def goInfo(self):
        loger.info('Fetching company data', extra=self.log)
        resp = self.getRequest(
            'https://api.iextrading.com/1.0/stock/{0}/company'.format(self.ticker))
        if len(resp) == 0:
            loger.warning('Resp returned no data')
            return

        key = hashlib.sha256(bytes(self.ticker + str(datetime.datetime.now()) + 'info',
                                   'utf-8')).hexdigest()

        self.producer.send(
            topic='Stocks_Company_Info',
            key=bytes(key, encoding='utf-8'),
            value=bytes(json.dumps(resp), encoding='utf-8')
        )

        loger.info('Sent company data for stock to Kafka', extra=self.log)

    def goPrice(self):
        loger.info('Fetching Price', extra=self.log)
        resp = self.getRequest(
            'https://api.iextrading.com/1.0/stock/{0}/quote'.format(self.ticker))
        if len(resp) == 0:
            loger.warning('Resp returned no data')
            return

        key = hashlib.sha256(bytes(self.ticker + str(datetime.datetime.now()) + 'price',
                                   'utf-8')).hexdigest()


        self.producer.send(
            topic='Stocks_Price',
            key=bytes(key, encoding='utf-8'),
            value=bytes(json.dumps(resp), encoding='utf-8')
        )

        loger.info('Sent Price for stock to Kafka', extra=self.log)

    # TODO add historicals here!

    def run(self):
        loger.info("Starting deploy of jobs", extra=self.log)
        self.goInfo()
        while True:
            self.goPrice()
            self.producer.flush()
            time.sleep(60)
            # t1 = Timer(60, self.goPrice)
            # t1.start()
            #
            # t1.join()





