# Very simple script to get information about Bitcoin price
# by default, the file is saved in C:/Users/Username/Desktop
# Written by Stan
import urllib.request
import json
import os
from datetime import datetime
today= datetime.now()
# o-option
o = 0
print("--------------Fast BitcoinChecker-------------------")
print(
    '1=ping to Coingecko api\n2=btc/usd \n3=btc/pln\n4=btc/chf\n5=btc/eur\n6=btc/gbp\n99=exit')
while o != 99 :
    o = (input(': '))
    if o == '99' :
        print("Bye")
        print("---------------------------------------------------")
        break
    elif o == '1' :
        url = 'https://api.coingecko.com/api/v3/ping'
        response = urllib.request.urlopen((url))
        result = json.loads(response.read())
        print(result['gecko_says'], '\n')
    elif o == '2' :
        url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())
        print(today,'Bitcoin price is', result['bitcoin']['usd'], 'usd', '\n')
        with open(os.path.join('C:/Users/Username/Desktop','btcusd.txt'), 'a') as file :
            file.writelines([str(today),' Bitcoin price is ', str(result['bitcoin']['usd']), ' USD', '\n'])
    elif o == '3' :
        url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=pln'
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())
        print(today,'Bitcoin price is', result['bitcoin']['pln'], 'zł', '\n')
        with open(os.path.join('C:/Users/Username/Desktop','btcpln.txt'), 'a') as file :
            file.writelines([str(today),' Bitcoin price is ', str(result['bitcoin']['pln']), ' PLN', '\n'])
    elif o == '4' :
        url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=chf'
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())
        print(today, 'Bitcoin price is', result['bitcoin']['chf'], 'chf', '\n')
        with open(os.path.join('C:/Users/Username/Desktop','btcchf.txt'), 'a') as file :
            file.writelines([str(today), ' Bitcoin price is ', str(result['bitcoin']['chf']), ' CHF', '\n'])
    elif o == '5' :
        url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eur'
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())
        print(today, 'Bitcoin price is', result['bitcoin']['eur'], 'eur', '\n')
        with open(os.path.join('C:/Users/Username/Desktop','btceur.txt'),'a') as file :
            file.writelines([str(today), ' Bitcoin price is ', str(result['bitcoin']['eur']), ' EUR', '\n'])
    elif o == '6' :
        url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=gbp'
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())
        print(today, 'Bitcoin price is', result['bitcoin']['gbp'], 'gbp', '\n')
        with open(os.path.join('C:/Users/Username/Desktop','btcgbp.txt'),'a') as file :
            file.writelines([str(today), ' Bitcoin price is ', str(result['bitcoin']['gbp']), ' GBP', '\n'])
    else:
        print('Please type correct number','\n')
    print(
        '1=ping to Coingecko api\n2=btc/usd \n3=btc/pln\n4=btc/chf\n5=btc/eur\n6=btc/gbp\n99=exit')
