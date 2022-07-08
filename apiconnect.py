import datetime
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

#function for getting the currency pair exchange rate from the API

def get_rate(cur_pair):

    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)

    pair = f"{cur_pair[:3]}_{cur_pair[4:]}".upper()

    now = requests.get(f"https://free.currconv.com/api/v7/convert?q={pair}&compact=ultra&apiKey={API_KEY}")
    yest = requests.get(f"https://free.currconv.com/api/v7/convert?q={pair}&compact=ultra&date={yesterday}&apiKey={API_KEY}")
    output = now.json()
    yest_output = yest.json()

    if (len(output) == 0 or (pair, 1) in output.items()) and ("status", 400) in yest_output.items():
        print("Currency pair not found")

    elif ("status", 400) in output.items():
        print("Cannot connect to API")

    else:
        out = output[pair]
        out_rounded = round(out, 2)
        if out - yest_output[pair][f"{yesterday}"] >= 0:
            print(f"\033[92m{out_rounded}\033[00m")
            color = "green"
            return out_rounded, color
        else:
            print(f"\033[91m{out_rounded}\033[00m")
            color = "red"
            return out_rounded, color
