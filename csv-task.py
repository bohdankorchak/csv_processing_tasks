import argparse
import csv


class CSVProcessor:

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def process(self):
        data = self.read()
        processed = self.transform(data)
        self.save(processed)

    def read(self):
        with open(self.input_file) as csv_in:
            reader = csv.DictReader(csv_in)
            data = list(reader)
        return data

    def transform(self, data):
        for row in data:
            try:
                row['price_edited'] = float(row.get('search_price', float(0)))
            except (ValueError, KeyError):
                row['price_edited'] = float(0)
        return data

    def save(self, data):
        with open(self.output_file, 'w') as csv_out:
            writer = csv.DictWriter(csv_out, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CSV Task')
    parser.add_argument('--infile', help='Input CSV file')
    parser.add_argument('--out', help='Output CSV file')
    args = parser.parse_args()

    CSVProcessor(args.infile, args.out).process()
