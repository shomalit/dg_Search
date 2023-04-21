from pickletools import float8
from unidecode import unidecode

def open_Read():
    prices=[]
    sum=0
    fd=open('price.txt','r',encoding='utf-8')
    line=''
    line=fd.readline().rstrip('\n')
    while line !='':
        m=int(line)
        prices.append(m)
        line=fd.readline().rstrip('\n')
    fd.close()
    for l in prices:
        print(f'type={type(l)}\t{l}\t')
        
    
  



# Run & Recall function
open_Read()