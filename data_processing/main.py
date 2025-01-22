from generate_large_data import generate_large_sample_data
from spark import anonymize_with_spark


if __name__ == "__main__":
    
    # Generate sample data (adjust num_records as needed)
    generate_large_sample_data(num_records=1000000, output_file='large_data.csv')
    
    # For very large datasets
    print("Processing with Spark...")
    anonymize_with_spark('large_data.csv', 'anonymized_spark.csv')
