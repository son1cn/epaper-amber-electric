#!/usr/bin/python3

# Import the libraries
import amberelectric
from amberelectric.api import amber_api
from datetime import datetime, timedelta
import requests
from checkamber import amber_acess_token
from papirus import PapirusTextPos
from papirus import Papirus

text=PapirusTextPos(False, rotation = 0)

#date
text.AddText("1", 0,0 , Id="date", size =35)

#Text Fields
text.AddText("Cur:", 0,35 , Id="cur", size =100)
text.AddText("Forecast", 0,125 , Id="forecast", size =25)
text.AddText("Past", 0,148 , Id="past", size=28)

# pull amber api token from the checkamber private file
configuration = amberelectric.Configuration(
    access_token = amber_access_token
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
    usage = api.get_usage(site_id, datetime.now() + timedelta(days=-2), datetime.now())
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

#get current date-time
now = datetime.now()
current_time = now.strftime("%d.%m %H:%M")
#update screen with formatting
text.UpdateText("date", current_time)

text.UpdateText("cur",format(current[0].per_kwh,'3.2f')+u"\u00A2")
text.UpdateText("forecast","forecast @" + next_hour.strftime('%H:%M') + ": %3.2f" %(current[1].per_kwh))
text.UpdateText("past", "Last 24Hr: \ncost $%3.2f" %(cost/100) + " kwh %3.2f" %(kwh))

# text.UpdateText("gas","Gas:"+str(gas))

# text.UpdateText("val", "Val1:"+format(ethval,'.6f'))
# text.UpdateText("valvalue","$"+format(ethval*eth_usd,'.2f'))
text.WriteAll()