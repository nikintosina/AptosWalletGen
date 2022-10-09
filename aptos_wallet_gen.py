from aptos_sdk.account import Account
from aptos_sdk.client import FaucetClient, RestClient
f = open("C:/Users/nickman/aptosproj/myownstuff/private_keys_storage.txt", "a")

for i in range(4):
        alice = Account.generate()
        prvk = str(alice.private_key)
        f.write(prvk)
        f.write("\n")

f.close()


