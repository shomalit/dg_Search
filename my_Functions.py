def make_Int(list):
    '''Get str list of price
       clear list and return int list 
    '''
    price_Int = []
    tmp_Str = ''
    for item in list:
        
        for l in item :
            if l !=',' :
                tmp_Str+=l
            else:
                pass
        price_Int.append(int(tmp_Str))
        #print(f'item is {type(item)} {item} len is {len(item)} Clear {tmp_Str} \n')
        tmp_Str=''
    return price_Int
def open_Data_txt():
    try:
        fd=open('price.txt','r',encoding='utf-8')
        line_Str =fd.readline()
        price_List =[]
        while line_Str !='' :
            l=line_Str.split('\t')
            price=l[1]  #price index is 1
            price_List.append(price)
            line_Str =fd.readline()
        fd.close()
        #print(price_List,end=' ')
        price_Int_list = make_Int(price_List)
        sum=0
        for item in price_Int_list :
            sum +=item
            print(f'Price is={item} \n')
        print(f'summary ={sum} \n') 
    except:
        print('Error X100 ')
    else:
        print('Try has finished .')
    return price_Int_list
#open_Data_txt() # Return prices int list