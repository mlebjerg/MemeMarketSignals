import os
from numpy import empty
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
from datetime import datetime, date

request_url = "https://www.nyse.com/api/regulatory/threshold-securities/" \
              "filter?selectedDate={}&market=&filterToken=XRT&max=10&offset=0" \
              "&pageNumber=1&sortOrder=up&sortType="
df = pd.read_csv('csvs/gme_TBTAL_20220506.csv', delimiter="|", names=[
                 "datetime", "tickType", "time", "price", "size", "tickAttribLast", "exchange", "specialConditions"])


symbol = "GME"
data = yf.download(
    tickers=symbol,
    period="1d",
    # start="2022-04-26",
    # end="2022-04-27",
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

l300 = df.loc[df['size'] == 300]
l400 = df.loc[df['size'] == 400]
l500 = df.loc[df['size'] == 500]
l505 = df.loc[df['size'] == 505]
l600 = df.loc[df['size'] == 600]
l700 = df.loc[df['size'] == 700]
l777 = df.loc[df['size'] == 777]
l800 = df.loc[df['size'] == 800]
l900 = df.loc[df['size'] == 900]
l911 = df.loc[df['size'] == 911]
l1000 = df.loc[df['size'] == 1000]
l2100 = df.loc[df['size'] == 2100]

if not l300.empty:

    fig.add_trace(
        go.Scatter(
            x=l300.datetime,
            y=l300.price,
            mode="text",
            text="🔻",
            name="🔻 Down",
            hovertext="Exchange: " + l300.exchange + " Tick type: " + l300.tickAttribLast,
            marker={"color": "blue"}
        )
    )
if not l400.empty:

    fig.add_trace(
        go.Scatter(
            x=l400.datetime,
            y=l400.price,
            mode="text",
            text="➡️",
            name="➡️ Sideways",
            hovertext="Exchange: " + l400.exchange + " Tick type: " + l400.tickAttribLast,
            marker={"color": "blue"}
        )
    )

if not l500.empty:

    fig.add_trace(
        go.Scatter(
            x=l500.datetime,
            y=l500.price,
            mode="text",
            text="💥",
            name="💥 Gap it",
            hovertext="Exchange: " + l500.exchange + " Tick type: " + l500.tickAttribLast,
            marker={"color": "blue"}
        )
    )

if not l505.empty:

    fig.add_trace(
        go.Scatter(
            x=l505.datetime,
            y=l505.price,
            mode="text",
            text="🤷‍♂️",
            name="🤷‍♂️ I am short on shares ",
            hovertext="Exchange: " + l505.exchange + " Tick type: " + l505.tickAttribLast,
            marker={"color": "blue"}
        )
    )

if not l600.empty:

    fig.add_trace(
        go.Scatter(
            x=l600.datetime,
            y=l600.price,
            mode="text",
            text="🔹",
            name="🔹 Resistance",
            hovertext="Exchange: " + l600.exchange + " Tick type: " + l600.tickAttribLast,
            marker={"color": "blue"}
        )
    )

if not l700.empty:

    fig.add_trace(
        go.Scatter(
            x=l700.datetime,
            y=l700.price,
            mode="text",
            text="💹",
            name="💹 UP!",
            hovertext="Exchange: " + l700.exchange + " Tick type: " + l700.tickAttribLast,
            marker={"color": "blue"}
        )
    )

if not l777.empty:

    fig.add_trace(
        go.Scatter(
            x=l777.datetime,
            y=l777.price,
            mode="text",
            text="💹",
            name="💹 UP!",
            hovertext="Exchange: " + l777.exchange + " Tick type: " + l777.tickAttribLast,
            marker={"color": "blue"}
        )
    )

if not l800.empty:

    fig.add_trace(
        go.Scatter(
            x=l800.datetime,
            y=l800.price,
            mode="text",
            text="🔊",
            name="🔊 Volume coming",
            hovertext="Exchange: " + l800.exchange + " Tick type: " + l800.tickAttribLast,
            marker={"color": "blue"}
        )
    )

if not l900.empty:

    fig.add_trace(
        go.Scatter(
            x=l900.datetime,
            y=l900.price,
            mode="text",
            text="🕊️",
            name="🕊️ Trade free",
            hovertext="Exchange: " + l900.exchange + " Tick type: " + l900.tickAttribLast,
            marker={"color": "blue"}
        )
    )

if not l911.empty:

    fig.add_trace(
        go.Scatter(
            x=l911.datetime,
            y=l911.price,
            mode="text",
            text="📰",
            name="📰 NEWS",
            hovertext="Exchange: " + l911.exchange + " Tick type: " + l911.tickAttribLast,
            marker={"color": "blue"}
        )
    )

if not l1000.empty:
    fig.add_trace(
        go.Scatter(
            x=l1000.datetime,
            y=l1000.price,
            mode="text",
            text="🛑",
            name="🛑 Don't let it run",
            hovertext="Exchange: " + l1000.exchange +
            " Tick type: " + l1000.tickAttribLast,
            marker={"color": "blue"}
        )
    )

if not l2100.empty:
    fig.add_trace(
        go.Scatter(
            x=l2100.datetime,
            y=l2100.price,
            mode="text",
            text="🚀",
            name="🚀 Let it run",
            hovertext="Exchange: " + l2100.exchange +
            " Tick type: " + l2100.tickAttribLast,
            marker={"color": "blue"}
        )
    )

fig.update_layout(
    title="{} share price".format(symbol),
    template="plotly_dark",
    yaxis_title="Stock Price (USD)",
    shapes=list()
)
exch_signals = pd.concat([l300,
                          l400,
                          l500,
                          l505,
                          l600,
                          l700,
                          l777,
                          l800,
                          l900,
                          l911,
                          l1000,
                          l2100, ]).exchange.value_counts()
trd_exch = df.exchange.value_counts()
exch_signals.name = "Counts"
trd_exch.name = "Counts"


# fig.show()

today = date.today()
os.mkdir(f"graphs/{today.strftime('%d%b')}{symbol}")
fig.write_html(f"graphs/{today.strftime('%d%b')}{symbol}/index.html")
sign_counts = {"300's": len(l300),
               "400's": len(l400),
               "500's": len(l500),
               "505's": len(l505),
               "600's": len(l600),
               "700's": len(l700),
               "777's": len(l777),
               "800's": len(l800),
               "900's": len(l900),
               "911's": len(l911),
               "1000's": len(l1000),
               "2100's": len(l2100)}

sign_counts = pd.Series(data=sign_counts, name="Counts")


print(f"""Signal counts:
      
{sign_counts.to_markdown()}
      
Signals pr. exchange:

{exch_signals.to_markdown()}
      
Trades pr. exchange:

{trd_exch.to_markdown()}
""")
