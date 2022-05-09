import os
from collections import defaultdict
from datetime import datetime
from queue import Queue
from threading import Thread
from time import sleep

import webull.streamconn as sc
from rich.live import Live
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.table import Table as rcTable
from rich.console import Console
from webull import webull
from webull.webull import timezone

from models import Deal, Order, symbol, webull_user, webull_pass

print("\033c", end="")


def create_deal(deal: dict) -> None:
    Deal.create(
        symbol=symbol,
        trdBs=deal["trdBs"],
        volume=deal["volume"],
        tradeTime=datetime.strptime(deal["tradeTime"], "%H:%M:%S"),
        price=deal["price"],
        tradeDate=datetime.strptime(
            deal["tradeDate"], "%Y-%m-%dT%H:%M:%S.%f%z"),
        trdEx=deal["trdEx"]
    )


def make_orders(data: dict) -> list:
    if "depth" in data:
        depth = data["depth"]
        ask_list = depth["ntvAggAskList"]
        bid_list = depth["ntvAggBidList"]
        orders = list()

        for ask in ask_list:
            for ask_order in ask["orderMap"]:
                orders.append(
                    Order("ASK", ask["price"],
                          ask_order["volume"], ask_order["marketName"]))
        for bid in bid_list:
            for bid_order in bid["orderMap"]:
                orders.append(
                    Order("BID", bid["price"],
                          bid_order["volume"], bid_order["marketName"]))

        return orders

    if "deal" in data:
        deal: dict = data["deal"]

        deal_colors = {
            "S": "[red]",
            "B": "[green]",
            "G": "[white on dark green]",
            "N": "[grey62]",
            "L": "[white on red3]"
        }

        color_str = deal_colors[deal["trdBs"]]
        base_str = f"{color_str}{deal['tradeTime']} on {deal['trdEx']} "

        if deal["volume"] == "100":
            console.print(f"{base_str} I need Shares.")
        if deal["volume"] == "200":
            console.print(
                f"{base_str} I need Shares badly! Do not take stock down.")
        if deal["volume"] == "300":
            console.print(
                f"{base_str} Take/Taking the stock down so I can load shares.")
            create_deal(deal)
        if deal["volume"] == "400":
            console.print(f"{base_str} Keep trading it sideways.")
            create_deal(deal)
        if deal["volume"] == "500":
            direction = "up ⬆️" if deal["trdBs"] in ("B", "G") else "down ⬇️"
            console.print(f"{base_str} Gap the stock {direction} ")
            create_deal(deal)

        if deal["volume"] == "505":
            console.print(f"{base_str} I am short on shares.")
            create_deal(deal)

        if deal["volume"] == "600":
            console.print(f"{base_str} Apply resistance at {deal['price']}")
            create_deal(deal)

        if deal["volume"] in ("700", "777"):
            console.print(f"{base_str} Move the price up.")
            create_deal(deal)

        if deal["volume"] == "800":
            console.print(f"{base_str} Volume coming.")
            create_deal(deal)

        if deal["volume"] == "900":
            console.print(f"{base_str} Let it trade freely.")
            create_deal(deal)

        if deal["volume"] == "911":
            console.print(f"{base_str} NEWS PENDING.")
            create_deal(deal)

        if deal["volume"] == "1000":
            console.print(f"{base_str} Don't let it run!")
            create_deal(deal)

        if deal["volume"] == "2100":
            console.print(f"{base_str} Let it run!")
            create_deal(deal)

    else:
        return []


def count_signals(orders: list) -> dict:
    count = defaultdict(int)

    for value in orders:
        count[str(value.volume)] += 1
        count["total"] += 1

    return count


queue = Queue()


def on_price_message(_, data) -> None:
    order_list = make_orders(data)
    if order_list is not None and len(order_list) > 0:
        queue.put(count_signals(order_list))


console = Console()

webull = webull()
webull.login(
    username=webull_user,
    password=webull_pass
)
webull.get_account_id()

print("\033c", end="")
tId = webull.get_ticker(stock=symbol)
nyc = timezone('America/New_York')
conn = sc.StreamConn(debug_flg=False)
conn.price_func = on_price_message
conn.order_func = lambda: print("order")

if webull._access_token is not None and len(webull._access_token) > 1:
    conn.connect(webull._did, access_token=webull._access_token)
else:
    conn.connect(webull._did)

conn.subscribe(tId=tId, level=108)

status = Progress("{task.description}", SpinnerColumn("moon"))
job_progress = Progress(
    "{task.description}",
    BarColumn(),
    TextColumn(
        "[progress.percentage]{task.completed:>3.0f}/"
        "[progress.total]{task.total}")
)

status.add_task("[green]Live")

counted_dict = defaultdict(int)
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
    with Live(progress_table, console=console, refresh_per_second=10):
        while True:
            sleep(0.1)
            count = queue.get()
            if conn.client_streaming_quotes.is_connected() is False:
                job_progress.stop_task(status)
                conn.connect()

            job_progress.update(l100, completed=count['100'],
                                total=count['total'])
            job_progress.update(l200, completed=count['200'],
                                total=count['total'])
            job_progress.update(l300, completed=count['300'],
                                total=count['total'])
            job_progress.update(l400, completed=count['400'],
                                total=count['total'])
            job_progress.update(l500, completed=count['500'],
                                total=count['total'])
            job_progress.update(l505, completed=count['505'],
                                total=count['total'])
            job_progress.update(l600, completed=count['600'],
                                total=count['total'])
            job_progress.update(l700, completed=count['700'],
                                total=count['total'])
            job_progress.update(l777, completed=count['777'],
                                total=count['total'])
            job_progress.update(l800, completed=count['800'],
                                total=count['total'])
            job_progress.update(l900, completed=count['900'],
                                total=count['total'])
            job_progress.update(l911, completed=count['911'],
                                total=count['total'])
            job_progress.update(l1000, completed=count['1000'],
                                total=count['total'])
            job_progress.update(l2100, completed=count['2100'],
                                total=count['total'])


Thread(target=output, daemon=True).start()
conn.run_blocking_loop()
