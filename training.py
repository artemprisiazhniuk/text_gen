import pickle
from modelClass import Model
import argparse

parser = argparse.ArgumentParser(description='Management assistant')
parser.add_argument('indir', type=str, help='Path to input text for model training')

model = Model()
model.fit(parser.parse_args().indir)

with open('data.txt', 'wb') as data:
    pickle.dump(model.dictionary, data)
