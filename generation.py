from modelClass import Model
import argparse

parser = argparse.ArgumentParser(description='Management assistant')
parser.add_argument('dir', type=str, help='Path to model data')
parser.add_argument('number', type=int, help='Number of words to output')
parser.add_argument('-p', type=str,
                    help='Path to text prefix file', required=False, default='')

model = Model(parser.parse_args().dir)

if parser.parse_args().p == '':
    print(model.generate(parser.parse_args().number))
else:
    print(model.generate(parser.parse_args().number,
                         parser.parse_args().p))
