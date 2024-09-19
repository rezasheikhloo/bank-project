from template_maker import entity_maker, da_maker

entity_maker("Transaction", ["id", "creation_date", "status", "amount"])

da_maker("Transaction", ["id", "creation_date", "status", "amount"])