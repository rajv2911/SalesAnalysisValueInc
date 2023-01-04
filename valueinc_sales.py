# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 12:22:10 2023

@author: Lenovo
"""

# data import from csv file

import pandas as pd

data = pd.read_csv('transaction.csv', sep =';')

# information about data from the csv file

data.info()

# calculation for columns

costPerItem = data['CostPerItem']
numberOfItemsPurchased = data['NumberOfItemsPurchased']
costPerTransaction = costPerItem * numberOfItemsPurchased

# adding new column to the dataframe

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']
data['Profit'] = data['SalesPerTransaction'] - data['CostPerTransaction']
data['Markup'] =  ( data['SalesPerTransaction'] -  data['CostPerTransaction'] ) / data['CostPerTransaction'] 

data['Markup'] = round(data['Markup'], 2)





# checking data type 

print(data['Day'].dtype)

# changing data type

day = data['Day'].astype(str)

print(day.dtype)

print(data['Year'].dtype)

year = data['Year'].astype(str)
print(year.dtype)

data['Date'] = day + '-' + data['Month'] + '-' + year

# iloc- used for displaying column and row associated with that particular index

data.iloc[0:5]

# head

data.head(5)

# splitting the client keywords
# new_var = column.str.split('sep', expand = true )

split_col = data['ClientKeywords'].str.split(',' , expand = True)


data['ClientAge'] =  split_col[0]

data['ClientType'] = split_col[1]

data['LengthOfContract'] = split_col[2]

# replace function

data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']', '')


#changing to lower case

data['ItemDescription'] = data['ItemDescription'] .str.lower()


# merging two datasets

seasons = pd.read_csv('1.4 value_inc_seasons.csv', sep =';')

#merging files- merge_df = pd.merge(df_old, df_new, on= 'key')

data = pd.merge(data, seasons, on = 'Month')





# dropping columns

data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Day', axis = 1)
data = data.drop('Year', axis = 1)
data = data.drop('Month', axis =1)

# exporting into csv

data.to_csv('ValueIncSales_Cleansed.csv', index = False)















