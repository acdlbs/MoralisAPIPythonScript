import requests
import pandas as pd
import config

# api key
header = {
    'x-api-key': config.apikey
}


# ---------Contract NFT Transfers-----------
# search limit
limit = "10"
# format of numbers
type = "hex"
# store
# currently opensea
store = "0x495f947276749ce646f68ac8c248420045cb7b5e" #opensea
# store = "0xb47e3cd837ddf8e4c57f05d70ab865de6e193bbb"# cryptopunks

# GET
response = requests.get("https://deep-index.moralis.io/api/v2/nft/" + store + "/transfers?chain=eth&format=" + type + "&limit=" + limit, headers = header)

# grab json data
j = response.json()
# normilze the nested json -- grabbing the results column
norm = pd.json_normalize(j, "result")
# put it in a datafram
df = pd.DataFrame.from_dict(norm)

# grab from addresses
from_addr = df["from_address"]

# print data to file
df.to_csv('./data/data.csv')
# ------------------------------------------


for addr in from_addr:
    data = requests.get("https://deep-index.moralis.io/api/v2/" + addr + "/nft/transfers?chain=eth&format=hex&direction=both&limit=" + "3", headers = header).json()
    n = pd.json_normalize(data, "result")
    frame = pd.DataFrame.from_dict(n)
    frame.to_csv('./data/' + addr + ".csv")
