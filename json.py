import pandas as pd
import numpy as np
import requests
import json
url = 'http://yourlinktojson'
data = requests.get(url).json()
data = pd.DataFrame(data)
data = data.loc[:,['id', 'price', 'ticker']]
data = data.rename(index=str, columns={'id':'isin','price':'price','ticker':'ticker'})
data.to_json('ateet_v1.json' , orient='records')