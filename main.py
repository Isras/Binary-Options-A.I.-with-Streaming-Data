import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from iqoptionapi.stable_api import IQ_Option
import logging
import time
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn import preprocessing
from sklearn import utils
import pickle
from getpass import getpass

email = str(input("Digite o email: "))
senha = getpass("Digite a senha:")
    
iq = IQ_Option(email, senha)
iq.connect()

if iq.check_connect() is True:
    print("Logado com sucesso!")

end_from_time = time.time()

modeloPronto = pickle.load(open('modeloTreinado.sav', 'rb'))

goal="EURUSD"
size=900
timeperiod=900
maxdict=1

iq.change_balance("PRACTICE")

print("start stream...")
iq.start_candles_stream(goal,size,maxdict)

while True:
    candles=iq.get_realtime_candles(goal,size)
    input = {
        "open": 0.0,
        "min": 0.0,
        "max": 0.0,
        "volume": 0.0,
        "close": 0.0
    }
    for timestamp in candles:
        input["open"] = candles[timestamp]["open"]
        input["min"] = candles[timestamp]["min"]
        input["max"] = candles[timestamp]["max"]
        input["volume"] = candles[timestamp]["volume"]
        input["close"] = candles[timestamp]["close"]

    print(input)
    print(int(time.time()), (timestamp + 900), input["open"])
    if int(time.time()) == timestamp + 898:
        dft = pd.DataFrame(data = input, index=[0])
        resultado = modeloPronto.predict(dft)
        if resultado < input['close']:
            sinal = 'put'
        else:
            sinal = 'call'
        check,id=iq.buy(5,"EURUSD",sinal,15)
        if check:
            print("Comprou com sucesso!")
        else:
            print("Não funcionou!")
        print(resultado)
        
    
    
    time.sleep(1)
