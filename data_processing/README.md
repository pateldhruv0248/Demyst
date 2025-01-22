# Fixed Width Parser

## Overview

`data_processing` is a Python module designed to generate and handle large CSV datasets. It uses spark to anonymize the data into smaller chunks and smaller files displayed into various smaller CSV files.

## Features

- Generate a large CSV file with  first_name, last_name, address, date_of_birth using chunks where size of chunks can be changed.
- Using PySpark, this large file is converted into smaller chunks of CSV files using distributed technology.
- The data is anionymized using SHA256

## Instructions

### Prerequisites

1. Ensure you have [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) installed on your machine.
2. Ensure Python 3.10 is available in Conda.

### Setting Up the Environment

1. Navigate to the project directory:
    ```sh
    cd Demyst/data_processing
    ```

2. Create a Conda environment:
    ```sh
    conda create --name venv python=3.10
    ```

3. Activate the Conda environment:
    ```sh
    conda activate venv
    ```

4. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Program

1. Ensure you are in the project directory:
    ```sh
    cd Demyst/data_processing
    ```

2. Run the main script:
    ```sh
    python main.py
    ```

### Additional Notes

- **Python Version**: This project uses Python 3.10. Ensure you create the Conda environment with this version.
- **Dependencies**: All required dependencies are listed in `requirements.txt` and will be installed using `pip install -r requirements.txt`.
