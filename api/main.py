import click
import logging
from data_parser.config import Config
from data_parser.parser import Parser
from data_parser.writer import Writer

@click.command()
@click.option('--config', default='config.yaml', help='Path to the configuration file')
@click.option('--input-file', required=True, help='Path to the input data file')
@click.option('--output-file', required=True, help='Path to the output data file')
def main(config, input_file, output_file):
    logging.basicConfig(level=logging.INFO)
    config = Config(config)
    parser = Parser(config)
    data = parser.parse(input_file)
    writer = Writer(config)
    writer.write(data, output_file)

if __name__ == '__main__':
    main()