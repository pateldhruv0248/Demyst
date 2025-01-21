import csv
import os
import json

# Reads the field specification from a JSON file.
def read_spec(spec_file_path):
    with open(spec_file_path, "r") as file:
        spec = json.load(file)
    return spec

# Parses a single fixed-width line based on the field specification.
def parse_fixed_width_line(line, field_spec):
    record = []
    start = 0
    for offset in field_spec["Offsets"]:
        length = int(offset)
        record.append(line[start:start + length].strip())
        start += length
    return record

# Writes data to a CSV file.
def write_csv(output_path, rows, columnNames=None):
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            if columnNames:
                writer.writerow(columnNames)
            # Considering that headers are already present in the first row and
            # following the offset order in the spec file.
            writer.writerows(rows)
        print(f"CSV successfully written to {output_path}")
    
    except Exception as e:
        print(f"Error writing CSV: {e}")
