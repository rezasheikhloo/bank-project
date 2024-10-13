from model.da.client_da import ClientDa

class ClientBl:
    @staticmethod
    def save(client):
        client_da = ClientDa()
        return client_da.save(client)

    @staticmethod
    def edit(client):
        client_da = ClientDa()
        return client_da.edit(client)

    @staticmethod
    def remove(client):
        client_da = ClientDa()
        return client_da.remove(client)

    @staticmethod
    def find_all(client):
        client_da = ClientDa()
        return client_da.find_all(client)