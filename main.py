import os, binascii, hashlib, base58, ecdsa, time, balance_checker, static


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def ripemd160(x):
    d = hashlib.new('ripemd160')
    d.update(x)
    return d


balance = 0
i = static.getint()
while True:
    i +=1
    priv_key = os.urandom(32)
    fullkey = '80' + binascii.hexlify(priv_key).decode()
    sha256a = hashlib.sha256(binascii.unhexlify(fullkey)).hexdigest()
    sha256b = hashlib.sha256(binascii.unhexlify(sha256a)).hexdigest()
    WIF = base58.b58encode(binascii.unhexlify(fullkey + sha256b[:8]))
    sk = ecdsa.SigningKey.from_string(priv_key, curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()
    publ_key = '04' + binascii.hexlify(vk.to_string()).decode()
    hash160 = ripemd160(hashlib.sha256(binascii.unhexlify(publ_key)).digest()).digest()
    publ_addr_a = b"\x00" + hash160
    checksum = hashlib.sha256(hashlib.sha256(publ_addr_a).digest()).digest()[:4]
    publ_addr_b = base58.b58encode(publ_addr_a + checksum)
    #cls()
    print('Private Key    ', str(i) + ": " + WIF.decode())
    print("Bitcoin Address", str(i) + ": " + publ_addr_b.decode())
    balance = balance_checker.get_btc(WIF.decode(),publ_addr_b.decode())
    #balance = balance_checker.get_btc(WIF.decode(),"183hmJGRuTEi2YDCWy5iozY8rZtFwVgahM")
    if balance != None and balance > 0:
        static.savekey(WIF.decode(), publ_addr_b.decode(), balance)
        static.i += 1
    print("Balance:   " + str(balance) + "\n")
    static.ink(i)

    if i % 5 == 0:
        time.sleep(2)
    if i % 10 == 0:
        time.sleep(1)
