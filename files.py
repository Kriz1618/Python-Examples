from datetime import datetime
import json

def read_lines(file):
    print('4', 'file', file)
    while file:
        line = file.readline()
        print('Line content: {}'.format(line))
        if not line:
            break
    # print(line for line in file.readline())

def write_if_not_exist(file: str):
    with open(file, 'r+', encoding="utf-8") as f:
        print('14', 'f.readable()', f.readable())
        data = f.read()
        print('10', 'data', type(data), f.readline(), data)
        if f:
            read_lines(f)
            f.writelines('Hi at {}\n'.format(datetime.now()))
        else:
            print(f'File {file} not found')

def clear_file(file: str):
    with open(file, 'w', encoding="utf-8") as f:
        f.write('')    
        
# clear_file('file.txt')
write_if_not_exist('file.txt')

def dump_file():
    x = [1, 'simple', 'list']
    st = json.dumps(x)
    print('34', 'st', st)
    
# dump_file()

def update_json(file, x):
   with open(file, 'w+', encoding="utf-8") as f:
       json.dump(x, f)

def decode_json(file):
    with open(file, 'r', encoding='utf-8') as f:
        content = json.load(f)
        print('45', 'content', content, type(content))
    
# update_json('file.json', { 'x': 33 })
# decode_json('file.json')