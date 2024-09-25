from model.entity.account import Account
from model.entity.client import Client

client = Client(1, "ali", "alizad", "ali1234", "123ali")
account = Account(1, "Jari", "1234567890123456", "reza")
client.account = account

print(client)
print(account)