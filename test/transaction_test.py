from model.entity.account import Account
from model.entity.client import Client
from model.entity.transaction import Transaction

client1 = Client(1, "ali", "alizad", "ali123", "ALI23")
account1 = Account(1, "saving", "1234567890123456", client1)


client2 = Client(1, "reza", "rezai", "reza345", "Reza1234")
account2 = Account(1, "saving", "1234567890123456", client2)


transaction = Transaction(1, "done", 1500, "2024-09-11 8:20", client1, client2)


print(transaction)

