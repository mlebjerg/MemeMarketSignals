import configparser
from peewee import *


print("Enter ticker:")
symbol = input().upper()
config = configparser.ConfigParser()
config.read('.conf')
webull_user = config['DEFAULT']['webull_user']
webull_pass = config['DEFAULT']['webull_pass']

db = SqliteDatabase(f"databases/{symbol}db.db")


class BaseModel(Model):
    class Meta:
        database = db


class Order:
    def __init__(self, ab, price, volume, market_name):
        self.ab = ab
        self.price = price
        self.volume = volume
        self.market_name = market_name


class Deal(BaseModel):
    symbol = CharField()
    trdBs = CharField()
    volume = IntegerField()
    tradeTime = TimeField()
    price = FloatField()
    tradeDate = DateTimeField()
    trdEx = TextField()


db.connect()
db.create_tables([Deal])
