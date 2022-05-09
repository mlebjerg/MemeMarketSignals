from datetime import datetime, date
from itertools import count
import os
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
from webull import webull
from models import Deal, symbol

l600 = Deal.select().where(Deal.volume == 600).dicts().execute()
# print(l600)
for i in l600:
    dt = datetime.strptime(i["tradeDate"], "%Y-%m-%d %H:%M:%S.%f%z")
    # print(
    #    f'gaps := time >= timestamp({dt.year}, {dt.month}, {dt.day}, {dt.hour}, {dt.minute}) ? {i["price"]} : gaps')
    print(
        f'label.new(timestamp({dt.year}, {dt.month}, {dt.day}, {dt.hour-4}, {dt.minute}, {dt.second}), {i["price"]},xloc=xloc.bar_time, style=label.style_diamond,size=size.tiny)')
