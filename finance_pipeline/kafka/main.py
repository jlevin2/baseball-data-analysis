import logging
from finance_pipeline.kafka.stock import Stock

FORMAT = '%(asctime)-15s %(threadName)s %(message)s'
logging.basicConfig(filename='../../logs/stock.log', format=FORMAT)

loger = logging.getLogger('Stocks')

loger.setLevel('INFO')

def main():

    threads = []
    # Spin off process for each stock
    with open('../../config/stocks.txt', 'r') as stocks:
        for tick in stocks.readlines():
            stk = Stock(tick.strip())
            stk.start()
            threads.append(stk)

    # Wait for each process to join back
    [t.join() for t in threads]


if __name__ == "__main__":
    main()