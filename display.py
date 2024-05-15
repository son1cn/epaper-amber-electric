#!/usr/bin/python3

# Import the libraries
import amberelectric
from amberelectric.api import amber_api
from datetime import datetime, timedelta
from papirus import PapirusTextPos
from papirus import Papirus

# Insert the API token you created at https://app.amber.com.au/developers
configuration = amberelectric.Configuration(
    access_token = 'psk_bc982fc781a984718d1ca2ebc769ee3c'
)

# Create an API instance
api = amber_api.AmberApi.create(configuration)

try:
    sites = api.get_sites()
except amberelectric.ApiException as e:
    print("Exception: %s\n" % e)

site_id = sites[0].id
try:
    current = api.get_current_price(site_id, next=1)
except amberelectric.ApiException as e:
    print("Exception: %s\n" % e)

print('%3.2f' %current[0].per_kwh)
next_hour = current[1].nem_time-timedelta(minutes=30)
print("forecast @" + next_hour.strftime('%H:%M') + ": %3.2f" %(current[1].per_kwh))

try:
    #usage = api.get_usage(site_id, date(2021, 6, 1), date(2021, 6, 1))
    usage = api.get_usage(site_id, datetime.now() + timedelta(days=-1), datetime.now())
except amberelectric.ApiException as e:
    print("Exception: %s\n" % e)

#print(usage)
cost = 0
kwh = 0
for i in usage:
    cost += i.cost
    kwh += i.kwh
    #print(i.start_time,i.per_kwh,i.kwh,i.cost,i.per_kwh*i.kwh)

print("Last 24Hr: \ncost $%3.2f" %(cost/100) + " kwh %3.2f" %(kwh))



# from papirus import PapirusTextPos
# from papirus import Papirus
# import time
# import requests
# #checkval.py used to pull beacon chain validator data. Contains private key so not in this repo
# import checkval
# from checkval import etherscan_api
# from datetime import datetime
# from pycoingecko import CoinGeckoAPI
# cg = CoinGeckoAPI()

# text=PapirusTextPos(False, rotation = 0)

# #date
# text.AddText("1", 0,0 , Id="date", size =35)

# #Eth header
# text.AddText("ETH:", 0,35 , Id="eth", size =28)
# text.AddText("moon", 0,60 , Id="ethcng", size =25)

# #ETH Gas price
# text.AddText("g", 0,85 , Id="gas", size =30)

# #validator
# text.AddText("val", 0,125 , Id="val", size =28)
# text.AddText("valvalue", 0,148 , Id="valvalue", size=28)

# def getETH():
#     #get ETH gas price and 24 hr change from CoinGecko
#     prices = cg.get_price(ids='ethereum', vs_currencies='usd', include_24hr_change='true')

#     eth_usd= (prices["ethereum"]['usd'])
#     eth_change= (prices["ethereum"]['usd_24h_change'])

#     #get my validator stats from the beacon chain api
#     #wrote checkval.py to pull the info and kept it in another file due to containing personal API key
#     ethval = checkval.check_val()

#     #get current ETH gas price
#     #etherscan_api is stored in checkval.py since it is private
#     url = "https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey="+etherscan_api
#     gas = requests.request("GET", url).json()['result']['ProposeGasPrice']
#     #testing new API endpoint
#     #print(gas)

#     #get current date-time
#     now = datetime.now()
#     current_time = now.strftime("%d.%m %H:%M")
#     #update screen with formatting
#     text.UpdateText("date", current_time)
    
#     text.UpdateText("eth","ETH:$"+str(eth_usd))
#     text.UpdateText("ethcng", (u"\u25B2" if eth_change>0 else u"\u25BC")+format(eth_change,'.2f')+"% 24hr")
    
#     text.UpdateText("gas","Gas:"+str(gas))
    
#     text.UpdateText("val", "Val1:"+format(ethval,'.6f'))
#     text.UpdateText("valvalue","$"+format(ethval*eth_usd,'.2f'))
#     text.WriteAll()

#     return

# data=getETH()