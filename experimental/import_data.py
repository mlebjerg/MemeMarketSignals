import json
import os
from collections import defaultdict
from datetime import datetime, date, timedelta, tzinfo
from queue import Queue
from threading import Thread
from time import sleep
import pandas as pd
import pytz
import requests
import webull.streamconn as sc
from rich.live import Live
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.table import Table as rcTable
from rich.console import Console
from webull import webull
from webull.webull import timezone

from models import Deal, Order, symbol, webull_user, webull_pass


def create_deal(deal: dict) -> None:
    Deal.create(
        symbol=symbol,
        trdBs=deal["trdBs"],
        volume=deal["volume"],
        tradeTime=datetime.strptime(deal["tradeTime"], "%H:%M:%S"),
        price=deal["price"],
        tradeDate=datetime.strptime(
            deal["tradeDate"], "%Y-%m-%d %H:%M:%S.%f%z"),
        trdEx=deal["trdEx"]
    )


def get_trades(webull, stock=None, tId=None, count=100, timeStamp=None):
    headers = webull.build_req_headers()
    if not tId is None:
        pass
    elif not stock is None:
        tId = webull.get_ticker(stock)
    else:
        raise ValueError('Must provide a stock symbol or a stock id')
    params = {'tickerId': tId, 'count': count, 'timestamp': timeStamp}
    response = requests.get("https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals",
                            params=params, headers=headers, timeout=webull.timeout)
    result = response.json()

    return pd.Series(result["data"])


webull = webull()
webull.login(
    username=webull_user,
    password=webull_pass
)
webull.get_account_id()


def get_trades_from(dt: datetime):

    i = 0
    last_trades_response = get_trades(webull=webull, stock=symbol,
                                      timeStamp=(round(datetime.now().timestamp()*1000)))
    trades = last_trades_response

    while last_trades_response.iloc[-1]["tradeStamp"] > round(dt.timestamp()*1000):
        response = get_trades(webull=webull, stock=symbol,
                              timeStamp=int(last_trades_response.iloc[-1]["tradeStamp"]-1))
        trades = pd.concat([trades, response])
        last_trades_response = response
        i += 1
        print(i)
    return trades


all_trades = get_trades_from(datetime.strptime(
    "2022-05-02T12:30:0.000+0000", "%Y-%m-%dT%H:%M:%S.%f%z"))
#all_trades = get_trades_from(datetime.now() - timedelta(hours=1, minutes=55))
print(all_trades.size)
for deal in all_trades.iloc[::-1]:

    dt = datetime.fromtimestamp(
        ((deal["tradeStamp"])/1000), tz=pytz.timezone("utc"))
    deal["tradeDate"] = dt.strftime("%Y-%m-%d %H:%M:%S.%f%z")
    # print(deal)
    # print(i)
    if deal["volume"] == "300":
        create_deal(deal)
    if deal["volume"] == "400":
        create_deal(deal)
    if deal["volume"] == "500":
        create_deal(deal)
    if deal["volume"] == "505":
        create_deal(deal)
    if deal["volume"] == "600":
        create_deal(deal)
    if deal["volume"] in ("700", "777"):
        create_deal(deal)
    if deal["volume"] == "800":
        create_deal(deal)
    if deal["volume"] == "900":
        create_deal(deal)
    if deal["volume"] == "911":
        create_deal(deal)
    if deal["volume"] == "1000":
        create_deal(deal)
    if deal["volume"] == "2100":
        create_deal(deal)
    else:
        create_deal(deal)
