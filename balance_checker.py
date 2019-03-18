import requests, static

def frominsightapi(key, address, baseurl, chain):
    try:
        r = requests.get(baseurl + 'addr/%s/?noTxList=1' % address)
        if r.text != 'Invalid address: Address has mismatched network type.. Code:1':
            balance = r.json()['balance']
            try:
                val = float(balance)
                if val is None:
                    static.errors(key,address)
                    return 0
                return val
            except:
                static.errors(key,address)
                return 0
        else:
            static.errors(key, address)
            return 0
    except:
        static.errors(key, address)
        return 0


def get_btc(key, address):
    chain = "BTC"
    return frominsightapi(key, address, 'https://insight.bitpay.com/api/', chain)
