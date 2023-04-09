import json
import sys
import time
from iqoptionapi.stable_api import IQ_Option
#Install using pip install -U https://github.com/iqoptionapi/iqoptionapi/archive/refs/heads/master.zip
from playsound import playsound
#pip install playsound


email = ""
password = ""

API = IQ_Option(email,password)

if API.check_connect() == False:   
    #Now we can connect it
    if (API.connect()):
        print("Connected Successfully")
        # playsound('login.mp3')
    else:
        print("Oops connection failed. Use correct details or check internet connection")

else:
  pass

# API.change_balance("REAL")

balance = API.get_balance()

if balance > 0:
    API.buy_digital_spot("EURUSD-OTC",100,"call",1)
else:
    print("We can't trade")

