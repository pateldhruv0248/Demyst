import os
from utils import read_spec, parse_fixed_width_line, write_csv

# Parse fixed-width-file into csv
def fixed_width_parser_to_csv():
    # File paths
    spec_file = "./fixed_width_parser/spec.json"
    input_file = "./fixed_width_parser/input_files/data.txt"
    output_file = "./fixed_width_parser/output_files/csv_file.csv"

    # Read field specifications
    field_spec = read_spec(spec_file)
    print(field_spec)
    includeHeaders = field_spec["IncludeHeader"]

    # Parse the fixed-width file
    rows = []
    with open(input_file, "r") as file:
        for line in file:
            rows.append(parse_fixed_width_line(line, field_spec))

    # Write to CSV
    if includeHeaders:
        write_csv(output_file, rows)
    else:
        write_csv(output_file, rows, field_spec["ColumnNames"] )
    print(f"Parsed CSV saved to: {output_file}")

