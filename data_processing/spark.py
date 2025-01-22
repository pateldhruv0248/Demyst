from hashlib import sha256
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

# Using PySpark (For distributed computing on very large datasets)
def setup_spark():
    # Initialize Spark session
    return SparkSession.builder \
        .appName("DataAnonymization") \
        .config("spark.driver.memory", "4g") \
        .config("spark.executor.memory", "4g") \
        .getOrCreate()

def anonymize_with_spark(input_file, output_file):
    # Anonymize large CSV file using Spark
    spark = setup_spark()
    
    # Read CSV file
    df = spark.read.csv(input_file, header=True, inferSchema=True)
    
    # Define UDFs for anonymization
    anonymize_name_udf = udf(lambda name: 'ANONYMIZED_' + sha256(str(name).encode()).hexdigest()[:8], StringType())
    anonymize_address_udf = udf(
        lambda addr: addr.split(',')[1].strip() if ',' in str(addr) else 'UNKNOWN_CITY',
        StringType()
    )
    
    # Apply anonymization
    anonymized_df = df \
        .withColumn('first_name', anonymize_name_udf('first_name')) \
        .withColumn('last_name', anonymize_name_udf('last_name')) \
        .withColumn('address', anonymize_address_udf('address'))
    
    # Write to CSV
    anonymized_df.write.csv(output_file, header=True, mode='overwrite')
    
    spark.stop()
