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

    @staticmethod
    @exception_handling
    def edit(name, family, username, password):
        client = Client(0, name, family, username, password)
        ClientBl.edit(client)
        return True, f"Client edited {client}"

    @staticmethod
    @exception_handling
    def remove(name, family, username, password):
        client = Client(0, name, family, username, password)
        ClientBl.remove(client)
        return True, f"Client edited {client}"

    @staticmethod
    @exception_handling
    def find_all(name, family, username, password):
        client = Client(0, name, family, username, password)
        ClientBl.find_all(client)
        return True, f"Client find_all {client}"