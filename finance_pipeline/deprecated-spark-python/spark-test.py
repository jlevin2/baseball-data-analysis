from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json
from pyspark.sql import DataFrameWriter
import os

def main():
    sc = SparkContext(appName="PythonSparkStreamingKafka")
    sc.setLogLevel("WARN")
    ssc = StreamingContext(sc, 15)

    kafkaStream = KafkaUtils.createDirectStream(ssc,
                                  ['Stocks_Price'],
                                  {
                                      "bootstrap.servers": ['localhost:9092', 'localhost:9093', 'localhost:9094']
                                  }

    )

    kafkaStream.foreachRDD(writeToPostgres)

def writeToPostgres(rdd):
    df = rdd.toDF()

    columns = [
          'symbol',
          'calculationPrice',
          'open',
          'close',
          'high',
          'low',
          'latestPrice',
          'latestSource',
          'latestUpdate',
          'latestVolumne',
          'change',
          'changePercent',
          'peRatio'
    ]

    df = df.select([c for c in df.columns if c in columns]).show()

    my_writer = DataFrameWriter(df)

    url_connect = "jdbc:postgresql://localhost:5432/postgres"
    table = "finance.stg_prices"
    mode = "append"
    properties = {"user": "dataloader", "password": "bigdata"}

    my_writer.jdbc(url_connect, table, mode, properties)

if __name__ == "__main__":

    main()