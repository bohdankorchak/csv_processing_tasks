import argparse
import csv


def convert(input_file, output_file):
    with open(input_file) as tsv_in, open(output_file, 'w') as csv_out:
        reader = csv.reader(tsv_in, delimiter='\t')
        writer = csv.writer(csv_out, delimiter=',')
        writer.writerows(reader)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CSV Task')
    parser.add_argument('--infile', help='Input TSV file')
    parser.add_argument('--out', help='Output CSV file')
    args = parser.parse_args()

    convert(args.infile, args.out)
