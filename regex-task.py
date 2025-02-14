import argparse
import csv
import re

pattern = re.compile(r'(?i)^(?=.*\bknit)(?!.*\bjumper).*$')


def filter(input_file, output_file):
    with open(input_file, 'r') as input_csv, open(output_file, 'w') as output_csv:
        reader = csv.reader(input_csv)
        writer = csv.writer(output_csv)

        header = next(reader)
        writer.writerow(header)

        for row in reader:
            if pattern.match(' '.join(row)):
                writer.writerow(row)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Regex Task')
    parser.add_argument('--infile', help='Input file')
    parser.add_argument('--out', help='Output file')
    args = parser.parse_args()

    filter(args.infile, args.out)
