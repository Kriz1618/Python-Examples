import zipfile
import os

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        print('7', 'root, dirs, files', root, dirs, files)
        for file in files:
            print(os.path.abspath(path), file, os.path.join(root, file))
            ziph.write(os.path.join(root, file))

# Example usage
if __name__ == '__main__':
    zipf = zipfile.ZipFile('my_archive.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('send_email', zipf)
    zipf.write('file.txt', 'file.txt')
    print('Zip created')
    zipf.close()