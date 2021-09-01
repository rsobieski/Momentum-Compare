#https://www.youtube.com/watch?v=wIfjERirYZk
import yfinance as yf
import numpy as np

df = yf.download('BTC-USD', start='2021-06-10',interval='1m')

def calculatePostion (df, step = 10):
    print(df)

    #copy of df
    df = df.copy()

    #np ->  Close -> procetnage change method
    df['ret'] = np.log(df.Close.pct_change() + 1)
    df['prior_n'] = df.ret.rolling(step).sum()

    print(df)

    #keep only valid entries in df
    df.dropna(inplace=True)

    #i is prior of day or days return
    #set return value: positive or negative depends on i
    df['position'] = [1 if i > 0 else -1 for i in df.prior_n]

    df['strat'] = df.position.shift(1) * df.ret

    print(df)

    return np.exp(df[['ret','strat']].cumsum()).plot(figsize=(12,6))

calculatePostion(df,10)

np.exp(df[['ret','strat']].cumsum()).plot(figsize=(26,16))


