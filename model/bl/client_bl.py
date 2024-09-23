from model.da.client_da import ClientDa


class ClientBl:
    @staticmethod
    def save(client):
        client_da = ClientDa()
        return client_da.save(client)