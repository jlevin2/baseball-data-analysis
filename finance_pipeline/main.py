import requests
import logging
import datetime
import hashlib
import json
from threading import Timer
from multiprocessing import Process
from finance_pipeline.stock import Stock


logging.basicConfig(filename='run.log') #, format='%(asctime) %(message)s')

loger = logging.getLogger('Stocks')

loger.setLevel('INFO')


def main():

    processes = []
    # Spin off process for each stock
    with open('../config/stocks.txt', 'r') as stocks:
        for tick in stocks.readlines():
            stk = Stock(tick.strip())
            stk.start()
            processes.append(stk)
            stk.goInfo()


if __name__ == "__main__":
    main()