from template_maker import entity_maker, da_maker

entity_maker("Client", ["id", "name", "model", "plate"])

da_maker("Cars", ["id", "name", "model", "plate"])