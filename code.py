from time import sleep
from hashlib import md5
from os import listdir

src_dir= 'myfiles'
my_files = listdir(src_dir)

#create hash for files
def get_file_hash(filename):
       return md5(open(filename,'rb').read()).hexdigest()

file_data = {}

def load_files():
       for filename in my_files:
              file_hash = get_file_hash(f'{src_dir}/{filename}')
              file_data[filename] = file_hash

load_files()
def check_changes():
        for filename in my_files:
              file_hash = get_file_hash(f'{src_dir}/{filename}')
              if file_data[filename] != file_hash:
                     print(f'change detected in file {filename}')
sleep(1)
check_changes()       

