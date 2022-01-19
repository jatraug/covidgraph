'''
mkbatch.py - use .env to produce the batch.txt file
'''
import os
from dotenv import load_dotenv
load_dotenv()

def mkbatch():
    print('cd htdocs')
    print('cd apps/covid')
    print(f'lcd {os.environ.get("COVWORK")}/html')
    print('put indexDB.html index.html')
    print('cd images')
    print('rm *jpg')
    print('lcd ../images')
    print('mput *')






def main():
    mkbatch()
    

if __name__ == '__main__':
    main()
