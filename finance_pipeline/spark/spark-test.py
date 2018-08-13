from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json
from pyspark.sql import DataFrameWriter
import os

def main():
    sc = SparkContext(appName="PythonSparkStreamingKafka")
    sc.setLogLevel("WARN")
    ssc = StreamingContext(sc, 5)

    topics = {
        'Stocks_Price' : 3
    }
    zkQuorum = "localhost:2181,localhost:2182,localhost:2183"

    kafkaStream = KafkaUtils.createStream(ssc,
                                  topics=topics,
                                  zkQuorum=zkQuorum,
                                  groupId='test_123'

    )

    parsed = kafkaStream.map(lambda v:
                             (v[0].decode('utf-8'),json.loads(v[1])))

    parsed.pprint()

    #parsed.foreachRDD(writeToPostgres)

    ssc.start()
    ssc.awaitTermination()

#
# def writeToPostgres(rdd):
#     # TODO implement this method
#     df = DataFrameWriter()
#
#     columns = [
#           'symbol',
#           'calculationPrice',
#           'open',
#           'close',
#           'high',
#           'low',
#           'latestPrice',
#           'latestSource',
#           'latestUpdate',
#           'latestVolumne',
#           'change',
#           'changePercent',
#           'peRatio',
#           'eventid'
#     ]
#
#     df = df.select([c for c in df.columns if c in columns]).show()
#
#     my_writer = DataFrameWriter(df)
#
#     url_connect = "jdbc:postgresql://localhost:5432/postgres"
#     table = "finance.stg_prices"
#     mode = "append"
#     properties = {"user": "dataloader", "password": "bigdata"}
#
#     my_writer.jdbc(url_connect, table, mode, properties)

if __name__ == "__main__":

    main()