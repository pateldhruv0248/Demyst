from .utils import read_spec, write_csv

# Parse fixed-width-file into csv
def fixed_width_parser_to_csv(spec_file, input_file, output_file):

    # Read field specifications
    field_spec = read_spec(spec_file)
    print(field_spec)
    includeHeaders = field_spec["IncludeHeader"]

    # Parse the fixed-width file
    rows = []
    try:
        with open(input_file, "r") as file:
            for line in file:
                rows.append(parse_fixed_width_line(line, field_spec))
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

    # Write to CSV
    if includeHeaders:
        write_csv(output_file, rows)
    else:
        write_csv(output_file, rows, field_spec["ColumnNames"] )
    print(f"Parsed CSV is saved at: {output_file}")

    return rows

# Parses a single fixed-width line based on the field specification.
def parse_fixed_width_line(line, field_spec):
    record = []
    start = 0
    for offset in field_spec["Offsets"]:
        length = int(offset)
        record.append(line[start:start + length].strip())
        start += length
    return record
