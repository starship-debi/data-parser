import argparse
import json
import logging
import os
import sys

# Set up logging
logging.basicConfig(
    format='%(asctime)s [%(levelname)s] %(message)s',
    level=logging.INFO,
    stream=sys.stdout
)

# Define constants
DATA_DIR = 'data'
OUTPUT_FILE = 'parsed_data.json'

def parse_args():
    parser = argparse.ArgumentParser(description='Data parser')
    parser.add_argument('--input-file', required=True, help='Input file to parse')
    parser.add_argument('--output-file', default=OUTPUT_FILE, help='Output file to write parsed data to')
    return parser.parse_args()

def load_data(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        logging.error(f'Failed to parse JSON: {e}')
        sys.exit(1)

def parse_data(data):
    # Assuming 'data' is a list of dictionaries
    parsed_data = []
    for item in data:
        # Example parsing logic
        parsed_item = {
            'id': item['id'],
            'name': item['name'],
            'description': item['description']
        }
        parsed_data.append(parsed_item)
    return parsed_data

def save_data(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    args = parse_args()
    input_file = args.input_file
    output_file = args.output_file

    data_dir = os.path.dirname(input_file)
    if data_dir and not os.path.exists(data_dir):
        os.makedirs(data_dir)

    data = load_data(input_file)
    parsed_data = parse_data(data)
    save_data(parsed_data, output_file)

    logging.info(f'Parsed data saved to {output_file}')

if __name__ == '__main__':
    main()