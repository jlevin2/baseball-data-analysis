from pyspark import SparkContext
from pyspark import sql
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql.types import *
from pyspark.sql.functions import udf
import json
from pyspark.sql import DataFrameWriter
import configparser
from pyspark.sql.functions import when

sc = SparkContext(appName="PythonSparkStreamingKafka").getOrCreate()

config = configparser.ConfigParser()

config.read('../../config/stocks-config.ini')

schema = StructType()
mapping = {"StringType": StringType(),
           "IntegerType": IntegerType(),
           "DoubleType": DoubleType(),
           "LongType": LongType(),
           }


for col, typ in config['priceSchema'].items():
    schema.add(field=col, data_type=mapping[typ], nullable=True)

# IMPORTANT MAKE SURE CONFIG FILES ARE USING RIGHT PYTHON VERSION

def main():
    #sc = SparkSession.builder.appName("PythonSparkStreamingKafka").getOrCreate()

    ssc = StreamingContext(sc, 5)

    topics = {
        'Stocks_Price' : 3
    }
    zkQuorum = "127.0.0.1:2181,127.0.0.1:2182,127.0.0.1:2183"

    kafkaStream = KafkaUtils.createStream(ssc,
                                  topics=topics,
                                  zkQuorum=zkQuorum,
                                  groupId='test_123'

    )

    parsed = kafkaStream.map(lambda v:
                             json.loads(v[1]))

    parsed.pprint()

    parsed.foreachRDD(process)

    ssc.start()
    ssc.awaitTermination()

def replace(column, value):
    return when(column != value, column).otherwise(None)

def process(rdd):
    try:
        sqlContext = sql.SQLContext(sc)
        df = sqlContext.createDataFrame(rdd, schema)

        #resetNulls = udf(lambda name: None if name == "NULL" else name, StringType())

        # Cast columns
        for col, typ in config['priceSchema'].items():
            #print(resetNulls(df[col]))
            df = df.withColumn(col, replace(df[col], 'NULL').cast(mapping[typ]))

        print(df.take(5))


        #my_writer = DataFrameWriter(df)

        url_connect = "jdbc:postgresql://localhost:5432/postgres" \
                      "?user=dataloader&password=bigdata"
        table = "finance.stg_prices_test"
        mode = "append"
        properties = {"driver": 'org.postgresql.Driver'}

        df.write.jdbc(url_connect, table, mode, properties)
    except Exception as e:
        print('Exception: ' + str(e))

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