import pandas as pd
import re
#set display

pd.set_option("display.max_columns",None)
pd.set_option("display.width",None)

#Task 2_1
#df = pd.read_csv('winereviews.csv',index_col=0)
#df.head(2)
#print(df)

#Task 2_2 What countries are represented in the dataset?
#df['country'].value_counts().index.tolist()
#df['country'].unique()

#df = pd.read_csv('winereviews.csv', index_col=0)
#ountries = pd.read_csv('winereviews.csv', usecols=["country"])
#nd_countries = countries.drop_duplicates()
#print(nd_countries)

#Task2_3 Show all wines with a score of 100
df = pd.read_csv('winereviews.csv', index_col=0)
#print(df[df['points']==100])
#df.loc[df['points']==100]
#print(df)

#Taskk2_4 Show all wines with a cost of over 1000
#price1 = df[df['price']>1000]
#print(price1)
#df.loc[df['price']>1000]

#Task2_5 Find the highest rated wine for each variety
#variety = df.groupby('variety').points.agg([max])
#print(variety)

#Task2_6 Find the lowest rated wine for each variety
#variety = df.groupby('variety').points.agg([min])
#print(variety)

#Task2_7 Find the top 10 bargain wines (wines with the highest points-to-price ratio)
#bargains = df.copy()
#bargains['Value'] =bargains.points/bargains.price
#largest = bargains.nlargest(10,'Value')
#print(largest)

#Task2_8 Calculate the average price of wine for each:
#country_avg = df['price'].groupby(df['country']).mean()
#print(country_avg)
#df.groupby('country')['price'].mean()
#variety_avg = df['price'].groupby(df['variety']).mean()
#print(variety_avg)
#df.groupby('variety')['price'].mean()

#Task2_9 Calculate the average score for wine for each:
#country_avg = df['score'].groupby(df['country']).mean()
#print(country_avg)
#df.groupby('country')['score'].mean()
#variety_avg = df['score'].groupby(df['variety']).mean()
#print(variety_avg)


#Advanced Create a Series whose index is a MultiIndex of {country, variety} pairs
#df[['country','variety']].value_counts()
#combo = df.groupby(['country','variety']).variety.count().sort_values(ascending=False)
#print(combo)

#Task 3
#regex
#desc = df['description']
#fruity= 0
#tropical= 0
#for d in desc:
    #if(re.search("fruity",d)):
        #fruity +=1
    #elif(re.search("tropical",d)):
        #tropical+=1

#print(tropical,"and",fruity)

##Pandas
n_trop = df.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = df.description.map(lambda desc: "fruity" in desc).sum()
print("tropical/fruity with Pandas")
print("tropical:",n_trop)
print("fruity",n_fruity)



