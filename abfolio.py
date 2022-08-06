import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import investpy as inv
import math
import numpy as np
import time

current_date = time.strftime("%d/%m/%Y")

current_date_yf = time.strftime('%Y-%m-%d')


sum1 = 1
isin_history = []

fetch_history = []


def fetchData(isin_history,sum1):
  error_arr = ['stocks','bonds','etfs','cryptos',"currencies","funds"]
  while round(sum1,4) >= 0:
      if sum1 > 0:

        print(' ')
        asset_cat = input('Type asset class ("stocks", "bonds",","etfs","cryptos","currencies","funds") <-> ')
        while asset_cat not in error_arr:
          asset_cat = input('Type asset class ("stocks", "bonds",","etfs","cryptos","currencies","funds") <-> ')
        print(' ')

        isin_code = input('Type ISIN code <-> ')
        print(' ')

        asset_weight = float(input('Asset Weight 0 to 1.0 ->'))
        print(' ')

        if asset_weight >=1:
          asset_weight = 1
        try:
          quote = inv.search_quotes(text=isin_code,products = [asset_cat.lower()],n_results = 1)
        except RuntimeError:
          print('Error! Invalid or unavailable ISIN Code, please try again')
        finally:
          print("*******************************")
          print(quote.name)
          print(quote.exchange)
          print(quote.country)
          print(quote.symbol)
          print('*******************************')
          print("%d -> remaining portfolio alloc"%(sum1))

          asset_isin = isin_code
          isin_history.append([quote.name,quote.symbol,quote.country,asset_weight,asset_cat.lower(),asset_isin.upper()])
          sum1 -= asset_weight 
          print(sum1)
      else:
        break
isin_array = []

isin_history = []
isin_history2 = []
sum1 = 1
sum2 = 1
print('PORTFOLIO 1 :')
fetchData(isin_history,sum1)
print('PORTFOLIO 2')
fetchData(isin_history2,sum2)
dfs1 = pd.DataFrame()
dfs2 = pd.DataFrame()
weights1 = []
columns1 = []
weights2 = []
columns2 = []
frames1 = []
frames2 = []
for i in range(len(isin_history)):
  name = isin_history[i][0]
  symbol = isin_history[i][1]
  country = isin_history[i][2]
  weight = isin_history[i][3]
  cat = isin_history[i][4]
  isin = isin_history[i][5]
  quote = inv.search_quotes(name,products = [cat],n_results = 1)
  df1 = quote.retrieve_historical_data('01/01/2003',current_date)
  df1 = df1['Close']
  columns1.append(symbol)
  weights1.append(weight)
  frames1.append(df1)
dfs1 = pd.concat(frames1,axis=1)

for i in range(len(isin_history2)):
  name = isin_history2[i][0]
  symbol = isin_history2[i][1]
  country = isin_history2[i][2]
  weight = isin_history2[i][3]
  cat = isin_history2[i][4]
  isin = isin_history2[i][5]
  quote = inv.search_quotes(name,products = [cat],n_results = 1)
  df2 = quote.retrieve_historical_data('01/01/2003',current_date)['Close']
  columns2.append(symbol)
  weights2.append(weight)
  frames2.append(df2)

dfs2 = pd.concat(frames2,axis=1)
dfs1T = dfs1
dfs2T = dfs2
dfs1T.columns = columns1
dfs2T.columns = columns2

weights_arr1 = np.array(weights1)
weights_arr2 = np.array(weights2)
returns1 = dfs1T.pct_change()
returns1.dropna(inplace=True)


if len(weights1) > 1:
  returns1['Portfolio 1'] = returns1.dot(weights_arr1)

daily_ret1 = (1+returns1).cumprod()

weights_arr2 = np.array(weights2)
returns2 = dfs2T.pct_change()
returns2.dropna(inplace=True)
if len(weights2)>1: 
  returns2['Portfolio 2'] = returns2.dot(weights_arr2)

daily_ret2 = (1+returns2).cumprod()


totalPlot = daily_ret1.join(daily_ret2)
totalPlot.dropna(inplace=True)

common_time = totalPlot.iloc[[0]].index.tolist()
common_time = common_time[0]
common_time = str(common_time)[:11]
newtime = '%s/%s/%s'%(common_time[8:10],common_time[5:7],common_time[:4])
sum1 = 1
sum2 = 1
dfs1 = pd.DataFrame()
dfs2 = pd.DataFrame()
weights1 = []
columns1 = []
weights2 = []
columns2 = []
frames1 = []
frames2 = []
for i in range(len(isin_history)):
  print(isin_history[i])
  name = isin_history[i][0]
  symbol = isin_history[i][1]
  country = isin_history[i][2]
  weight = isin_history[i][3]
  cat = isin_history[i][4]
  isin = isin_history[i][5]
  quote = inv.search_quotes(name,products = [cat],n_results = 1)
  df1 = quote.retrieve_historical_data(newtime,current_date)['Close']
  columns1.append(symbol)
  weights1.append(weight)
  frames1.append(df1)
dfs1 = pd.concat(frames1,axis=1)

for i in range(len(isin_history2)):
  name = isin_history2[i][0]
  symbol = isin_history2[i][1]
  country = isin_history2[i][2]
  weight = isin_history2[i][3]
  cat = isin_history2[i][4]
  isin = isin_history2[i][5]
  quote = inv.search_quotes(name,products = [cat],n_results = 1)
  df2 = quote.retrieve_historical_data(newtime,current_date)['Close']
  columns2.append(symbol)
  weights2.append(weight)
  frames2.append(df2)

dfs2 = pd.concat(frames2,axis=1)
dfs1T = dfs1
dfs2T = dfs2
dfs1T.columns = columns1
dfs2T.columns = columns2

weights_arr1 = np.array(weights1)
weights_arr2 = np.array(weights2)
returns1 = dfs1T.pct_change()
returns1.dropna(inplace=True)


if len(weights1) > 1:
  returns1['Portfolio 1'] = returns1.dot(weights_arr1)

daily_ret1 = (1+returns1).cumprod()

weights_arr2 = np.array(weights2)
returns2 = dfs2T.pct_change()
returns2.dropna(inplace=True)
if len(weights2)>1: 
  returns2['Portfolio 2'] = returns2.dot(weights_arr2)

daily_ret2 = (1+returns2).cumprod()


totalPlot = daily_ret1.join(daily_ret2)
totalPlot.dropna(inplace=True)
if len(weights1) > 1:
  totalPlot[['Portfolio 1',list(totalPlot.columns)[-1]]].plot(figsize=(10,5),fontsize=16)
elif len(weights2) > 1:
  totalPlot[[list(totalPlot.columns)[0],'Portfolio 2']].plot(figsize=(10,5),fontsize=16)
else:
  totalPlot.plot(figsize=(10,5),fontsize=16)
plt.xlabel('Period',fontsize=20)
plt.title('Portfolio Performance - @Antonio Brych/ABFOLIO',fontsize=16)
plt.show()
