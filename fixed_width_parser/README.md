# Fixed Width Parser

## Overview

`fixed_width_parser` is a Python library designed to parse fixed-width formatted files. Fixed-width files are plain text files where each column has a fixed width, and this library helps in extracting and processing the data efficiently.

## Features

- Parse fixed-width formatted files
- Define custom column widths
- Handle large files efficiently
- Convert parsed data to CSV format

## Points to be noted

- The fixed width file was generated manually using the spec.json file provided. It is stored in the input_files/data.txt
- The output is a csv file for the given data.txt file stored in output_files/csv_file.csv
- Empty rows in fixed width file are retained in CSV file as well
- Special operators like '(single quotes), "(double quotes), ,(comma) etc are preserved in CSV file.

## Instructions

### Installation

1. Ensure you have Python 3 installed. You can download it from [python.org](https://www.python.org/).

### Running the Parser

1. Navigate to the project directory:
    ```sh
    cd Demyst/
    ```

2. Run the parser using the following command:
    ```sh
    python -m fixed_width_parser.src.main
    ```

### Running the Tests

1. Navigate to the project directory:
    ```sh
    cd Demyst/
    ```

2. Run the parser using the following command:
    ```sh
    python -m unittest fixed_width_parser.tests.test_parser
    ```