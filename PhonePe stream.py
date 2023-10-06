import pandas as pd
import sqlalchemy
import streamlit as st
import pymysql 
import plotly.express as px
from plotly.subplots import make_subplots
from PIL import Image
from streamlit_option_menu import option_menu
engine = sqlalchemy.create_engine('mysql+pymysql://root:Surya123@localhost/phonepe')

image = Image.open("D:\PhonePe-Logo. jpg.png")
st.set_page_config(page_title= "Phonepe Pulse Data Visualization",
                   page_icon= image,
                   layout= "wide"
                   )

primaryColor = "#FF4B4B"
backgroundColor = "#6739B7"
secondaryBackgroundColor = "#18184C"
textColor = "#FFFFFF"


mydb = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="Surya123",
    database="phonepe" ) 


cursor = mydb.cursor()
image = Image.open('D:\PhonePe-Logo. jpg.png')

st.sidebar.image(image, use_column_width=True)

st.sidebar.header(":wave: :violet[**Welcome to the Dashboard**]")

st.header ("Phonepe Pulse Data Visualization and Exploration", divider='rainbow')
a = st.sidebar.selectbox('**Category**',('None','State', 'District'))
b = st.sidebar.selectbox('**Type**',('None','Transaction', 'User'))
c = st.sidebar.selectbox('**Year**',('None','2018', '2019','2020', '2021', '2022'))
d = st.sidebar.selectbox('**Quarter**',('None','1', '2','3', '4'))



if a == 'State' and b == 'Transaction':

    col1,col2 = st.columns([2,2],gap="medium")

    with col1:    
        
        aa = pd.read_sql_query(f"select sum(Amount) as Total_Transaction from map_trans where year = '{c}' and quarter = '{d}'",engine)
        df = pd.DataFrame(aa)
        st.write("##### **Total Transaction Amount :**", df['Total_Transaction'][0])


    with col2:
        aa = pd.read_sql_query(f"select Avg(Amount) as Avg_value from map_trans where year = '{c}' and quarter = '{d}'", engine)
        df = pd.DataFrame(aa)
        st.write("##### **Avg Transaction Amount :**", df['Avg_value'][0])


    col1,col2 = st.columns([2,2],gap="medium")

    with col1:    
        aa = pd.read_sql_query(f"select sum(count) as Total_Count from map_trans where year = '{c}' and quarter = '{d}'", engine)
        df = pd.DataFrame(aa)
        st.write("##### **Total Transaction Count :**", df['Total_Count'][0])


    with col2:
        aa = pd.read_sql_query(f"select Avg(count) as Avg_Count from map_trans where year = '{c}' and quarter = '{d}'", engine)
        df = pd.DataFrame(aa)
        st.write("##### **Avg Transaction Count :**", df['Avg_Count'][0])

    col1,col2 = st.columns([2,2],gap="medium")

    with col1:  
        st.subheader("Transaction Count ")

        aa = pd.read_sql_query(f"select State, sum(Transaction_count) as T_count, sum(Transaction_amount) as T_amount from Agg_trans where year = '{c}' and quarter = '{d}' group by state ", engine)
        df = pd.DataFrame(aa)

        fig = px.choropleth(
            df,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='T_count',
            color_continuous_scale='Reds',

        )

        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig,use_container_width=True)



    with col2:    

        st.subheader("Transaction Amount ")

        aa = pd.read_sql_query(f"select State, sum(Transaction_count) as T_count, sum(Transaction_amount) as T_amount from Agg_trans where year = '{c}' and quarter = '{d}' group by state ", engine)
        df = pd.DataFrame(aa)

        fig = px.choropleth(
            df,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='T_amount',
            color_continuous_scale='Reds'
        )

        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig,use_container_width=True)



    st.header(" Transaction Type")

    col1,col2 = st.columns([2,2],gap="medium")


    with col1:    
        st.subheader("Transaction Count")

        aa = pd.read_sql_query(f"select Transaction_type, sum(Transaction_count) as T_count, sum(Transaction_amount) as T_amount from Agg_trans where year = '{c}' and quarter = '{d}' group by Transaction_type order by T_count Desc", engine)
        df = pd.DataFrame(aa)
        fig = px.bar(df, x='Transaction_type', y='T_count', color = 'T_count',  color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(fig,use_container_width=True)

    with col2:    
        st.subheader("Transaction Amount")

        aa = pd.read_sql_query(f"select Transaction_type, sum(Transaction_count) as T_count, sum(Transaction_amount) as T_amount from Agg_trans where year = '{c}' and quarter = '{d}' group by Transaction_type order by T_amount Desc", engine)
        df = pd.DataFrame(aa)
        fig = px.bar(df, x='Transaction_type', y='T_amount', color = 'T_amount', color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(fig,use_container_width=True)



    st.header ('States')

    col1,col2 = st.columns([2,2],gap="medium")

    with col1:    
        st.subheader("Top 10 States by Total Count")

        aa = pd.read_sql_query(f"select state, sum(Transaction_count) as T_count, sum(Transaction_amount) as T_amount from Agg_trans where year = '{c}' and quarter = '{d}' group by state order by T_count desc limit 10", engine)
        df = pd.DataFrame(aa)
        fig = px.pie(aa, names='state', values='T_count', color_discrete_sequence=px.colors.sequential.Agsunset)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig,use_container_width=True)

    with col2:    
        st.subheader("Top 10 States by Total Amount")

        aa = pd.read_sql_query(f"select state, sum(Transaction_count) as T_count, sum(Transaction_amount) as T_amount from Agg_trans where year = '{c}' and quarter = '{d}' group by state order by T_amount desc limit 10", engine)
        df = pd.DataFrame(aa)
        fig = px.pie(aa, names='state', values='T_amount', color_discrete_sequence=px.colors.sequential.Agsunset)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig,use_container_width=True)

    st.header ('Districts')


    col1,col2 = st.columns([2,2],gap="medium")

    with col1:
        st.subheader("Top 10 Districts by Total Count")       

        aa = pd.read_sql_query(f"select district , sum(Count) as T_count, sum(Amount) as T_amount from map_trans where year ='{c}' and quarter = '{d}' group by district order by T_count desc limit 10",engine)
        df = pd.DataFrame(aa)
        fig = px.pie(aa, names='district', values='T_count',color_discrete_sequence=px.colors.sequential.Agsunset)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig,use_container_width=True)

    with col2:
        st.subheader("Top 10 Districts by Total Amount")

        aa = pd.read_sql_query(f"select district , sum(Count) as T_count, sum(Amount) as T_amount from map_trans where year ='{c}' and quarter = '{d}' group by district order by T_amount desc limit 10",engine)
        df = pd.DataFrame(aa)
        fig = px.pie(aa, names='district', values='T_amount',color_discrete_sequence=px.colors.sequential.Agsunset)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig,use_container_width=True)

    st.header ('Pincodes')


    col1,col2 = st.columns([2,2],gap="medium")

    with col1:
        st.subheader("Top 10 Pincodes by Total Count")

        aa = pd.read_sql_query(f"select pincode , sum(Transaction_count) as T_count, sum(Transaction_amount) as T_amount from top_trans where year ='{c}' and quarter = '{d}' group by pincode order by T_count desc limit 10",engine)
        df = pd.DataFrame(aa)
        fig = px.pie(aa, names='pincode', values='T_count',color_discrete_sequence=px.colors.sequential.Agsunset)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig,use_container_width=True)

    with col2:
        st.subheader("Top 10 Pincodes by Total Amount")

        aa = pd.read_sql_query(f"select pincode , sum(Transaction_count) as T_count, sum(Transaction_amount) as T_amount from top_trans where year ='{c}' and quarter = '{d}' group by pincode order by T_amount desc limit 10",engine)
        df = pd.DataFrame(aa)
        fig = px.pie(aa, names='pincode', values='T_amount',color_discrete_sequence=px.colors.sequential.Agsunset)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig,use_container_width=True)

if a == 'State' and b == 'User':

    col1,col2 = st.columns([2,2],gap="medium")

    with col1:  
  
        aa = pd.read_sql_query(f"select sum(Registered_user) as Total_User from map_user where year = '{c}' and quarter = '{d}'", engine)
        df = pd.DataFrame(aa)
        st.write("##### **Total User :**", df['Total_User'][0])


    with col2:
        aa = pd.read_sql_query(f"select Avg(Registered_user) as Avg_User from map_user where year = '{c}' and quarter = '{d}'", engine)
        df = pd.DataFrame(aa)
        st.write("##### **Avg User :**", df['Avg_User'][0])

    col1,col2 = st.columns([2,2],gap="medium")

    with col1:    
        aa = pd.read_sql_query(f"select sum(App_opens) as Total_App_opens from map_user where year = '{c}' and quarter = '{d}'", engine)
        df = pd.DataFrame(aa)
        st.write("##### **Total App Opens :**", df['Total_App_opens'][0])


    with col2:
        aa = pd.read_sql_query(f"select Avg(App_opens) as Avg_App_opens from map_user where year = '{c}' and quarter = '{d}'", engine)
        df = pd.DataFrame(aa)
        st.write("##### **Avg App Opens :**", df['Avg_App_opens'][0])


        
    col1,col2 = st.columns([2,2],gap="medium")

    with col1:  
        st.subheader("Total User")
  
        aa = pd.read_sql_query(f"select state, sum(Registered_user) as user from map_user  where year = '{c}' and quarter = '{d}'  group by state ", engine)
        df = pd.DataFrame(aa)

        fig = px.choropleth(
            df,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='state',
            color='user',
            color_continuous_scale='Reds'
        )

        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig,use_container_width=True)

    with col2:    
        st.subheader("Total App Opens")

        aa = pd.read_sql_query(f"select state, sum(Registered_user) as user, sum(App_opens) as app_open from map_user where year = '{c}' and quarter = '{d}'  group by state ", engine)
        df = pd.DataFrame(aa)

        fig = px.choropleth(
            df,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='state',
            color='app_open',
            color_continuous_scale='Reds',

        )

        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig,use_container_width=True)



    col1,col2 = st.columns([2,2],gap="medium")

    with col1:    
        st.subheader("Brand Wise Users")

        aa = pd.read_sql_query(f"select brands, sum(count)as counts from agg_user where year = '{c}' and quarter = '{d}'  group by brands order by counts desc ", engine)
        df = pd.DataFrame(aa)
        fig = px.bar(df, x='brands', y='counts', color = 'counts', color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(fig,use_container_width=True)

    with col2:    
        st.subheader("State Wise Users")

        aa = pd.read_sql_query(f"select state, sum(count) as counts from agg_user where year = '{c}' and quarter = '{d}'  group by state order by counts desc ", engine)
        df = pd.DataFrame(aa)
        fig = px.bar(df, x='state', y='counts', color = 'counts', color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(fig,use_container_width=True)


    st.header ('States')

    col1,col2 = st.columns([2,2],gap="medium")

    with col1:    
        st.subheader("Top 10 states by Total User")

        aa = pd.read_sql_query(f"select state, sum(Registered_user) as user, sum(App_opens) app_open from map_user where year = '{c}' and quarter = '{d}'  group by state order by user desc limit 10", engine)
        df = pd.DataFrame(aa)
        fig = px.pie(aa, names='state', values='user', color_discrete_sequence=px.colors.sequential.Agsunset)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig,use_container_width=True)

    with col2:    
        st.subheader("Top 10 states by Total App Open")

        aa = pd.read_sql_query(f"select state, sum(Registered_user) as user, sum(App_opens) app_open from map_user where year = '{c}' and quarter = '{d}'  group by state order by app_open desc limit 10", engine)
        df = pd.DataFrame(aa)
        fig = px.pie(aa, names='state', values='app_open', color_discrete_sequence=px.colors.sequential.Agsunset)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig,use_container_width=True)


    st.header ('Districts')

    col1,col2 = st.columns([2,2],gap="medium")

    with col1:    
        st.subheader("Top 10 Districts by Total User")

        aa = pd.read_sql_query(f"select district, sum(Registered_user) as user, sum(App_opens) app_open from map_user where year = '{c}' and quarter = '{d}'  group by district order by user desc limit 10", engine)
        df = pd.DataFrame(aa)
        fig = px.pie(aa, names='district', values='user', color_discrete_sequence=px.colors.sequential.Agsunset)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig,use_container_width=True)

    with col2:    
        st.subheader("Top 10 Districts by Total App Open")

        aa = pd.read_sql_query(f"select district, sum(Registered_user) as user, sum(App_opens) app_open from map_user where year = '{c}' and quarter = '{d}'  group by district order by app_open desc limit 10", engine)
        df = pd.DataFrame(aa)
        fig = px.pie(aa, names='district', values='app_open', color_discrete_sequence=px.colors.sequential.Agsunset)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig,use_container_width=True)


    st.header ('Pincodes')
    st.subheader("Top 10 Pincodes by Total User")

    aa = pd.read_sql_query(f"select pincode, sum(Registered_users) as user from top_user where year = '{c}' and quarter = '{d}'  group by pincode order by user desc limit 10", engine)
    df = pd.DataFrame(aa)
    fig = px.pie(aa, names='pincode', values='user', color_discrete_sequence=px.colors.sequential.Agsunset)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig,use_container_width=True)



if a == 'District':
    ad = st.selectbox("#### **Select a State**",
                             ( 'Andaman & Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh',     
                               'Dadra and Nagar Haveli and Daman and Diu', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 
                               'Jammu & Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep', 'Madhya Pradesh','Maharashtra', 
                               'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 
                               'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal'), index = 30)
        

if a == 'District' and b == 'Transaction':


    col1,col2 = st.columns([2,2],gap="medium")

    with col1:    
        
        aa = pd.read_sql_query(f"select State, year, quarter, avg(Amount) as Avg_Transaction_amount from map_trans where year = '{c}' and quarter = '{d}' and State = '{ad}'group by State,year,quarter order by state", engine)
        df = pd.DataFrame(aa)
        st.write("##### **Avg Amount :**", df['Avg_Transaction_amount'][0])


    with col2:
        aa = pd.read_sql_query(f"select State, year, quarter, avg(Count) as Avg_Transaction_count from map_trans where year = '{c}' and quarter = '{d}' and State = '{ad}'group by State,year,quarter order by state", engine)
        df = pd.DataFrame(aa)
        st.write("##### **Avg Count :**", df['Avg_Transaction_count'][0])


    col1,col2 = st.columns([2,2],gap="medium")

    with col1:
        st.subheader("Total Transaction Count")

        aa = pd.read_sql_query(f"select State, sum(Count) as Total_Transactions, sum(Amount) as Total_Amount from map_trans where year = '{c}' and quarter = '{d}' and State = '{ad}' group by State order by state", engine)
        df = pd.DataFrame(aa)

        fig = px.choropleth(
            df,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='Total_Transactions',
            color_continuous_scale='Reds'
        )

        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig,use_container_width=True)

    with col2:
        st.subheader("Total Transaction Amount")

        aa = pd.read_sql_query(f"select State, sum(Count) as Total_Transactions, sum(Amount) as Total_Amount from map_trans where year = '{c}' and quarter = '{d}' and State = '{ad}' group by State order by state", engine)
        df = pd.DataFrame(aa)

        fig = px.choropleth(
            df,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='Total_Amount',
            color_continuous_scale='Reds'
        )

        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig,use_container_width=True)


    st.subheader("Transaction Count by Districts")

    aa = pd.read_sql_query(f"select State, District,year,quarter, sum(Count) as Total_Transactions, sum(Amount) as Total_Amount from map_trans where year = '{c}' and quarter = '{d}' and State = '{ad}' group by State, District,year,quarter order by state,Total_Transactions desc", engine)
    df1 = pd.DataFrame(aa)
    fig = px.bar(df1, x="District", y="Total_Transactions", color='Total_Transactions', color_continuous_scale=px.colors.sequential.Agsunset)
    st.plotly_chart(fig,use_container_width=True)


    st.subheader("Transaction Amount by Districts")

    aa = pd.read_sql_query(f"select State, District,year,quarter, sum(Count) as Total_Transactions, sum(Amount) as Total_Amount from map_trans where year = '{c}' and quarter = '{d}' and State = '{ad}' group by State, District,year,quarter order by state,Total_Amount desc", engine)
    df1 = pd.DataFrame(aa)
    fig = px.bar(df1, x="District", y="Total_Amount", color='Total_Amount', color_continuous_scale=px.colors.sequential.Agsunset)
    st.plotly_chart(fig,use_container_width=True)

if a == 'District' and b == 'User':
       
    aa = pd.read_sql_query(f"select state, year, quarter, avg(Registered_users) as Avg_users from top_user2 where year = '{c}' and quarter = '{d}' and State = '{ad}' group by State,year,quarter order by state", engine)
    df = pd.DataFrame(aa)
    st.write("##### **Avg Users :**", df['Avg_users'][0])


    st.subheader("Total Registered Users")

    aa = pd.read_sql_query(f"select state,sum(Registered_users) as Total_Users from top_user2 where year = '{c}' and quarter = '{d}' and State = '{ad}' group by State", engine)
    df = pd.DataFrame(aa)

    fig = px.choropleth(
                df,
                geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                featureidkey='properties.ST_NM',
                locations='state',
                color='Total_Users',
                color_continuous_scale='Reds'
        )

    fig.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig,use_container_width=True)


    st.subheader("Total Users by Districts")

    aa = pd.read_sql_query(f"select District, sum(Registered_user) as Total_Users from map_user where year = '{c}' and quarter = '{d}' and State = '{ad}'group by District order by Total_Users desc", engine)
    df1 = pd.DataFrame(aa)
    fig = px.bar(df1, x="District", y="Total_Users", color='Total_Users', color_continuous_scale=px.colors.sequential.Agsunset)
    st.plotly_chart(fig,use_container_width=True)


    st.subheader("Total AppOpen by Districts")

    aa = pd.read_sql_query(f"select District, sum(app_opens) as Total_AppOpen from map_user where year = '{c}' and quarter = '{d}' and State = '{ad}'group by District order by Total_AppOpen desc", engine)
    df1 = pd.DataFrame(aa)
    fig = px.bar(df1, x="District", y="Total_AppOpen", color='Total_AppOpen', color_continuous_scale=px.colors.sequential.Agsunset)
    st.plotly_chart(fig,use_container_width=True)
































