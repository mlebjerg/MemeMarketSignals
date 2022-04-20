from queue import Queue
from threading import Thread
from time import sleep
from rich.live import Live
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.table import Table as rcTable
from rich.console import Console
from rich.spinner import Spinner, SPINNERS
from rich.status import Status
from numpy.random.mtrand import randint
from webull import webull
import pprint
import webull.streamconn as sc
import time
from webull.webull import timezone
from peewee import *
from datetime import datetime
import configparser
config = configparser.ConfigParser()
symbol = ""

config.read('.conf')

print('Enter ticker:')
symbol = input().upper()
db_name = symbol + 'db.db'
db = SqliteDatabase(db_name)
webull_user = config['DEFAULT']['webull_user']
webull_pass = config['DEFAULT']['webull_pass']


class BaseModel(Model):
    class Meta:
        database = db


class Order:
    def __init__(self, ab, price, volume, marketname):
        self.ab = ab
        self.price = price
        self.volume = volume
        self.marketname = marketname


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

print("\033c", end="")
counted_dict = {
    '100': 0,
    '200': 0,
    '300': 0,
    '400': 0,
    '500': 0,
    '505': 0,
    '600': 0,
    '700': 0,
    '777': 0,
    '800': 0,
    '900': 0,
    '911': 0,
    '1000': 0,
    '2100': 0,
    'total': 0
}


def create_deal(deal):
    Deal.create(symbol=symbol,
                trdBs=deal['trdBs'],
                volume=deal['volume'],
                tradeTime=datetime.strptime(deal['tradeTime'], "%H:%M:%S"),
                price=deal['price'],
                tradeDate=datetime.strptime(
                    deal['tradeDate'], "%Y-%m-%dT%H:%M:%S.%f%z"),
                trdEx=deal['trdEx'],)


def make_orders(json):
    data = json
    # print(data)
    if "depth" in data:
        depth = data['depth']
        ask_list = depth["ntvAggAskList"]
        bid_list = depth["ntvAggBidList"]
        orders_list = []

        for val in ask_list:
            price = val['price']
            for val in val['orderMap']:
                order = Order(
                    "ASK", price, val['volume'], val['marketName'])
                orders_list.append(order)
        for val in bid_list:
            price = val['price']
            for val in val['orderMap']:
                order = Order("BID", price, val['volume'], val['marketName'])
                orders_list.append(order)

        return orders_list

    #teststr = "{'PChang': '-14.46', 'deal': {'trdBs': 'B', 'volume': '3', 'tradeTime': '07:29:48', 'price': '1007.91', 'tradeDate': '2022-04-14T11:29:48.332+0000', 'trdEx':'NAS'}, 'pubId': 371421, 'tradeStamp': 1649935788356, 'originTime': 1649935788356, 'src': 'TR', 'dealAmount': '0.0000', 'marketValue': '1056627176258','tradeTime': '2022-04-14T11:29:48.332+0000', 'negMarketValue': '862434638118.33', 'PPrice': '1007.91', 'tickerId': 913255598, 'trdSeq': 5343, 'PChRatio':'-0.0141', 'status': 'F'}"
    if "deal" in data:
        deal = data['deal']
        color_str = None

        if deal['trdBs'] == 'S':
            color_str = "[red]"
        elif deal['trdBs'] == 'B':
            color_str = "[green]"
        elif deal['trdBs'] == 'G':
            color_str = "[white on dark_green]"
        elif deal['trdBs'] == 'N':
            color_str = "[grey62]"
        elif deal['trdBs'] == 'L':
            color_str = "[white on red3]"
        else:
            color_str = deal['trdBs']
        base_str = color_str + deal['tradeTime'] + " on " + deal['trdEx'] + " "
        # console.print(data)
        if deal['volume'] == "100":
            console.print(base_str + "I need Shares")
        if deal['volume'] == "200":
            console.print(
                base_str + "I need Shares badly do not take stock down")
        if deal['volume'] == "300":
            console.print(
                base_str + "Take/Taking the stock down so I can load shares")
            create_deal(deal)
        if deal['volume'] == "400":
            console.print(base_str + "Keep trading it sideways")
            create_deal(deal)
        if deal['volume'] == "500":
            direction = ""
            if deal['trdBs'] == "B" or deal['trdBs'] == "G":
                direction = "up ⬆️"
            elif deal['trdBs'] == "S" or deal['trdBs'] == "L":
                direction = "down ⬇️"
            console.print(base_str + "Gap the stock " + direction)
            create_deal(deal)

        if deal['volume'] == "505":
            console.print(base_str + "I am short on shares")
            create_deal(deal)

        if deal['volume'] == "600":
            console.print(base_str + "Apply resistance at " + deal['price'])
            create_deal(deal)

        if deal['volume'] == "700":
            console.print(base_str + "Move the price up")
            create_deal(deal)

        if deal['volume'] == "777":
            console.print(base_str + "Move the price up")
            create_deal(deal)

        if deal['volume'] == "800":
            console.print(base_str + "Volume coming")
            create_deal(deal)

        if deal['volume'] == "900":
            console.print(base_str + "Let it trade freely")
            create_deal(deal)

        if deal['volume'] == "911":
            console.print(base_str + "NEWS PENDING")
            create_deal(deal)

        if deal['volume'] == "1000":
            console.print(base_str + "Don't let it run!")
            create_deal(deal)

        if deal['volume'] == "2100":
            console.print(base_str + "Let it run!")
            create_deal(deal)

        # else:
        #    console.print(base_str + deal['volume'])

    else:
        return []


def count_signals(order_list):
    count_dict = {
        '100': 0,
        '200': 0,
        '300': 0,
        '400': 0,
        '500': 0,
        '505': 0,
        '600': 0,
        '700': 0,
        '777': 0,
        '800': 0,
        '900': 0,
        '911': 0,
        '1000': 0,
        '2100': 0,
        'total': 0
    }
    for val in order_list:
        vol = val.volume

        if vol == 100:
            count_dict['100'] += 1
            count_dict['total'] += 1
        if vol == 200:
            count_dict['200'] += 1
            count_dict['total'] += 1
        if vol == 300:
            count_dict['300'] += 1
            count_dict['total'] += 1
        if vol == 400:
            count_dict['400'] += 1
            count_dict['total'] += 1
        if vol == 500:
            count_dict['500'] += 1
            count_dict['total'] += 1
        if vol == 505:
            count_dict['505'] += 1
            count_dict['total'] += 1
        if vol == 600:
            count_dict['600'] += 1
            count_dict['total'] += 1
        if vol == 700:
            count_dict['700'] += 1
            count_dict['total'] += 1
        if vol == 777:
            count_dict['777'] += 1
            count_dict['total'] += 1
        if vol == 800:
            count_dict['800'] += 1
            count_dict['total'] += 1
        if vol == 900:
            count_dict['900'] += 1
            count_dict['total'] += 1
        if vol == 911:
            count_dict['911'] += 1
            count_dict['total'] += 1
        if vol == 1000:
            count_dict['1000'] += 1
            count_dict['total'] += 1
        if vol == 2100:
            count_dict['2100'] += 1
            count_dict['total'] += 1
    return count_dict


queue = Queue()


def on_price_message(topic, data):
    # print(data)
    order_list = make_orders(data)
    if order_list is not None:
        if len(order_list) != 0:
            counted_dict = count_signals(order_list)
            # print(counted_dict)
            queue.put(counted_dict)


def on_order_message(topic, data):
    print("order")


def get_counted_dict():
    return counted_dict


console = Console()
webull = webull()
webull.login(webull_user, webull_pass)
webull.get_account_id()

print("\033c", end="")
tId = webull.get_ticker(stock=symbol)
nyc = timezone('America/New_York')
conn = sc.StreamConn(debug_flg=False)
conn.price_func = on_price_message
conn.order_func = on_order_message
if not webull._access_token is None and len(webull._access_token) > 1:
    conn.connect(webull._did, access_token=webull._access_token)
else:
    conn.connect(webull._did)

conn.subscribe(tId=tId, level=108)

status = Progress(
    "{task.description}",
    SpinnerColumn("moon"),
)
job_progress = Progress(
    "{task.description}",
    BarColumn(),
    TextColumn(
        "[progress.percentage]{task.completed:>3.0f}/[progress.total]{task.total}"),
)
status.add_task("[green]Live")
l100 = job_progress.add_task(
    "[green]100", completed=counted_dict['100'], total=0)
l200 = job_progress.add_task(
    "[green]200", completed=counted_dict['200'], total=0)
l300 = job_progress.add_task(
    "[red]300", completed=counted_dict['300'], total=0)
l400 = job_progress.add_task(
    "[grey]400", completed=counted_dict['400'], total=0)
l500 = job_progress.add_task(
    "[blue]500", completed=counted_dict['500'], total=0)
l505 = job_progress.add_task(
    "[red]505", completed=counted_dict['505'], total=0)
l600 = job_progress.add_task(
    "[red]600", completed=counted_dict['600'], total=0)
l700 = job_progress.add_task(
    "[green]700", completed=counted_dict['700'], total=0)
l777 = job_progress.add_task(
    "[green]777", completed=counted_dict['777'], total=0)
l800 = job_progress.add_task(
    "[cyan]800", completed=counted_dict['800'], total=0)
l900 = job_progress.add_task(
    "[green]900", completed=counted_dict['900'], total=0)
l911 = job_progress.add_task(
    "[purple]911", completed=counted_dict['911'], total=0)
l1000 = job_progress.add_task(
    "[red]1000", completed=counted_dict['1000'], total=0)
l2100 = job_progress.add_task(
    "[green]2100", completed=counted_dict['2100'], total=0)

total = sum(task.total for task in job_progress.tasks)
overall_progress = Progress()
overall_task = overall_progress.add_task("All Jobs", total=int(total))

progress_table = rcTable.grid()
progress_table.add_row(status)
progress_table.add_row(
    Panel.fit(job_progress, title="[b] " + symbol + " Signals",
              border_style="green", padding=(1, 2)),
)


def output():

    with Live(progress_table, console=console, refresh_per_second=10) as live:
        while 1:
            sleep(0.1)
            counted_dict = queue.get()
            if conn.client_streaming_quotes.is_connected() is False:
                job_progress.stop_task(status)
                conn.connect()

            job_progress.update(
                l100, completed=counted_dict['100'], total=counted_dict['total'])
            job_progress.update(
                l200, completed=counted_dict['200'], total=counted_dict['total'])
            job_progress.update(
                l300, completed=counted_dict['300'], total=counted_dict['total'])
            job_progress.update(
                l400, completed=counted_dict['400'], total=counted_dict['total'])
            job_progress.update(
                l500, completed=counted_dict['500'], total=counted_dict['total'])
            job_progress.update(
                l505, completed=counted_dict['505'], total=counted_dict['total'])
            job_progress.update(
                l600, completed=counted_dict['600'], total=counted_dict['total'])
            job_progress.update(
                l700, completed=counted_dict['700'], total=counted_dict['total'])
            job_progress.update(
                l777, completed=counted_dict['777'], total=counted_dict['total'])
            job_progress.update(
                l800, completed=counted_dict['800'], total=counted_dict['total'])
            job_progress.update(
                l900, completed=counted_dict['900'], total=counted_dict['total'])
            job_progress.update(
                l911, completed=counted_dict['911'], total=counted_dict['total'])
            job_progress.update(
                l1000, completed=counted_dict['1000'], total=counted_dict['total'])
            job_progress.update(
                l2100, completed=counted_dict['2100'], total=counted_dict['total'])


Thread(target=output, daemon=True).start()
conn.run_blocking_loop()
