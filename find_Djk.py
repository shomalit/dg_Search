#ITNOTG
from ast import Del
import os
import time
import requests
import selenium
import my_Functions as MF
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from unidecode import unidecode

#Function area
def kesy_Hlp():
    #request
    # You can make your own url by link https://www.digikala.com/search/?q
    #'https://www.digikala.com/search/?q='+usr_Phrase 
    # 'https://www.digikala.com'
    #search Proccess
    # Class of Main frame product-list_ProductList__item__LiiNI
    # Class of img d-flex grow-1 pos-relative flex-column
    # Class of Price d-flex ai-center jc-end gap-1 color-700 color-400 text-h5 grow-1
    # class of title ellipsis-2 text-body2-strong color-700 styles_VerticalProductCard__productTitle__6zjjN
    # input box= px-2 TextField_TextField__input__hFMFl text-subtitle w-100 TextField_TextField__bwN9_ TextField_TextField--primary__IZ6Ku color-500 text-body-2 text-body-2
    # px-2 TextField_TextField__input__hFMFl text-subtitle w-100 TextField_TextField__bwN9_ TextField_TextField--primary__IZ6Ku color-500 text-body-2 text-body-2
    # Answerd ** .pos-relative.d-inline-flex.py-2.pr-2.pl-0.p-2-lg.bg-000.radius
    # test input Answerd ** box color-500 d-flex ai-center text-body-2
    pass
def page_Load_init(q):
    usr_Url='https://www.digikala.com'+usr_Phrase  #Make url 
    #print(f'{usr_Url}',end='')
    path = 'chromedriver.exe'
    op = webdriver.ChromeOptions()
    op.add_argument('--disable-gpu')
    d = webdriver.Chrome(executable_path=path,chrome_options=op)
    d.get(usr_Url)
    time.sleep(15)
    d.maximize_window()
    # Make wait timout to load page
    cart_a = WebDriverWait(d,100).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.color-500.d-flex.ai-center.text-body-2')))
    #cart_a.send_keys(Keys.ESCAPE)
    cart_a.click()  #first- click in div of search box 
    time.sleep(2)
    # Type(send) in text box for search and Enter
    cart_b = WebDriverWait(d,100).until(EC.visibility_of_element_located((By.NAME,'search-input')))
    cart_b.send_keys(q)
    time.sleep(3)
    cart_b.send_keys(Keys.ENTER)
    time.sleep(5)
    d.execute_script('window.scrollTo(0,3500)')
    time.sleep(8)
    return d
def find_Src(dr):
    img_Tag=[]
    img_Tag = dr.find_elements(By.CSS_SELECTOR,'.w-100.radius-medium.d-inline-block.lazyloaded')
    img_cnt = len(img_Tag)
    cnt = 0
    if img_cnt > 0 :
        src_List=[]
        for item in img_Tag :
            p_Src = item.get_attribute('src')
            src_List.append(p_Src)
            cnt +=1
            if cnt== img_cnt or cnt == 31 :
                with open('img_src.txt','w',encoding='utf-8') as f:
                    for elm in src_List :
                        str=elm+'\n'
                        f.write(str)
                    f.close()
                    
                break
    else :
        print ('Not found src')
def find_Price(dr):
    p_Div=[]
    p_Div = dr.find_elements(By.CSS_SELECTOR,'.d-flex.ai-center.jc-end.gap-1.color-700.color-400.text-h5.grow-1')
    p_cnt = len(p_Div)
    cnt = 0
    if p_cnt > 0 :
        price_List=[]
        for item in p_Div :
            celm='' # clear elm (clear number)
            p_Span = item.find_element(By.TAG_NAME,'span')
            price = p_Span.get_attribute('innerHTML')
            price_List.append(price)
            cnt +=1
            if cnt==p_cnt or cnt == 31 :
                with open('price.txt','w',encoding='utf-8') as f:
                    for elm in price_List:
                        for l in elm :
                            if l !=',':
                                celm +=l
                            else:
                                pass
                        str=celm+'\n'
                        f.write(str)
                        celm=''
                    f.close()
                break
    else :
        print('Not found price')
def find_Title(dr):
    title_H=[]
    title_H = dr.find_elements(By.CSS_SELECTOR,'.ellipsis-2.text-body2-strong.color-700.styles_VerticalProductCard__productTitle__6zjjN')
    t_cnt = len(title_H)
    cnt = 0
    if t_cnt > 0 :
        title_List=[]
        for item in title_H :
            p_Title = item.get_attribute('innerHTML')
            title_List.append(p_Title)
            cnt +=1
            if cnt ==t_cnt or cnt == 31 :
                with open('titles.txt','w',encoding='utf-8') as f:
                    for tit in title_List:
                        str=tit+'\n'
                        f.write(str)
                    f.close()
                break
    else :
        print('not found title')
def find_href(dr):
    refs=[]
    refs = dr.find_elements(By.CSS_SELECTOR,'.d-block.pointer.pos-relative.bg-000.overflow-hidden.grow-1.py-3.px-4.px-2-lg.h-full-md.styles_VerticalProductCard--hover__ud7aD')
    href_cnt =len(refs)
    cnt = 0
    if href_cnt > 0 :
        href_List=[]
        for item in refs :
            #tag_a = item.find_element(By.TAG_NAME,'a')
            ancr = item.get_attribute('href')
            href_List.append(ancr)
            cnt +=1
            #print(ancr)
            if cnt == href_cnt or cnt ==31 :
                with open('refs.txt','w',encoding='utf-8') as f:
                    for r in href_List :
                        str=r+'\n'
                        f.write(str)
                    f.close()
        
                break
    else:
        print('Could not find any href')
def write_Data():
    fd = open('tmp.txt','w',encoding='utf-8')
    for t in range(0,30) :
        line_Str = title_List[t]+'\t'+href_List[t]+'\t'+price_List[t]+'\t'+src_List[t]+'\n'
        fd.write(line_Str)
        line_Str=''
    fd.close()
def dj_Search(query):
    try :
        u_Query=query
        driver=page_Load_init(u_Query) #load page    
        find_Src(driver)
        find_href(driver)              #Finding image sources
        find_Title(driver)            #Finding Title
        find_Price(driver)            # Finding price
        #write_Data()
    except:
        print('\n Error 102 check Main .')
    else:
        pass

#Variable Environment
title_List=[]   #listed product title
price_List=[]   #listed product price  
src_List = []   #listed product image src
href_List =[]
data_List= []
line_Str = ''   #make line of product`s title,price,image source
usr_Phrase =''#'رادیو' #You should get it from dash or user
#e ='ساعت'

#dj_Search(e)
## Main
'''try :
    driver=page_Load_init() #load page    
    find_Src(driver)              #Finding image sources
    find_Title(driver)            #Finding Title
    find_Price(driver)            # Finding price
    write_Data()
except:
    print('\n Error 102 check Main .')
else:
    pass '''
