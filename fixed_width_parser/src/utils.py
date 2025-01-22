import csv
import os
import json

# Reads the field specification from a JSON file.
def read_spec(spec_file_path):
    try:
        with open(spec_file_path, "r") as file:
            spec = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {spec_file_path} does not exist.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    return spec

# Writes data to a CSV file.
def write_csv(output_path, rows, columnNames=None):
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            if columnNames:
                writer.writerow(columnNames)
            # Considering that headers are already present in the first row in the 
            # spec file and following the offset order.
            writer.writerows(rows)
        print(f"CSV successfully written to {output_path}")
    
    except Exception as e:
        print(f"Error writing CSV: {e}")
