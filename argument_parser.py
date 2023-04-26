import argparse
import os

# Custom function to convert input string into a list of paths
def paths_list(string):
    paths = string.split(',')
    return [os.path.abspath(path) for path in paths]

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
# parser.add_argument('--folders_list', metavar='+', type=str, help='List of folders')
parser.add_argument('--paths', type=paths_list, help='List of paths separated by commas')
args = parser.parse_args()
print(args.accumulate(args.integers), args.paths)