# Very simple script to get information about Bitcoin price
# Originally written by Stan, remade by GrogMaster

# Imports (removed os since i don't think its important to save the price in a txt file, sorry)
import urllib.request
import json
import os
from datetime import datetime

# Main Function
def main():
    now = datetime.now()
    # I used this function to remove the milliseconds
    today = now.strftime("%d/%m/%Y %H:%M:%S")
    # More at: https://www.programiz.com/python-programming/datetime/current-datetime
    
    # o-options
    o = 0

    print("------------- Fast BitcoinChecker ------------------")
    print("------------------- Options ------------------------")
    
    print("""1   -->   Ping the Coingecko api
2   -->   BTC to USD
3   -->   BTC to PLN
4   -->   BTC to CHF
5   -->   BTC to EUR
6   -->   BTC to GBP
99  -->   EXIT the program
00  -->   CLEAR the terminal""")

    while o != 99 :
        o = input("Type number here >>> ")
        
        # Using a base url is more compact and it takes less lines of code
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies="
        
        if o == '99' :
            os.system('cls')
            print("----------------------- Bye -----------------------")
            # Yes, you can use the BREAK function, but its more specific using the QUIT() function.
            quit()
        
        elif o == '1' :
            ping_url = 'https://api.coingecko.com/api/v3/ping'
            response = urllib.request.urlopen((ping_url))
            result = json.loads(response.read())
            if result['gecko_says'] == "(V3) To the Moon!":
                print("The API is up and running. To the Moon!\n")
            else:
                print("The API is NOT up and running. Retry again later,\n")
                # Same ad above (line 41)
                quit()
            
        elif o == '2' :
            response = urllib.request.urlopen(url + "usd")
            result = json.loads(response.read())
            # Used a more efficient format string (f"string")
            print(f"today: {today}\nBitcoin price is --> {result['bitcoin']['usd']} USD\n")
            # More at: https://realpython.com/python-f-strings/            
            
        elif o == '3' :
            response = urllib.request.urlopen(url + "pln")
            result = json.loads(response.read())
            print(f"today: {today}\nBitcoin price is --> {result['bitcoin']['pln']} PLN\n")
        
        elif o == '4' :
            response = urllib.request.urlopen(url + "chf")
            result = json.loads(response.read())
            print(f"today: {today}\nBitcoin price is --> {result['bitcoin']['chf']} CHF\n")
            
        elif o == '5' :
            response = urllib.request.urlopen(url + "eur")
            result = json.loads(response.read())
            print(f"today: {today}\nBitcoin price is --> {result['bitcoin']['eur']} EUR\n") 
                
        elif o == '6' :
            response = urllib.request.urlopen(url + "gbp")
            result = json.loads(response.read())
            print(f"today: {today}\nBitcoin price is --> {result['bitcoin']['gbp']} GBP\n")
            
        # Clear the terminal
        elif o == '00':
            os.system('cls')
            # More at: https://www.geeksforgeeks.org/clear-screen-python/
            print("[terminal cleaned]")
            print("------------------- Options ------------------------")
            print("""1   -->   Ping the Coingecko api
2   -->   BTC to USD
3   -->   BTC to PLN
4   -->   BTC to CHF
5   -->   BTC to EUR
6   -->   BTC to GBP
99  -->   EXIT the program
00  -->   CLEAR the terminal""")
        
        else:
            print("Please type a correct number. Retry with a valid option.")
            print("""1   -->   Ping the Coingecko api
2   -->   BTC to USD
3   -->   BTC to PLN
4   -->   BTC to CHF
5   -->   BTC to EUR
6   -->   BTC to GBP
99  -->   EXIT the program
00  -->   CLEAR the terminal""")
            
if __name__ == "__main__":
    main()
