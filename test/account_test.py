from model.entity.account import Account
from model.entity.client import Client

client = Client(1,"ali","alipour", None)
account = Account(1, "Jari", "1234567890123456", client)
client.account = account

print(client)
print(account)