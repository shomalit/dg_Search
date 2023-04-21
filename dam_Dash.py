#from main_package import find_Dj
from asyncio import sleep
from distutils.log import debug
from imp import reload
from msilib.schema import Component
from pickle import APPEND
from pickletools import int4
import find_Djk
from dash import Dash,dcc,Input,Output
import dash_bootstrap_components as dbc
from dash import html #import dash_html_components as html
from dash import dash_table #import dash_table
import plotly.graph_objects as go
import time
# Variable area
u_Q ='' #user query
# Functions environment
def price_Xchang():
    '''Return int list of prices'''
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
    ''' for l in prices:
        print(f'type={type(l)}\t{l}\t') '''
    return prices

# Call area
    #find_Djk.dj_Search('رادیو') #use after get user query from dash
app =Dash(__name__,external_stylesheets=[dbc.themes.DARKLY])
my_div =html.Div()
my_graph = dcc.Graph(figure={})
my_input = dbc.Input(value='عبارت جستجو',style={'color':'blue','text-align':'right'})
my_btn  = dbc.Button('Search',style={'width':'100px','height':'35px','margin-top':'25px','margin-down':'25px'})
my_btn_rst  = dbc.Button('Reset',style={'width':'100px','height':'35px','margin-top':'25px','margin-down':'25px','margin-left':'20px'})
my_text1 = html.H3('Student Shomali Damon',style={'color':'yellow'})
 
@app.callback(
Output(my_div,component_property='children'),
Output(my_btn,component_property='n_clicks'),
Output(my_graph,component_property='figure'),
Input(my_btn,component_property='n_clicks'),
Input(my_input,component_property='value')
)
def create_table(n_clicks,q_Str):
    #n=int(n_clicks)
    rows=[]
    if n_clicks:
        print(f'mmm1000---{q_Str}')
        find_Djk.dj_Search(q_Str)   # Does djikala search and make file.txt
        time.sleep(5)
        print('mmm1001')
        rows=[html.Tr([html.Th('تصویر'),html.Th('قیمت'),html.Th('عنوان'),html.Th('شماره'),])]

        with open('price.txt','r',encoding='utf-8') as f:
            prices=f.read().split('\n')
            f.close()
        with open('titles.txt','r',encoding='utf-8') as f:
            titles=f.read().split('\n')
            f.close()
        with open('refs.txt','r',encoding='utf-8') as f:
            links=f.read().split('\n')
            f.close()
        with open('img_src.txt','r',encoding='utf-8') as f:
            sources=f.read().split('\n')
            f.close()    
        for i,p,t,l,img_s in zip(range(0,len(prices)),prices,titles,links,sources) :
            img = html.Img(src=img_s,width='50px',height='50px')
            d = html.Tr([html.Td(img),html.Td('تومان'+p),html.Td(html.A(t,href=l)),html.Td(i),])
            rows.append(d)
        print('----Cmm1002----')
        prs_Int=price_Xchang()   # make int list of prices for plot
        print('----Cmm1003----')
        figure=go.Figure(data=go.Scatter(x=list(range(0,len(prs_Int))),y=prs_Int))
        print('----Cmm1004----')
        #reset lists
        prs_Int=[]
        prices=[]
        titles=[]
        links=[]
        sources=[]
        children=[html.Table(rows,style={'width':'100%','border':'solid'})]
    else:
        print('----Error 201----')
        
    return children ,n_clicks,figure


app.layout=dbc.Container([
    dbc.Row([my_text1,my_input,my_btn,my_div,my_graph],className='text-center')
])
if __name__=='__main__' :
    app.run_server(port='8005',debug=True)    #debug=True
    

