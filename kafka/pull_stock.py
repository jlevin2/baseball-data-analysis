import multiprocessing as mp
from kafka import KafkaProducer

class Stock():

    def __init__(self, ticker, interval):
        self.ticker = ticker
        self.interval = interval


    def pull(self):
        while True:


    def push(self):
