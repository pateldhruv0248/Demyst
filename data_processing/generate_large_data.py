import pandas as pd
import random

def generate_large_sample_data(num_records=1000000, output_file='large_original_data.csv'):
    # Generate large sample data in chunks
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