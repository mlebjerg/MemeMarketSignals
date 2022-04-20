import yfinance as yf
import pandas as pd
import plotly.graph_objs as go

from models import Deal, symbol

request_url = "https://www.nyse.com/api/regulatory/threshold-securities/" \
              "filter?selectedDate={}&market=&filterToken=XRT&max=10&offset=0" \
              "&pageNumber=1&sortOrder=up&sortType="

data = yf.download(
    # tickers list or string as well
    tickers=symbol,

    # use "period" instead of start/end
    # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    # (optional, default is '1mo')
    period="1d",

    # fetch data by interval (including intraday if period < 60 days)
    # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
    # (optional, default is '1d')
    interval="1m",

    # group by ticker (to access via data['SPY'])
    # (optional, default is 'column')
    group_by='ticker',

    # adjust all OHLC automatically
    # (optional, default is False)
    auto_adjust=True,

    # download pre/post regular market hours data
    # (optional, default is False)
    prepost=True,

    # use threads for mass downloading? (True/False/Integer)
    # (optional, default is True)
    threads=True,

    # proxy URL scheme use when downloading?
    # (optional, default is None)
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

l300 = pd.DataFrame(Deal.select().where(Deal.volume == 300).dicts().execute())
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
            text="⬇️",
            name="⬇️ Down",
            marker={"color": "blue"}
        )
    )

l400 = pd.DataFrame(Deal.select().where(Deal.volume == 400).dicts().execute())
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
            marker={"color": "blue"}
        )
    )

l500 = pd.DataFrame(Deal.select().where(Deal.volume == 500).dicts().execute())
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
            text="🧨",
            name="🧨 Gap it",
            marker={"color": "blue"}
        )
    )

l600 = pd.DataFrame(Deal.select().where(Deal.volume == 600).dicts().execute())
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
            text="〰",
            name="〰 Resistance",
            marker={"color": "blue"}
        )
    )

l700 = pd.DataFrame(Deal.select().where(Deal.volume == 700).dicts().execute())
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
            text="⬆️",
            name="⬆️ UP!",
            marker={"color": "blue"}
        )
    )

l777 = pd.DataFrame(Deal.select().where(Deal.volume == 777).dicts().execute())
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
            text="⬆️",
            name="⬆️ UP!",
            marker={"color": "blue"}
        )
    )

l800 = pd.DataFrame(Deal.select().where(Deal.volume == 800).dicts().execute())
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
            marker={"color": "blue"}
        )
    )

l900 = pd.DataFrame(Deal.select().where(Deal.volume == 900).dicts().execute())
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
            marker={"color": "blue"}
        )
    )

l911 = pd.DataFrame(Deal.select().where(Deal.volume == 911).dicts().execute())
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
            marker={"color": "blue"}
        )
    )

l1000 = pd.DataFrame(Deal.select().where(Deal.volume == 1000).dicts().execute())
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
            marker={"color": "blue"}
        )
    )

l2100 = pd.DataFrame(Deal.select().where(Deal.volume == 2100).dicts().execute())
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
