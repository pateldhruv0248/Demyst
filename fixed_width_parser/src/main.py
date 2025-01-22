from .parser import fixed_width_parser_to_csv

if __name__ == "__main__":
    # File paths
    spec_file = "./fixed_width_parser/spec.json"
    input_file = "./fixed_width_parser/input_files/data.txt"
    output_file = "./fixed_width_parser/output_files/csv_file.csv"

    fixed_width_parser_to_csv(spec_file=spec_file, input_file=input_file, output_file=output_file)
