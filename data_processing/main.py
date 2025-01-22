# Solution 1: Using Dask (Good for laptop processing of 2GB+ files)
# import dask.dataframe as dd
import pandas as pd
from hashlib import sha256
import numpy as np
from datetime import datetime
import random
import os

def generate_large_sample_data(num_records=1000000, output_file='large_original_data.csv'):
    """Generate large sample data in chunks"""
    chunk_size = 100000
    num_chunks = num_records // chunk_size
    
    # Sample data pools
    first_names = ['John', 'Jane', 'Michael', 'Emma', 'William', 'Sarah', 'David', 'Lisa', 'Robert', 'Mary']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez']
    streets = ['Main St', 'Oak Ave', 'Maple Rd', 'Cedar Ln', 'Pine Dr']
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
    
    # Write header
    with open(output_file, 'w') as f:
        f.write('first_name,last_name,address,date_of_birth\n')
    
    # Generate data in chunks
    for chunk in range(num_chunks):
        data = []
        for _ in range(chunk_size):
            address = f"{random.randint(100, 9999)} {random.choice(streets)}, {random.choice(cities)}"
            record = {
                'first_name': random.choice(first_names),
                'last_name': random.choice(last_names),
                'address': address,
                'date_of_birth': f"{random.randint(1950, 2005)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
            }
            data.append(record)
        
        # Convert chunk to DataFrame and append to CSV
        chunk_df = pd.DataFrame(data)
        chunk_df.to_csv(output_file, mode='a', header=False, index=False)
        
        print(f"Generated chunk {chunk + 1}/{num_chunks}")



# Using PySpark (For distributed computing on very large datasets)
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

def setup_spark():
    """Initialize Spark session"""
    return SparkSession.builder \
        .appName("DataAnonymization") \
        .config("spark.driver.memory", "4g") \
        .config("spark.executor.memory", "4g") \
        .getOrCreate()

def anonymize_with_spark(input_file, output_file):
    """Anonymize large CSV file using Spark"""
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

if __name__ == "__main__":
    
    # Generate sample data (adjust num_records as needed)
    generate_large_sample_data(num_records=1000000, output_file='large_data.csv')
    
    # For very large datasets
    print("Processing with Spark...")
    anonymize_with_spark('large_data.csv', 'anonymized_spark.csv')
