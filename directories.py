import os
print(os.getcwd())
print(os.getcwdb())

os.chdir('/home/kriz/Documents/')
print('6', 'os.listdir()', os.listdir())

os.mkdir('test-folder')

os.rename('test-folder', 'new-folder')

# os.remove('Test.txt')
os.rmdir('new-folder')

os.chdir('/home/kriz/Documents/Python/Python-Examples/')