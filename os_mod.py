import os
import shutil
import time

def basics():
    print(os.getcwd())
    # os.chdir('~/Downloads')
    print('6', 'os.system(\'ls -l\')', os.system('ls -l'))
    
# basics()

def ex():
    print('dir', dir(os))
    print('help', help(os))
    
# ex()

def ex1():
    shutil.copyfile('file.txt', 'copied.txt')
    # shutil.move('/Downloads/', 'copied.txt')
    time.sleep(4)
    os.system('rm copied.txt')
    
# ex1()

import glob
import sys

def ex2():
    print(glob.glob('file.*'))
    print(sys.argv)
    
# ex2()

import argparse

def ex3():
    parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
    parser.add_argument('filenames', nargs='+')
    parser.add_argument('-l', '--lines', type=int, default=10)
    args = parser.parse_args()
    print(args)
    # run by python os_mod.py --lines=5 file.txt file.json
    
# ex3()

def ex4():
    sys.stderr.write('Warning, log file not found starting a new one\n')
    
# ex4()

import re

def ex5():
    print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
    print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in in the the hat'))
    print('tea for too'.replace('too', 'two'))

# ex5()

import math
import random

def ex6():
    print(math.cos(math.pi / 4))
    print(math.log(1024, 2), '\n')
    print(random.choice(['apple', 'pear', 'banana']))
    print(random.choice(['apple', 'pear', 'banana']))
    print(random.sample(range(100), 10))
    print(random.random())
    print(random.randrange(6))
    print(random.randrange(6))
    
# ex6()

import statistics

def ex7():
    data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
    print(statistics.mean(data), '\n', statistics.median(data), '\n', statistics.variance(data))
    
# ex7()

from urllib.request import urlopen

def ex8():
    with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
        for line in response:
            line = line.decode()             # Convert bytes to a str
            if line.startswith('datetime'):
                print(line.rstrip())         # Remove trailing newline
                
# ex8()

import smtplib

def ex9(to):
    server = smtplib.SMTP('localhost')
    server.sendmail('krizmarles@yopmail.com', to,
    """To: jcaesar@example.org
    From: soothsayer@example.org

    Beware the Ides of March.
    """)
    server.quit()

# ex9('christian@yopmail.com')

from datetime import date

def ex10():
    now = date.today()
    print('115', 'now', now)
    print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
    
    birthday = date(1964, 7, 31)
    age = now - birthday
    print('120', 'age.days', age.days)
    
ex10()

import zlib

def exm():
    s = b'witch which has which witches wrist watch'
    print('128', 'len(s)', len(s))

    t = zlib.compress(s)
    print('131', 'len(t)', len(t))

    print('133', 'zlib.decompress(t)', zlib.decompress(t))

    print('135', 'zlib.crc32(s)', zlib.crc32(s))
# exm()

from timeit import Timer

def exm1():
    print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit(), '\n', Timer('a,b = b,a', 'a=1; b=2').timeit())
    
# exm1()

import doctest
import unittest

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

class TestStatisticalFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)
            
doctest.testmod()
unittest.main()