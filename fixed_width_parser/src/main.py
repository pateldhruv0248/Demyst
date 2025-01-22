from .parser import fixed_width_parser_to_csv

if __name__ == "__main__":
    # File paths
    spec_file = "./spec.json"
    input_file = "./input_files/fixed-width-file.txt"
    output_file = "./output_files/csv_file.csv"

    fixed_width_parser_to_csv(spec_file=spec_file, input_file=input_file, output_file=output_file)
