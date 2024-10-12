from model.bl.client_bl import ClientBl
from model.entity.client import Client
from tools.decorators import exception_handling


class ClientController:
    @staticmethod
    @exception_handling
    def save(name, family, username, password):
        client = Client(0, name, family, username, password)
        ClientBl.save(client)
        return True, f"Client Saved {client}"

    def edit(self, name, family, username, password):
        pass

    def find_all(self, name, family, username, password):
        pass