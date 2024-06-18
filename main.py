import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import mysql.connector
import pandas as pd
from sqlalchemy import create_engine
import requests
import json


db=mysql.connector.connect(
host='localhost',
user='root',
password='root',
database='phonepe'

)
mycursor= db.cursor()


 
query1 = '''SELECT * FROM phonepe.aggtrans;'''
mycursor.execute(query1)
t1=mycursor.fetchall()
Aggtrans= pd.DataFrame(t1,columns=['States','Year','Quater','TransactionType','TransactionCount','TransactionAmount'])


query2 = '''SELECT * FROM phonepe.aggusers;'''
mycursor.execute(query2)
t2=mycursor.fetchall()
Aggusers= pd.DataFrame(t2,columns=['States','Year','Quater','UsersBrand','UsersCount','UsersPercentage'])

query3 = '''SELECT * FROM phonepe.maptrans;'''
mycursor.execute(query3)
t3=mycursor.fetchall()
Maptrans= pd.DataFrame(t3,columns=['States','Year','Quater','Districts','TransCount','TransAmount'])

query4 = '''SELECT * FROM phonepe.mapusers;'''
mycursor.execute(query4)
t4=mycursor.fetchall()
Mapusers= pd.DataFrame(t4,columns=['States','Year','Quater','Districts','UsersRegister','UsersAppopens'])

query5 = '''SELECT * FROM phonepe.toptrans;'''
mycursor.execute(query5)
t5=mycursor.fetchall()
Toptrans= pd.DataFrame(t5,columns=['States','Year','Quater','Pincode','TransCount','TransAmount'])

query6 = '''SELECT * FROM phonepe.topusers;'''
mycursor.execute(query6)
t6=mycursor.fetchall()
Topusers= pd.DataFrame(t6,columns=['States','Year','Quater','Pincode','RegisteredUsers'])





def averageTrans(Amount,q21):
        db=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='phonepe'

        )
        mycursor= db.cursor()


        
        query1 = f'''SELECT * FROM phonepe.aggtrans where Year='{Amount}' and Quater='{q21}';'''
        mycursor.execute(query1)
        t1=mycursor.fetchall()
        mf1= pd.DataFrame(t1,columns=['States','Year','Quater','TransactionType','TransactionCount','TransactionAmount'])
        
        mfs1=mf1.groupby('States')[['TransactionCount','TransactionAmount']].sum()
        mfs1.reset_index(inplace=True)
        col1,col2=st.columns(2)
        with col1:
    
             fig2=px.bar(mfs1,x='States',y='TransactionAmount',title=f'{Amount} Q{q21} Transanction Amount')
             st.plotly_chart(fig2, use_container_width=True)
        with col2:     
            fig3=px.bar(mfs1,x='States',y='TransactionCount',title=f'{Amount} Q{q21} Transanction Count',color_discrete_sequence=px.colors.sequential.Agsunset_r)
            st.plotly_chart(fig3, use_container_width=True)


        url='https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson'

        response= requests.get(url)
        data1=json.loads(response.content)
        states_name=[]
        for feature in data1['features']:
            states_name.append(feature['properties']['ST_NM'])

        states_name.sort()
    
        
        figindia= px.choropleth(mfs1,geojson=data1,locations='States',featureidkey='properties.ST_NM',
                                color='TransactionAmount',color_continuous_scale='deep',
                                range_color=(mfs1['TransactionAmount'].min(),mfs1['TransactionAmount'].max()),
                                hover_name='States',title=f'{Amount} Q{q21} Transanction amount',fitbounds='locations',
                                height=800,width=100)
        figindia.update_geos(visible=False)
        st.plotly_chart(figindia, use_container_width=True)

        
        figindia1= px.choropleth(mfs1,geojson=data1,locations='States',featureidkey='properties.ST_NM',
                                color='TransactionCount',color_continuous_scale='sunset',
                                range_color=(mfs1['TransactionCount'].min(),mfs1['TransactionCount'].max()),
                                hover_name='States',title=f'{Amount} Q{q21} Transanction Count',fitbounds='locations',
                                height=800,width=100)

        figindia1.update_geos(visible=False)
        st.plotly_chart(figindia1, use_container_width=True)
def avgtrans(amount1):
        db=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='phonepe'

        )
        mycursor= db.cursor()


        
        query1 = f'''SELECT * FROM phonepe.aggtrans where Year='{amount1}';'''
        mycursor.execute(query1)
        t1=mycursor.fetchall()
        mf= pd.DataFrame(t1,columns=['States','Year','Quater','TransactionType','TransactionCount','TransactionAmount'])
        mfs1=mf.groupby('States')[['TransactionCount','TransactionAmount']].sum()
        mfs1.reset_index(inplace=True)
       


        url='https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson'

        response= requests.get(url)
        data1=json.loads(response.content)
        states_name=[]
        for feature in data1['features']:
            states_name.append(feature['properties']['ST_NM'])

        states_name.sort()
        

        figindia21= px.choropleth(mfs1,geojson=data1,locations='States',featureidkey='properties.ST_NM',
                                color='TransactionAmount',color_continuous_scale='deep',
                                range_color=(mfs1['TransactionAmount'].min(),mfs1['TransactionAmount'].max()),
                                hover_name='States',title=f'{amount1} Transanction Amount',fitbounds='locations',
                                height=800,width=100)
        figindia21.update_geos(visible=False)
        st.plotly_chart(figindia21, use_container_width=True)

        

    
        figindia31= px.choropleth(mfs1,geojson=data1,locations='States',featureidkey='properties.ST_NM',
                                color='TransactionCount',color_continuous_scale='sunset',
                                range_color=(mfs1['TransactionCount'].min(),mfs1['TransactionCount'].max()),
                                hover_name='States',title=f'{amount1} Transanction Count',fitbounds='locations',
                                height=800,width=100)
        figindia31.update_geos(visible=False)
        st.plotly_chart(figindia31, use_container_width=True)


def usersreg(amount1):
        db=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='phonepe'

        )
        mycursor= db.cursor()



        query4 = f'''SELECT * FROM phonepe.mapusers where Year ='{amount1}';'''
        mycursor.execute(query4)
        t4=mycursor.fetchall()
        mqf= pd.DataFrame(t4,columns=['States','Year','Quater','Districts','UsersRegister','UsersAppopens'])

        mqfs1=mqf.groupby('States')[['UsersRegister']].sum()
        mqfs1.reset_index(inplace=True)
       


        url='https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson'

        response= requests.get(url)
        data1=json.loads(response.content)
        states_name=[]
        for feature in data1['features']:
            states_name.append(feature['properties']['ST_NM'])

        states_name.sort()
        

        figindia51= px.choropleth(mqfs1,geojson=data1,locations='States',featureidkey='properties.ST_NM',
                                color='UsersRegister',color_continuous_scale='ylorrd',
                                range_color=(mqfs1['UsersRegister'].min(),mqfs1['UsersRegister'].max()),
                                hover_name='States',title=f'{amount1} UsersRegister',fitbounds='locations',
                                height=800,width=100)
        figindia51.update_geos(visible=False)
        st.plotly_chart(figindia51, use_container_width=True)     






def mtrans(mAmount,ma19,state):
      db=mysql.connector.connect(
      host='localhost',
      user='root',
      password='root',
      database='phonepe'

      )
      mycursor= db.cursor()



      query3 = f'''SELECT * FROM phonepe.maptrans where Year='{mAmount}' and Quater='{ma19}' and State='{state}';'''
      mycursor.execute(query3)
      t3=mycursor.fetchall()
      ms= pd.DataFrame(t3,columns=['States','Year','Quater','Districts','TransCount','TransAmount'])
      cm1,cm2=st.columns(2)
      with cm1:
            fig1=px.bar(ms,x='Districts',y='TransAmount',title=f'{mAmount} Quater{ma19} {state} Transanction Amount')
            st.plotly_chart(fig1, use_container_width=True)
      with  cm2:
            fig2=px.bar(ms,x='Districts',y='TransCount',title=f'{mAmount} Quater{ma19} {state} Transanction Count')
            st.plotly_chart(fig2, use_container_width=True)
                  
        

def mtrans1(mAmount,state):
        db=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='phonepe'

        )
        mycursor= db.cursor()



        query3 = f'''SELECT * FROM phonepe.maptrans where Year='{mAmount}' and  State='{state}';'''
        mycursor.execute(query3)
        t3=mycursor.fetchall()
        ms= pd.DataFrame(t3,columns=['States','Year','Quater','Districts','TransCount','TransAmount'])
        my=ms.groupby('Districts')[['TransCount','TransAmount']].sum()
        my.reset_index(inplace=True)
        cn1,cn2=st.columns(2)
        with cn1:
                fig1=px.bar(my,x='Districts',y='TransAmount',title=f'{mAmount} {state} Transanction Amount')
                st.plotly_chart(fig1, use_container_width=True)
        with cn2:
             fig2=px.bar(my,x='Districts',y='TransCount',title=f'{mAmount} {state} Transanction Count')
             st.plotly_chart(fig2, use_container_width=True)       

        




             

        
def ttrans(tAmount,State):
        db=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='phonepe'

        )
        mycursor= db.cursor()
        query5 = f'''SELECT * FROM phonepe.toptrans where Year='{tAmount}' and State= '{State}';'''
        mycursor.execute(query5)
        t5=mycursor.fetchall()
        mts= pd.DataFrame(t5,columns=['States','Year','Quater','Pincode','TransCount','TransAmount'])


        fig1=px.bar(mts,x='Quater',y='TransAmount',hover_data='Pincode',title=f'{tAmount} {state} Transanction Amount')
        st.plotly_chart(fig1, use_container_width=True)

        fig2=px.bar(mts,x='Quater',y='TransCount',hover_data='Pincode',title=f'{tAmount} {state} Transanction Count')
        st.plotly_chart(fig2, use_container_width=True)
             


def usersy(UAmount,ustate):
    db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='phonepe'

    )
    mycursor= db.cursor()
    query2 = f'''SELECT * FROM phonepe.aggusers where Year='{UAmount}' and State='{ustate}';'''
    mycursor.execute(query2)
    t2=mycursor.fetchall()
    muts= pd.DataFrame(t2,columns=['States','Year','Quater','UsersBrand','UsersCount','UsersPercentage'])
    mufs=muts.groupby('UsersBrand')[['UsersCount']].sum()
    mufs.reset_index(inplace=True)
    fig15=px.bar(mufs,x='UsersBrand',y='UsersCount',title=f'{UAmount} {ustate} Users Count')
    st.plotly_chart(fig15, use_container_width=True)
    

def usersq(UAmount,ustate,qu):
    db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='phonepe'

    )
    mycursor= db.cursor()
    query2 = f'''SELECT * FROM phonepe.aggusers where Year='{UAmount}'and Quater='{qu}' and State='{ustate}';'''
    mycursor.execute(query2)
    t2=mycursor.fetchall()
    muts= pd.DataFrame(t2,columns=['States','Year','Quater','UsersBrand','UsersCount','UsersPercentage'])

    mufs=muts.groupby('UsersBrand')[['UsersCount']].sum()
    mufs.reset_index(inplace=True)
    fig14=px.bar(mufs,x='UsersBrand',y='UsersCount',title=f'{UAmount} Quater{qu} {ustate} Users Count')
    st.plotly_chart(fig14, use_container_width=True)




def userd (mamount,maw,wstate):
    db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='phonepe'

    )
    mycursor= db.cursor()
    query4 = f'''SELECT * FROM phonepe.mapusers where Year='{mamount}' and Quater='{maw}' and State='{wstate}';'''
    mycursor.execute(query4)
    t4=mycursor.fetchall()
    mutsw= pd.DataFrame(t4,columns=['States','Year','Quater','Districts','UsersRegister','UsersAppopens'])


    fig17=px.bar(mutsw,x='Districts',y='UsersRegister',title=f'{mamount} Quater{maw} {wstate} Users Count')
    st.plotly_chart(fig17, use_container_width=True)

    fig18=px.bar(mutsw,x='Districts',y='UsersAppopens',title=f'{mamount} Quater{maw} {wstate} Users Appopens')
    st.plotly_chart(fig18, use_container_width=True)


def usersdy (mamount,wstate):
    db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='phonepe'

    )
    mycursor= db.cursor()

    query4 = f'''SELECT * FROM phonepe.mapusers where Year='{mamount}' and State='{wstate}';'''
    mycursor.execute(query4)
    t4=mycursor.fetchall()
    mutsq= pd.DataFrame(t4,columns=['States','Year','Quater','Districts','UsersRegister','UsersAppopens'])


    mufsq=mutsq.groupby('Districts')[['UsersRegister','UsersAppopens']].sum()
    mufsq.reset_index(inplace=True)
    fig16=px.bar(mufsq,x='Districts',y='UsersRegister',title=f'{mamount}  {wstate} Users Count')
    st.plotly_chart(fig16, use_container_width=True)
    fig11=px.bar(mufsq,x='Districts',y='UsersAppopens',title=f'{mamount} {wstate} Users Appopens')

    st.plotly_chart(fig11, use_container_width=True)






def topr(uAmount,utstate):
        db=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='phonepe'

        )
        mycursor= db.cursor()

        query6 = f'''SELECT * FROM phonepe.topusers  where Year='{uAmount}' and State='{utstate}';'''
        mycursor.execute(query6)
        t6=mycursor.fetchall()
        mts= pd.DataFrame(t6,columns=['States','Year','Quater','Pincode','RegisteredUsers'])
        fig19=px.bar(mts,x='Quater',y='RegisteredUsers',title=f'{uAmount}  {utstate} Users Count',hover_data='Pincode')
        st.plotly_chart(fig19, use_container_width=True)








st.set_page_config(
    layout='wide'
)
st.title('Phonepe Data Visualization and Exploration')


with st.sidebar:
    select = option_menu("Main Menu",['Home','Explore Data','DropDown Questions'],
                         orientation='horizontal')

if select=="Home":
        amount1=st.radio('select the year',[2018,2019,2020,2021,2022,2023],horizontal=True)
        if amount1==amount1:
                tran=avgtrans(amount1)
                uussera=usersreg(amount1)

                


elif select=="Explore Data":
    page1,page2,page3=st.tabs(["aggregated charts","map charts","top charts"])
    with page1:
            method=st.radio("select the method",["AggUsers Charts","AggTransaction Charts"],horizontal=True)
            if method=='AggUsers Charts':
                  UAmount=st.radio('select the year',[2018,2019,2020,2021,2022,2023],horizontal=True)
                  if UAmount==UAmount:
                        qu=st.radio('select the quater',[1,2,3,4],horizontal=True)
                        ustate= st.selectbox('Select the Districts',Aggusers['States'].unique())
                        uu=usersy(UAmount,ustate)

                        ut=usersq(UAmount,ustate,qu)
                        


                        
                
            elif method=='AggTransaction Charts':
                    Amount=st.radio('select the year',[2018,2019,2020,2021,2022,2023],horizontal=True)
                    if Amount==Amount:
                        q21=st.radio('select the quater',[1,2,3,4],horizontal=True)
                        if q21==q21:
                            transa=averageTrans(Amount,q21)
                    

                
                             

    with page2: 
        method=st.radio("select the method",['MapUsers Charts','MapTransaction Charts'],horizontal=True)
        if method=='MapUsers Charts':
             mamount=st.radio('select the years',[2018,2019,2020,2021,2022,2023],horizontal=True)
             if mamount==mamount:
                    maw=st.radio('select the quaters',[1,2,3,4],horizontal=True)
                    wstate= st.selectbox('Select the District',Mapusers['States'].unique())
                    if wstate==wstate:
                        map2w=usersdy(mamount,wstate)

                        map1e=userd(mamount,maw,wstate)
            
        elif method=='MapTransaction Charts':
                mAmount=st.radio('select the years',[2018,2019,2020,2021,2022,2023],horizontal=True)
                if mAmount==mAmount:
                    ma19=st.radio('select the quaters',[1,2,3,4],horizontal=True)
                    state= st.selectbox('Select The District',Maptrans['States'].unique())
                    if state==state:
                        map2=mtrans1(mAmount,state)

                        map1=mtrans(mAmount,ma19,state)




                


    with page3: 
        method=st.radio("select the method",['TopUsers Charts','TopTransaction Charts'],horizontal=True)
        if method=='TopUsers Charts':
            utAmount=st.radio('Select The Year',[2018,2019,2020,2021,2022,2023],horizontal=True)
            if utAmount==utAmount:
                            utstate= st.selectbox('select the districts',Topusers['States'].unique())
                            utt=topr(utAmount,utstate)
        elif method=='TopTransaction Charts':
                        tAmount=st.radio('Select the years',[2018,2019,2020,2021,2022,2023],horizontal=True)
                        if tAmount==tAmount:
                            state= st.selectbox('select the district',Toptrans['States'].unique())
                            tt=ttrans(tAmount,state)

                                                
elif select=='DropDown Questions':
        question = st.selectbox("select the question",('select question','1.what are the transaction count and transaction type in 2019?',
                                                '2.what are the transaction amount and transaction type in 2019?',
                                                '3.what are the transaction count and  transaction type in 2022?',
                                                '4.what are the transaction amount and transaction type in 2022?',
                                                '5.what are the transaction count and transaction type in 2021?',
                                                '6.what are the transaction amount and transaction type in 2021?',
                                                '7.what are the transaction count and transaction type in 2020',
                                                '8.what are the transaction amount and transaction type in 2020?',
                                                '9.what are the mobile brand used and its percentage in 2021?',
                                                '10.what are the mobile brand used and its percentage in 2022?'))
        if  question =='1.what are the transaction count and transaction type in 2019?':
                        db=mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='root',
                        database='phonepe'

                        )
                        mycursor= db.cursor()
                        query1 = '''SELECT * FROM phonepe.aggtrans where Year=2019;'''
                        mycursor.execute(query1)
                        t1=mycursor.fetchall()
                        muf= pd.DataFrame(t1,columns=['States','Year','Quater','TransactionType','TransactionCount','TransactionAmount'])
                        mufs=muf.groupby('TransactionType')[['TransactionCount']].sum()
                        mufs.reset_index(inplace=True)
                        fig15=px.bar(mufs,x='TransactionType',y='TransactionCount',title=f'{2019} transaction type  Count')
                        st.plotly_chart(fig15, use_container_width=True)
        elif question =='2.what are the transaction amount and transaction type in 2019?':
                        db=mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='root',
                        database='phonepe'

                        )
                        mycursor= db.cursor()
                        query1 = '''SELECT * FROM phonepe.aggtrans where Year=2019;'''
                        mycursor.execute(query1)
                        t1=mycursor.fetchall()
                        af= pd.DataFrame(t1,columns=['States','Year','Quater','TransactionType','TransactionCount','TransactionAmount'])

                        afs=af.groupby('TransactionType')[['TransactionAmount']].sum()
                        afs.reset_index(inplace=True)
                        a2=px.bar(afs,x='TransactionType',y='TransactionAmount',title=f'{2019} transaction type  Amount')
                        st.plotly_chart(a2, use_container_width=True)  
        elif question == '3.what are the transaction count and transaction type in 2022?':
                        db=mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='root',
                        database='phonepe'

                        )
                        mycursor= db.cursor()
                        query1 = '''SELECT * FROM phonepe.aggtrans where Year=2022;'''
                        mycursor.execute(query1)
                        t1=mycursor.fetchall()
                        muf= pd.DataFrame(t1,columns=['States','Year','Quater','TransactionType','TransactionCount','TransactionAmount'])

                        mufs=muf.groupby('TransactionType')[['TransactionCount']].sum()
                        mufs.reset_index(inplace=True)
                        fig15=px.bar(mufs,x='TransactionType',y='TransactionCount',title=f'{2022} transaction type  Count')
                        st.plotly_chart(fig15, use_container_width=True)  
                    
        elif question =='4.what are the transaction amount and transaction type in 2022?':
                        db=mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='root',
                        database='phonepe'

                        )
                        mycursor= db.cursor()
                        query1 = '''SELECT * FROM phonepe.aggtrans where Year=2022;'''
                        mycursor.execute(query1)
                        t1=mycursor.fetchall()
                        af= pd.DataFrame(t1,columns=['States','Year','Quater','TransactionType','TransactionCount','TransactionAmount'])
                        afs=af.groupby('TransactionType')[['TransactionAmount']].sum()
                        afs.reset_index(inplace=True)
                        a2=px.bar(afs,x='TransactionType',y='TransactionAmount',title=f'{2022} transaction type  Amount')
                        st.plotly_chart(a2, use_container_width=True) 
        elif question =='5.what are the transaction count and transaction type in 2021?':
                        db=mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='root',
                        database='phonepe'

                        )
                        mycursor= db.cursor()
                        query1 = '''SELECT * FROM phonepe.aggtrans where Year=2021;'''
                        mycursor.execute(query1)
                        t1=mycursor.fetchall()
                        muf= pd.DataFrame(t1,columns=['States','Year','Quater','TransactionType','TransactionCount','TransactionAmount'])
                        mufs=muf.groupby('TransactionType')[['TransactionCount']].sum()
                        mufs.reset_index(inplace=True)
                        fig15=px.bar(mufs,x='TransactionType',y='TransactionCount',title=f'{2021} transaction type  Count')
                        st.plotly_chart(fig15, use_container_width=True)     
        elif question =='6.what are the transaction amount and transaction type in 2021?':
                        db=mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='root',
                        database='phonepe'

                        )
                        mycursor= db.cursor()
                        query1 = '''SELECT * FROM phonepe.aggtrans where Year=2021;'''
                        mycursor.execute(query1)
                        t1=mycursor.fetchall()
                        af= pd.DataFrame(t1,columns=['States','Year','Quater','TransactionType','TransactionCount','TransactionAmount'])
    
                        afs=af.groupby('TransactionType')[['TransactionAmount']].sum()
                        afs.reset_index(inplace=True)
                        a2=px.bar(afs,x='TransactionType',y='TransactionAmount',title=f'{2021} transaction type  Amount')
                        st.plotly_chart(a2, use_container_width=True) 
        elif question =='7.what are the transaction count and transaction type in 2020':
                        db=mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='root',
                        database='phonepe'

                        )
                        mycursor= db.cursor()
                        query1 = '''SELECT * FROM phonepe.aggtrans where Year=2020;'''
                        mycursor.execute(query1)
                        t1=mycursor.fetchall()
                        muf= pd.DataFrame(t1,columns=['States','Year','Quater','TransactionType','TransactionCount','TransactionAmount'])
    
                        mufs=muf.groupby('TransactionType')[['TransactionCount']].sum()
                        mufs.reset_index(inplace=True)
                        fig15=px.bar(mufs,x='TransactionType',y='TransactionCount',title=f'{2020} transaction type  Count')
                        st.plotly_chart(fig15, use_container_width=True)
        elif question =='8.what are the transaction amount and transaction type in 2020?':
                        db=mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='root',
                        database='phonepe'

                        )
                        mycursor= db.cursor()
                        query1 = '''SELECT * FROM phonepe.aggtrans where Year=2020;'''
                        mycursor.execute(query1)
                        t1=mycursor.fetchall()
                        af= pd.DataFrame(t1,columns=['States','Year','Quater','TransactionType','TransactionCount','TransactionAmount'])
                        
                        afs=af.groupby('TransactionType')[['TransactionAmount']].sum()
                        afs.reset_index(inplace=True)
                        a2=px.bar(afs,x='TransactionType',y='TransactionAmount',title=f'{2020} transaction type  Amount')
                        st.plotly_chart(a2, use_container_width=True) 
        elif question =='9.what are the mobile brand used and its percentage in 2021?':
                    db=mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='root',
                    database='phonepe'

                    )
                    mycursor= db.cursor()
                    query2 = '''SELECT * FROM phonepe.aggusers;'''
                    mycursor.execute(query2)
                    t2=mycursor.fetchall()
                    af10= pd.DataFrame(t2,columns=['States','Year','Quater','UsersBrand','UsersCount','UsersPercentage'])
                    a19=px.pie(af10,names='UsersBrand',values='UsersPercentage',title=f'{2021} brand percentage')
                    st.plotly_chart(a19, use_container_width=True)
        elif question =='10.what are the mobile brand used and its percentage in 2022?':
                    db=mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='root',
                    database='phonepe'

                    )
                    mycursor= db.cursor()
                    query2 = '''SELECT * FROM phonepe.aggusers where Year=2022;'''
                    mycursor.execute(query2)
                    t2=mycursor.fetchall()
                    af10= pd.DataFrame(t2,columns=['States','Year','Quater','UsersBrand','UsersCount','UsersPercentage'])
                    af9=Aggusers[Aggusers['Year']==2022]
                    af9.reset_index(drop=True,inplace=True)
                    a9=px.pie(af9,names='UsersBrand',values='UsersPercentage',title=f'{2022} brand percentage')
                    st.plotly_chart(a9, use_container_width=True)



      
                 

    
