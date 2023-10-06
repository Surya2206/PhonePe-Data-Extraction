import pandas as pd
import pymysql
import os
import json
from pprint import pprint

path=r"C:\Users\surya\Desktop\pulse-master\pulse-master\data\aggregated\transaction\country\india\state\andaman-&-nicobar-islands\2018\1.json"
Data=open(path,'r')
D=json.load(Data)

path_1=r"C:\Users\surya\Desktop\pulse-master\pulse-master\data\aggregated\transaction\country\india\state"
trans_list=os.listdir(path_1)

column={'State':[], 'Year':[],'Quater':[],'Transacion_type':[],
            'Transacion_count':[], 'Transacion_amount':[]}

for state in trans_list:
        col_state=path_1+"/"+state
        year_list=os.listdir(col_state)

        for year in year_list:
            col_year=col_state+"/"+year
            file_list=os.listdir(col_year)

            for file in file_list:
                col_file=col_year+"/"+file
                Data=open(col_file,'r')
                A=json.load(Data)
                try:
                    for i in A['data']['transactionData']:
                        Name=i['name']
                        count=i['paymentInstruments'][0]['count']
                        amount=i['paymentInstruments'][0]['amount']
                        column['Transacion_type'].append(Name)
                        column['Transacion_count'].append(count)
                        column['Transacion_amount'].append(amount)
                        column['State'].append(state)
                        column['Year'].append(year)
                        column['Quater'].append(int(file.strip('.json')))
                except:
                    pass
Agg_Trans=pd.DataFrame(column)

s = {'andaman-&-nicobar-islands' : 'Andaman & Nicobar',
        'andhra-pradesh' : 'Andhra Pradesh',
        'arunachal-pradesh' : 'Arunachal Pradesh',
        'assam' : 'Assam',   
        'bihar' : 'Bihar', 
        'chandigarh' : 'Chandigarh',
        'chhattisgarh' : 'Chhattisgarh',
        'dadra-&-nagar-haveli-&-daman-&-diu' : 'Dadra and Nagar Haveli and Daman and Diu',
        'delhi' : 'Delhi',
        'goa' : 'Goa',
        'gujarat' : 'Gujarat',
        'haryana' : 'Haryana',
        'himachal-pradesh' : 'Himachal Pradesh',
        'jammu-&-kashmir' : 'Jammu & Kashmir',
        'jharkhand' : 'Jharkhand',
        'karnataka' : 'Karnataka',
        'kerala' : 'Kerala',
        'ladakh' : 'Ladakh',
        'lakshadweep' : 'Lakshadweep',
        'madhya-pradesh' : 'Madhya Pradesh',
        'maharashtra' : 'Maharashtra',
        'manipur' : 'Manipur',
        'meghalaya' : 'Meghalaya',
        'mizoram' : 'Mizoram',
        'nagaland' : 'Nagaland',
        'odisha' : 'Odisha',
        'puducherry' : 'Puducherry',
        'punjab' : 'Punjab',
        'rajasthan' : 'Rajasthan',
        'sikkim' : 'Sikkim',
        'tamil-nadu' : 'Tamil Nadu',
        'telangana' : 'Telangana',
        'tripura' : 'Tripura',
        'uttar-pradesh' : 'Uttar Pradesh',
        'uttarakhand' : 'Uttarakhand',
        'west-bengal' : 'West Bengal'}
Agg_Trans['State'] = Agg_Trans['State'].map(s)

# *******************************************************************************************************


path2=r"C:\Users\surya\Desktop\pulse-master\pulse-master\data\aggregated\user\country\india\state"

user_list = os.listdir(path2)

columns2 = {'State': [], 'Year': [], 'Quarter': [], 'Brands': [], 'Count': [],
            'Percentage': []}
for state in user_list:
    cur_state = path2 + "/"+ state
    year_list = os.listdir(cur_state)
    
    for year in year_list:
        cur_year = cur_state + "/"+ year
        file_list = os.listdir(cur_year)

        for file in file_list:
            cur_file = cur_year + "/"+ file
            data = open(cur_file, 'r')
            B = json.load(data)
            try:
                for i in B["data"]["usersByDevice"]:
                    brand_name = i["brand"]
                    counts = i["count"]
                    percents = i["percentage"]
                    columns2["Brands"].append(brand_name)
                    columns2["Count"].append(counts)
                    columns2["Percentage"].append(percents)
                    columns2["State"].append(state)
                    columns2["Year"].append(year)
                    columns2["Quarter"].append(int(file.strip('.json')))
            except:
                pass
Agg_user = pd.DataFrame(columns2)

s = {'andaman-&-nicobar-islands' : 'Andaman & Nicobar',
     'andhra-pradesh' : 'Andhra Pradesh',
     'arunachal-pradesh' : 'Arunachal Pradesh',
     'assam' : 'Assam',   
     'bihar' : 'Bihar', 
     'chandigarh' : 'Chandigarh',
     'chhattisgarh' : 'Chhattisgarh',
     'dadra-&-nagar-haveli-&-daman-&-diu' : 'Dadra and Nagar Haveli and Daman and Diu',
     'delhi' : 'Delhi',
     'goa' : 'Goa',
     'gujarat' : 'Gujarat',
    'haryana' : 'Haryana',
     'himachal-pradesh' : 'Himachal Pradesh',
     'jammu-&-kashmir' : 'Jammu & Kashmir',
     'jharkhand' : 'Jharkhand',
     'karnataka' : 'Karnataka',
     'kerala' : 'Kerala',
     'ladakh' : 'Ladakh',
     'lakshadweep' : 'Lakshadweep',
     'madhya-pradesh' : 'Madhya Pradesh',
     'maharashtra' : 'Maharashtra',
     'manipur' : 'Manipur',
     'meghalaya' : 'Meghalaya',
     'mizoram' : 'Mizoram',
     'nagaland' : 'Nagaland',
     'odisha' : 'Odisha',
     'puducherry' : 'Puducherry',
     'punjab' : 'Punjab',
     'rajasthan' : 'Rajasthan',
     'sikkim' : 'Sikkim',
     'tamil-nadu' : 'Tamil Nadu',
     'telangana' : 'Telangana',
     'tripura' : 'Tripura',
     'uttar-pradesh' : 'Uttar Pradesh',
     'uttarakhand' : 'Uttarakhand',
     'west-bengal' : 'West Bengal'}
Agg_user['State'] = Agg_user['State'].map(s)

# *********************************************************************************


path3=r"C:\Users\surya\Desktop\pulse-master\pulse-master\data\map\transaction\hover\country\india\state"

map_trans_list = os.listdir(path3)

columns3 = {'State': [], 'Year': [], 'Quarter': [], 'District': [], 'Count': [],
            'Amount': []}
for state in map_trans_list:
    cur_state = path3 +"/" +state
    map_year_list = os.listdir(cur_state)
    
    for year in map_year_list:
        cur_year = cur_state +"/" +year
        map_file_list = os.listdir(cur_year)

        for file in map_file_list:
            cur_file = cur_year +"/" +file
            data = open(cur_file, 'r')
            C = json.load(data)

            for i in C["data"]["hoverDataList"]:
                district = i["name"]
                count = i["metric"][0]["count"]
                amount = i["metric"][0]["amount"]
                columns3["District"].append(district)
                columns3["Count"].append(count)
                columns3["Amount"].append(amount)
                columns3['State'].append(state)
                columns3['Year'].append(year)
                columns3['Quarter'].append(int(file.strip('.json')))
map_trans = pd.DataFrame(columns3)

s = {'andaman-&-nicobar-islands' : 'Andaman & Nicobar',
     'andhra-pradesh' : 'Andhra Pradesh',
     'arunachal-pradesh' : 'Arunachal Pradesh',
     'assam' : 'Assam',   
     'bihar' : 'Bihar', 
     'chandigarh' : 'Chandigarh',
     'chhattisgarh' : 'Chhattisgarh',
     'dadra-&-nagar-haveli-&-daman-&-diu' : 'Dadra and Nagar Haveli and Daman and Diu',
     'delhi' : 'Delhi',
     'goa' : 'Goa',
     'gujarat' : 'Gujarat',
    'haryana' : 'Haryana',
     'himachal-pradesh' : 'Himachal Pradesh',
     'jammu-&-kashmir' : 'Jammu & Kashmir',
     'jharkhand' : 'Jharkhand',
     'karnataka' : 'Karnataka',
     'kerala' : 'Kerala',
     'ladakh' : 'Ladakh',
     'lakshadweep' : 'Lakshadweep',
     'madhya-pradesh' : 'Madhya Pradesh',
     'maharashtra' : 'Maharashtra',
     'manipur' : 'Manipur',
     'meghalaya' : 'Meghalaya',
     'mizoram' : 'Mizoram',
     'nagaland' : 'Nagaland',
     'odisha' : 'Odisha',
     'puducherry' : 'Puducherry',
     'punjab' : 'Punjab',
     'rajasthan' : 'Rajasthan',
     'sikkim' : 'Sikkim',
     'tamil-nadu' : 'Tamil Nadu',
     'telangana' : 'Telangana',
     'tripura' : 'Tripura',
     'uttar-pradesh' : 'Uttar Pradesh',
     'uttarakhand' : 'Uttarakhand',
     'west-bengal' : 'West Bengal'}
map_trans['State'] = map_trans['State'].map(s)

# *************************************************************************************

path4=r"C:\Users\surya\Desktop\pulse-master\pulse-master\data\map\user\hover\country\india\state"

map_user_list = os.listdir(path4)

columns4 = {'State': [], 'Year': [], 'Quarter': [], 'District': [],
            'RegisteredUser': [], 'AppOpens': []}
for state in map_user_list:
    cur_state = path4 +"/" +state
    map_year_list = os.listdir(cur_state)
    
    for year in map_year_list:
        cur_year = cur_state +"/" +year
        map_file_list = os.listdir(cur_year)

        for file in map_file_list:
            cur_file = cur_year +"/"+ file
            data = open(cur_file, 'r')
            D = json.load(data)

            for i in D["data"]["hoverData"].items():
                district = i[0]
                registereduser = i[1]["registeredUsers"]
                appOpens = i[1]['appOpens']
                columns4["District"].append(district)
                columns4["RegisteredUser"].append(registereduser)
                columns4["AppOpens"].append(appOpens)
                columns4['State'].append(state)
                columns4['Year'].append(year)
                columns4['Quarter'].append(int(file.strip('.json')))

map_user = pd.DataFrame(columns4)

s = {'andaman-&-nicobar-islands' : 'Andaman & Nicobar',
     'andhra-pradesh' : 'Andhra Pradesh',
     'arunachal-pradesh' : 'Arunachal Pradesh',
     'assam' : 'Assam',   
     'bihar' : 'Bihar', 
     'chandigarh' : 'Chandigarh',
     'chhattisgarh' : 'Chhattisgarh',
     'dadra-&-nagar-haveli-&-daman-&-diu' : 'Dadra and Nagar Haveli and Daman and Diu',
     'delhi' : 'Delhi',
     'goa' : 'Goa',
     'gujarat' : 'Gujarat',
    'haryana' : 'Haryana',
     'himachal-pradesh' : 'Himachal Pradesh',
     'jammu-&-kashmir' : 'Jammu & Kashmir',
     'jharkhand' : 'Jharkhand',
     'karnataka' : 'Karnataka',
     'kerala' : 'Kerala',
     'ladakh' : 'Ladakh',
     'lakshadweep' : 'Lakshadweep',
     'madhya-pradesh' : 'Madhya Pradesh',
     'maharashtra' : 'Maharashtra',
     'manipur' : 'Manipur',
     'meghalaya' : 'Meghalaya',
     'mizoram' : 'Mizoram',
     'nagaland' : 'Nagaland',
     'odisha' : 'Odisha',
     'puducherry' : 'Puducherry',
     'punjab' : 'Punjab',
     'rajasthan' : 'Rajasthan',
     'sikkim' : 'Sikkim',
     'tamil-nadu' : 'Tamil Nadu',
     'telangana' : 'Telangana',
     'tripura' : 'Tripura',
     'uttar-pradesh' : 'Uttar Pradesh',
     'uttarakhand' : 'Uttarakhand',
     'west-bengal' : 'West Bengal'}
map_user['State'] = map_user['State'].map(s)

# ********************************************************************************************


path5 = r"C:\Users\surya\Desktop\pulse-master\pulse-master\data\top\transaction\country\india\state"
top_trans_list = os.listdir(path5)

columns5 = {'State': [], 'Year': [], 'Quarter': [], 'Pincode': [],
            'Transaction_count': [], 'Transaction_amount': []}
for state in top_trans_list:
    cur_state = path5 +"/" +state
    top_year_list = os.listdir(cur_state)
    
    for year in top_year_list:
        cur_year = cur_state +"/" +year
        top_file_list = os.listdir(cur_year)

        for file in top_file_list:
            cur_file = cur_year +"/"+ file
            data = open(cur_file, 'r')
            E = json.load(data)

            for i in E['data']['pincodes']:
                name = i['entityName']
                count = i['metric']['count']
                amount = i['metric']['amount']
                columns5['Pincode'].append(name)
                columns5['Transaction_count'].append(count)
                columns5['Transaction_amount'].append(amount)
                columns5['State'].append(state)
                columns5['Year'].append(year)
                columns5['Quarter'].append(int(file.strip('.json')))

top_trans = pd.DataFrame(columns5)

s = {'andaman-&-nicobar-islands' : 'Andaman & Nicobar',
     'andhra-pradesh' : 'Andhra Pradesh',
     'arunachal-pradesh' : 'Arunachal Pradesh',
     'assam' : 'Assam',   
     'bihar' : 'Bihar', 
     'chandigarh' : 'Chandigarh',
     'chhattisgarh' : 'Chhattisgarh',
     'dadra-&-nagar-haveli-&-daman-&-diu' : 'Dadra and Nagar Haveli and Daman and Diu',
     'delhi' : 'Delhi',
     'goa' : 'Goa',
     'gujarat' : 'Gujarat',
    'haryana' : 'Haryana',
     'himachal-pradesh' : 'Himachal Pradesh',
     'jammu-&-kashmir' : 'Jammu & Kashmir',
     'jharkhand' : 'Jharkhand',
     'karnataka' : 'Karnataka',
     'kerala' : 'Kerala',
     'ladakh' : 'Ladakh',
     'lakshadweep' : 'Lakshadweep',
     'madhya-pradesh' : 'Madhya Pradesh',
     'maharashtra' : 'Maharashtra',
     'manipur' : 'Manipur',
     'meghalaya' : 'Meghalaya',
     'mizoram' : 'Mizoram',
     'nagaland' : 'Nagaland',
     'odisha' : 'Odisha',
     'puducherry' : 'Puducherry',
     'punjab' : 'Punjab',
     'rajasthan' : 'Rajasthan',
     'sikkim' : 'Sikkim',
     'tamil-nadu' : 'Tamil Nadu',
     'telangana' : 'Telangana',
     'tripura' : 'Tripura',
     'uttar-pradesh' : 'Uttar Pradesh',
     'uttarakhand' : 'Uttarakhand',
     'west-bengal' : 'West Bengal'}
top_trans['State'] = top_trans['State'].map(s)

# ************************************************************************************************************


path6 = r"C:\Users\surya\Desktop\pulse-master\pulse-master\data\top\transaction\country\india\state"

top_trans_list = os.listdir(path6)
columns6 = {'State': [], 'Year': [], 'Quarter': [], 'district': [], 'Transaction_count': [],
            'Transaction_amount': []}

for state in top_trans_list:
    cur_state = path6 +"/" + state
    top_year_list = os.listdir(cur_state)
    
    for year in top_year_list:
        cur_year = cur_state +"/" + year
        top_file_list = os.listdir(cur_year)
        
        for file in top_file_list:
            cur_file = cur_year +"/" +file
            data = open(cur_file, 'r')
            F = json.load(data)
            
            for i in F['data']['districts']:
                name = i['entityName']
                count = i['metric']['count']
                amount = i['metric']['amount']
                columns6['district'].append(name)
                columns6['Transaction_count'].append(count)
                columns6['Transaction_amount'].append(amount)
                columns6['State'].append(state)
                columns6['Year'].append(year)
                columns6['Quarter'].append(int(file.strip('.json')))
top_trans2 = pd.DataFrame(columns6)


s = {'andaman-&-nicobar-islands' : 'Andaman & Nicobar',
     'andhra-pradesh' : 'Andhra Pradesh',
     'arunachal-pradesh' : 'Arunachal Pradesh',
     'assam' : 'Assam',   
     'bihar' : 'Bihar', 
     'chandigarh' : 'Chandigarh',
     'chhattisgarh' : 'Chhattisgarh',
     'dadra-&-nagar-haveli-&-daman-&-diu' : 'Dadra and Nagar Haveli and Daman and Diu',
     'delhi' : 'Delhi',
     'goa' : 'Goa',
     'gujarat' : 'Gujarat',
    'haryana' : 'Haryana',
     'himachal-pradesh' : 'Himachal Pradesh',
     'jammu-&-kashmir' : 'Jammu & Kashmir',
     'jharkhand' : 'Jharkhand',
     'karnataka' : 'Karnataka',
     'kerala' : 'Kerala',
     'ladakh' : 'Ladakh',
     'lakshadweep' : 'Lakshadweep',
     'madhya-pradesh' : 'Madhya Pradesh',
     'maharashtra' : 'Maharashtra',
     'manipur' : 'Manipur',
     'meghalaya' : 'Meghalaya',
     'mizoram' : 'Mizoram',
     'nagaland' : 'Nagaland',
     'odisha' : 'Odisha',
     'puducherry' : 'Puducherry',
     'punjab' : 'Punjab',
     'rajasthan' : 'Rajasthan',
     'sikkim' : 'Sikkim',
     'tamil-nadu' : 'Tamil Nadu',
     'telangana' : 'Telangana',
     'tripura' : 'Tripura',
     'uttar-pradesh' : 'Uttar Pradesh',
     'uttarakhand' : 'Uttarakhand',
     'west-bengal' : 'West Bengal'}
top_trans2['State'] = top_trans2['State'].map(s)

# *********************************************************************************************************

path7 = r"C:\Users\surya\Desktop\pulse-master\pulse-master\data\top\user\country\india\state"
top_user_list = os.listdir(path7)
columns7 = {'State': [], 'Year': [], 'Quarter': [], 'Pincode': [],
            'RegisteredUsers': []}

for state in top_user_list:
    cur_state = path7+ "/"+ state
    top_year_list = os.listdir(cur_state)
    
    for year in top_year_list:
        cur_year = cur_state+ "/"+ year
        top_file_list = os.listdir(cur_year)
        
        for file in top_file_list:
            cur_file = cur_year +"/"+ file
            data = open(cur_file, 'r')
            G = json.load(data)
            
            for i in G['data']['pincodes']:
                name = i['name']
                registeredUsers = i['registeredUsers']
                columns7['Pincode'].append(name)
                columns7['RegisteredUsers'].append(registeredUsers)
                columns7['State'].append(state)
                columns7['Year'].append(year)
                columns7['Quarter'].append(int(file.strip('.json')))
top_user = pd.DataFrame(columns7)

s = {'andaman-&-nicobar-islands' : 'Andaman & Nicobar',
     'andhra-pradesh' : 'Andhra Pradesh',
     'arunachal-pradesh' : 'Arunachal Pradesh',
     'assam' : 'Assam',   
     'bihar' : 'Bihar', 
     'chandigarh' : 'Chandigarh',
     'chhattisgarh' : 'Chhattisgarh',
     'dadra-&-nagar-haveli-&-daman-&-diu' : 'Dadra and Nagar Haveli and Daman and Diu',
     'delhi' : 'Delhi',
     'goa' : 'Goa',
     'gujarat' : 'Gujarat',
    'haryana' : 'Haryana',
     'himachal-pradesh' : 'Himachal Pradesh',
     'jammu-&-kashmir' : 'Jammu & Kashmir',
     'jharkhand' : 'Jharkhand',
     'karnataka' : 'Karnataka',
     'kerala' : 'Kerala',
     'ladakh' : 'Ladakh',
     'lakshadweep' : 'Lakshadweep',
     'madhya-pradesh' : 'Madhya Pradesh',
     'maharashtra' : 'Maharashtra',
     'manipur' : 'Manipur',
     'meghalaya' : 'Meghalaya',
     'mizoram' : 'Mizoram',
     'nagaland' : 'Nagaland',
     'odisha' : 'Odisha',
     'puducherry' : 'Puducherry',
     'punjab' : 'Punjab',
     'rajasthan' : 'Rajasthan',
     'sikkim' : 'Sikkim',
     'tamil-nadu' : 'Tamil Nadu',
     'telangana' : 'Telangana',
     'tripura' : 'Tripura',
     'uttar-pradesh' : 'Uttar Pradesh',
     'uttarakhand' : 'Uttarakhand',
     'west-bengal' : 'West Bengal'}
top_user['State'] = top_user['State'].map(s)
# ******************************************************************************************************************

path8 = r"C:\Users\surya\Desktop\pulse-master\pulse-master\data\top\user\country\india\state"
top_user_list = os.listdir(path8)
columns8 = {'State': [], 'Year': [], 'Quarter': [], 'district': [],
            'RegisteredUsers': []}

for state in top_user_list:
    cur_state = path8+ "/"+ state
    top_year_list = os.listdir(cur_state)
    
    for year in top_year_list:
        cur_year = cur_state+ "/"+ year
        top_file_list = os.listdir(cur_year)
        
        for file in top_file_list:
            cur_file = cur_year +"/"+ file
            data = open(cur_file, 'r')
            H = json.load(data)
            
            for i in H['data']['districts']:
                name = i['name']
                registeredUsers = i['registeredUsers']
                columns8['district'].append(name)
                columns8['RegisteredUsers'].append(registeredUsers)
                columns8['State'].append(state)
                columns8['Year'].append(year)
                columns8['Quarter'].append(int(file.strip('.json')))
top_user2 = pd.DataFrame(columns8)

s = {'andaman-&-nicobar-islands' : 'Andaman & Nicobar',
     'andhra-pradesh' : 'Andhra Pradesh',
     'arunachal-pradesh' : 'Arunachal Pradesh',
     'assam' : 'Assam',   
     'bihar' : 'Bihar', 
     'chandigarh' : 'Chandigarh',
     'chhattisgarh' : 'Chhattisgarh',
     'dadra-&-nagar-haveli-&-daman-&-diu' : 'Dadra and Nagar Haveli and Daman and Diu',
     'delhi' : 'Delhi',
     'goa' : 'Goa',
     'gujarat' : 'Gujarat',
    'haryana' : 'Haryana',
     'himachal-pradesh' : 'Himachal Pradesh',
     'jammu-&-kashmir' : 'Jammu & Kashmir',
     'jharkhand' : 'Jharkhand',
     'karnataka' : 'Karnataka',
     'kerala' : 'Kerala',
     'ladakh' : 'Ladakh',
     'lakshadweep' : 'Lakshadweep',
     'madhya-pradesh' : 'Madhya Pradesh',
     'maharashtra' : 'Maharashtra',
     'manipur' : 'Manipur',
     'meghalaya' : 'Meghalaya',
     'mizoram' : 'Mizoram',
     'nagaland' : 'Nagaland',
     'odisha' : 'Odisha',
     'puducherry' : 'Puducherry',
     'punjab' : 'Punjab',
     'rajasthan' : 'Rajasthan',
     'sikkim' : 'Sikkim',
     'tamil-nadu' : 'Tamil Nadu',
     'telangana' : 'Telangana',
     'tripura' : 'Tripura',
     'uttar-pradesh' : 'Uttar Pradesh',
     'uttarakhand' : 'Uttarakhand',
     'west-bengal' : 'West Bengal'}
top_user2['State'] = top_user2['State'].map(s)

# *********************************************************************************************************

connection = pymysql.connect(
                     host = "127.0.0.1",
                     user = "root",
                     password = "Surya123"
                     )

cur = connection.cursor()
cur.execute("create database if not exists phonepe")

connection = pymysql.connect(
                     host = "127.0.0.1",
                     user = "root",
                     password = "Surya123",
                     database = "phonepe"
                     )
cur = connection.cursor()

cur.execute("create table if not exists Agg_trans (State varchar(250), Year int(64), Quarter int(64), Transaction_type varchar(250), Transaction_count int(64), Transaction_amount varchar(250))")
sql = "INSERT INTO Agg_trans VALUES (%s,%s,%s,%s,%s,%s)"
for i in range(0,len(Agg_Trans)):
    cur.execute(sql,tuple(Agg_Trans.iloc[i]))
    connection.commit()


cur.execute("create table if not exists Agg_user (State varchar(100), Year int, Quarter int, Brands varchar(100), Count int, Percentage double)")
sql = "INSERT INTO Agg_user VALUES (%s,%s,%s,%s,%s,%s)"
for i in range(0,len(Agg_user)):
    cur.execute(sql,tuple(Agg_user.iloc[i]))
    connection.commit()

cur.execute("create table if not exists Map_trans (State varchar(100), Year int, Quarter int, District varchar(100), Count int, Amount double)")
sql = "INSERT INTO Map_trans VALUES (%s,%s,%s,%s,%s,%s)"
for i in range(0,len(map_trans)):
    cur.execute(sql,tuple(map_trans.iloc[i]))
    connection.commit()  

cur.execute("create table if not exists Map_user (State varchar(100), Year int, Quarter int, District varchar(100), Registered_user int, App_opens int)")
sql = "INSERT INTO Map_user VALUES (%s,%s,%s,%s,%s,%s)"
for i in range(0,len(map_user)):
    cur.execute(sql,tuple(map_user.iloc[i]))
    connection.commit()    

cur.execute("create table if not exists Top_trans (State varchar(100), Year int, Quarter int, Pincode int, Transaction_count int, Transaction_amount varchar(250))")
sql = "INSERT INTO Top_trans VALUES (%s,%s,%s,%s,%s,%s)"
for i in range(0,len(top_trans)):
    cur.execute(sql,tuple(top_trans.iloc[i]))
    connection.commit()    


cur.execute("create table if not exists Top_trans2 (State varchar(100), Year int, Quarter int, District varchar(250), Transaction_count int, Transaction_amount varchar(250))")
sql = "INSERT INTO Top_trans2 VALUES (%s,%s,%s,%s,%s,%s)"
for i in range(0,len(top_trans2)):
    cur.execute(sql,tuple(top_trans2.iloc[i]))
    connection.commit()  


cur.execute("create table if not exists Top_user (State varchar(100), Year int, Quarter int, Pincode int, Registered_users int)")
sql = "INSERT INTO Top_user VALUES (%s,%s,%s,%s,%s)"
for i in range(0,len(top_user)):
    cur.execute(sql,tuple(top_user.iloc[i]))
    connection.commit()       


cur.execute("create table if not exists Top_user2 (State varchar(100), Year int, Quarter int, District varchar(250), Registered_users int)")
sql = "INSERT INTO Top_user2 VALUES (%s,%s,%s,%s,%s)"
for i in range(0,len(top_user2)):
    cur.execute(sql,tuple(top_user2.iloc[i]))
    connection.commit()       