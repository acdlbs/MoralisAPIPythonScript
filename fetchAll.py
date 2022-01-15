import requests
import pandas as pd
import config

# api key
header = {
    'x-api-key': config.apikey
}


# ---------Contract NFT Transfers-----------
# search limit
limit = "2000"
# offset
# offset for opensea 2022-01-01 - 62768
offset = "62768"
# format of numbers
type = "hex"
# store
# currently opensea
store = "0x495f947276749ce646f68ac8c248420045cb7b5e" #opensea
# store = "0xb47e3cd837ddf8e4c57f05d70ab865de6e193bbb"# cryptopunks


# cursor
c = None

for i in range(4):
    try:
        if (c == None):
            response = requests.get("https://deep-index.moralis.io/api/v2/nft/" + store + "/transfers?chain=eth&offset=" + offset + "&format=" + type + "&limit=" + limit, headers = header)
        else:
            response = requests.get("https://deep-index.moralis.io/api/v2/nft/" + store + "/transfers?chain=eth&offset=" + offset + "&cursor=" + c + "&format=" + type + "&limit=" + limit, headers = header)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    # grab json data
    j = response.json()
    # try to set cursor
    try:
        c = j["cursor"]
        print("cursor=" + c)
    except:
        print(j)
        print(c)
        exit()

    pd.DataFrame().from_dict(j).to_csv('./data/' + str(i) + '.csv')
