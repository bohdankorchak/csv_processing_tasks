# csv_processing_tasks

This project contains three Python scripts for working with CSV files:

1. **[convert-tsv-to-csv.py](convert-tsv-to-csv.py)** – Converts TSV file to CSV.
2. **[csv-task.py](csv-task.py)** – Transforms CSV file data, adds `price_edited` column.
3. **[regex-task.py](regex-task.py)** – Filters CSV files based on specified criteria using regex.

## Requirements

- Python 3.8 and above

## Usage

The scripts are executed from the terminal with parameters for specifying the paths to the input and output files.

### Running [convert-tsv-to-csv.py](convert-tsv-to-csv.py)
```bash
python convert-tsv-to-csv.py --infile python_home_task_file.tsv --out python_home_task_file.csv
```

### Running [csv-task.py](csv-task.py)
```bash
python csv-task.py --infile python_home_task_file.csv --out python_home_task_file_with_price.csv
```

### Running [regex-task.py](regex-task.py)
```bash
python regex-task.py --infile python_home_task_file.csv --out python_home_task_file_regex.csv
```
