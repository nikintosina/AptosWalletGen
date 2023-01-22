from aptos_sdk.account import Account
from aptos_sdk.client import FaucetClient, RestClient
f = open("private_keys_storage.txt", "a")

x = int(input("How many private keys do you want to generate? "))

for i in range(x):
        alice = Account.generate()
        prvk = str(alice.private_key)
        f.write(prvk)
        f.write("\n")

f.close()
