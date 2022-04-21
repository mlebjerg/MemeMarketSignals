from datetime import datetime, date
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go

from models import Deal, symbol

request_url = "https://www.nyse.com/api/regulatory/threshold-securities/" \
              "filter?selectedDate={}&market=&filterToken=XRT&max=10&offset=0" \
              "&pageNumber=1&sortOrder=up&sortType="

data = yf.download(
    tickers=symbol,
    period="1d",
    interval="1m",
    group_by='ticker',
    auto_adjust=True,
    prepost=True,
    threads=True,
    proxy=None
)

fig = go.Figure()
fig.add_trace(go.Candlestick())
fig.add_trace(
    go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        name='market data')
)
today = date.today()
print(today)
l300 = pd.DataFrame(Deal.select().where(
    Deal.tradeDate.startswith(str(today)),
    Deal.volume == 300).dicts().execute())
if not l300.empty:
    l300["tradeDate"] = pd.to_datetime(
        l300["tradeDate"],
        format="%Y-%m-%dT%H:%M:%S.%f%z"
    )
    fig.add_trace(
        go.Scatter(
            x=l300["tradeDate"].dt.tz_convert('America/New_York'),
            y=l300.price,
            mode="text",
            text="🔻",
            name="🔻 Down",
            hovertext="Exchange: " + l300.trdEx + " Direction: " + l300.trdBs,
            marker={"color": "blue"}
        )
    )

l400 = pd.DataFrame(Deal.select().where(Deal.tradeDate.startswith(
    str(today)), Deal.volume == 400).dicts().execute())
if not l400.empty:
    l400["tradeDate"] = pd.to_datetime(
        l400["tradeDate"],
        format="%Y-%m-%dT%H:%M:%S.%f%z"
    )
    fig.add_trace(
        go.Scatter(
            x=l400["tradeDate"].dt.tz_convert('America/New_York'),
            y=l400.price,
            mode="text",
            text="➡️",
            name="➡️ Sideways",
            hovertext="Exchange: " + l400.trdEx + " Direction: " + l400.trdBs,
            marker={"color": "blue"}
        )
    )

l500 = pd.DataFrame(Deal.select().where(Deal.tradeDate.startswith(
    str(today)), Deal.volume == 500).dicts().execute())
if not l500.empty:
    l500["tradeDate"] = pd.to_datetime(
        l500["tradeDate"],
        format="%Y-%m-%dT%H:%M:%S.%f%z"
    )
    fig.add_trace(
        go.Scatter(
            x=l500["tradeDate"].dt.tz_convert('America/New_York'),
            y=l500.price,
            mode="text",
            text="💥",
            name="💥 Gap it",
            hovertext="Exchange: " + l500.trdEx + " Direction: " + l500.trdBs,
            marker={"color": "blue"}
        )
    )

l505 = pd.DataFrame(Deal.select().where(Deal.tradeDate.startswith(
    str(today)), Deal.volume == 505).dicts().execute())
if not l505.empty:
    l505["tradeDate"] = pd.to_datetime(
        l505["tradeDate"],
        format="%Y-%m-%dT%H:%M:%S.%f%z"
    )
    fig.add_trace(
        go.Scatter(
            x=l505["tradeDate"].dt.tz_convert('America/New_York'),
            y=l505.price,
            mode="text",
            text="🤷‍♂️",
            name="🤷‍♂️ I am short on shares ",
            hovertext="Exchange: " + l505.trdEx + " Direction: " + l505.trdBs,
            marker={"color": "blue"}
        )
    )

l600 = pd.DataFrame(Deal.select().where(Deal.tradeDate.startswith(
    str(today)), Deal.volume == 600).dicts().execute())
if not l600.empty:
    l600["tradeDate"] = pd.to_datetime(
        l600["tradeDate"],
        format="%Y-%m-%dT%H:%M:%S.%f%z"
    )
    fig.add_trace(
        go.Scatter(
            x=l600["tradeDate"].dt.tz_convert('America/New_York'),
            y=l600.price,
            mode="text",
            text="🔹",
            name="🔹 Resistance",
            hovertext="Exchange: " + l600.trdEx + " Direction: " + l600.trdBs,
            marker={"color": "blue"}
        )
    )

l700 = pd.DataFrame(Deal.select().where(Deal.tradeDate.startswith(
    str(today)), Deal.volume == 700).dicts().execute())
if not l700.empty:
    l700["tradeDate"] = pd.to_datetime(
        l700["tradeDate"],
        format="%Y-%m-%dT%H:%M:%S.%f%z"
    )
    fig.add_trace(
        go.Scatter(
            x=l700["tradeDate"].dt.tz_convert('America/New_York'),
            y=l700.price,
            mode="text",
            text="💹",
            name="💹 UP!",
            hovertext="Exchange: " + l700.trdEx + " Direction: " + l700.trdBs,
            marker={"color": "blue"}
        )
    )

l777 = pd.DataFrame(Deal.select().where(Deal.tradeDate.startswith(
    str(today)), Deal.volume == 777).dicts().execute())
if not l777.empty:
    l777["tradeDate"] = pd.to_datetime(
        l777["tradeDate"],
        format="%Y-%m-%dT%H:%M:%S.%f%z"
    )
    fig.add_trace(
        go.Scatter(
            x=l777["tradeDate"].dt.tz_convert('America/New_York'),
            y=l777.price,
            mode="text",
            text="💹",
            name="💹 UP!",
            hovertext="Exchange: " + l777.trdEx + " Direction: " + l777.trdBs,
            marker={"color": "blue"}
        )
    )

l800 = pd.DataFrame(Deal.select().where(Deal.tradeDate.startswith(
    str(today)), Deal.volume == 800).dicts().execute())
if not l800.empty:
    l800["tradeDate"] = pd.to_datetime(
        l800["tradeDate"],
        format="%Y-%m-%dT%H:%M:%S.%f%z"
    )
    fig.add_trace(
        go.Scatter(
            x=l800["tradeDate"].dt.tz_convert('America/New_York'),
            y=l800.price,
            mode="text",
            text="🔊",
            name="🔊 Volume coming",
            hovertext="Exchange: " + l800.trdEx + " Direction: " + l800.trdBs,
            marker={"color": "blue"}
        )
    )

l900 = pd.DataFrame(Deal.select().where(Deal.tradeDate.startswith(
    str(today)), Deal.volume == 900).dicts().execute())
if not l900.empty:
    l900["tradeDate"] = pd.to_datetime(
        l900["tradeDate"],
        format="%Y-%m-%dT%H:%M:%S.%f%z"
    )
    fig.add_trace(
        go.Scatter(
            x=l900["tradeDate"].dt.tz_convert('America/New_York'),
            y=l900.price,
            mode="text",
            text="🕊️",
            name="🕊️ Trade free",
            hovertext="Exchange: " + l900.trdEx + " Direction: " + l900.trdBs,
            marker={"color": "blue"}
        )
    )

l911 = pd.DataFrame(Deal.select().where(Deal.tradeDate.startswith(
    str(today)), Deal.volume == 911).dicts().execute())
if not l911.empty:
    l911["tradeDate"] = pd.to_datetime(
        l911["tradeDate"],
        format="%Y-%m-%dT%H:%M:%S.%f%z"
    )
    fig.add_trace(
        go.Scatter(
            x=l911["tradeDate"].dt.tz_convert('America/New_York'),
            y=l911.price,
            mode="text",
            text="📰",
            name="📰 NEWS",
            hovertext="Exchange: " + l911.trdEx + " Direction: " + l911.trdBs,
            marker={"color": "blue"}
        )
    )

l1000 = pd.DataFrame(Deal.select().where(Deal.tradeDate.startswith(str(today)),
                                         Deal.volume == 1000).dicts().execute())
if not l1000.empty:
    l1000["tradeDate"] = pd.to_datetime(
        l1000["tradeDate"],
        format="%Y-%m-%dT%H:%M:%S.%f%z"
    )
    fig.add_trace(
        go.Scatter(
            x=l1000["tradeDate"].dt.tz_convert('America/New_York'),
            y=l1000.price,
            mode="text",
            text="🛑",
            name="🛑 Don't let it run",
            hovertext="Exchange: " + l1000.trdEx + " Direction: " + l1000.trdBs,
            marker={"color": "blue"}
        )
    )

l2100 = pd.DataFrame(Deal.select().where(Deal.tradeDate.startswith(str(today)),
                                         Deal.volume == 2100).dicts().execute())
if not l2100.empty:
    l2100["tradeDate"] = pd.to_datetime(
        l2100["tradeDate"],
        format="%Y-%m-%dT%H:%M:%S.%f%z"
    )
    fig.add_trace(
        go.Scatter(
            x=l2100["tradeDate"].dt.tz_convert('America/New_York'),
            y=l2100.price,
            mode="text",
            text="🚀",
            name="🚀 Let it run",
            hovertext="Exchange: " + l2100.trdEx + " Direction: " + l2100.trdBs,
            marker={"color": "blue"}
        )
    )

fig.update_layout(
    title="{} share price".format(symbol),
    template="plotly_dark",
    yaxis_title="Stock Price (USD)",
    shapes=list()
)

fig.show()
