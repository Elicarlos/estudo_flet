from peewee import *

import datetime


db = PostgresqlDatabase(
    'etiquetario',
    host = 'localhost',
    port = 5432,
    user = 'postgres',
    password = 'postgres'
)

class BaseModel(Model):
    class Meta:
        database = db


class Produto(BaseModel):
    descricao = CharField(max_length=50)
    preco = DecimalField(max_digits=10, decimal_places=2)


db.connect()
db.create_tables([Produto])