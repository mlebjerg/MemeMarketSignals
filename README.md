# Market Maker Signals

## Description

This is still early stages, feel free to play around with it. Pull-requests will be looked at.
I made "MM-signals.py" in two days, and "MM-graph.py" in 3 hours, i know it is messy.

https://www.reddit.com/r/Superstonk/comments/u7iox3/it_is_time_to_talk_about_market_maker_signals_i/

Well it is speculated that market makers use these signals to coordinate and manipulate the market.

If you want to learn what the signals mean here is a link: https://otc.financial/list-of-market-maker-signals/
|Volume|Describtion|
|---|---|
|100|I need Shares|
|200|I need Shares badly but do not take the stock down|
|300|Take (or I am taking) the stock down at least 30% so I can load shares|
|400|Keep trading it sideways|
|500|Gap the stock. Gap can be up or down, depending on direction of 500 signal|
|505|I am short on shares|
|600|Apply resistance at the ASK to keep the price from increasing|
|700|Move the price up|
|777|Also recognized as a signal to move the price up|
|800|Prepare for an increase in trading volume|
|900|Allow the stock to float and trade freely|
|911|Pending News/Press Release On The Way|
|1000|Don't let it run|
|2100|Let it run|

This is made in Python, it takes level 2 data from webull and counts every known one. Trades are also translated.

## Getting Started

### Dependencies

Python 3

A Webull account with L2 data

Run this command in the project folder to get the dependencies:

```
pip install -r requirements.txt
```

### Executing program

- Copy the "example.conf" file
- Rename it to ".conf"
- Replace the text with what it says.
- Run the script "MM-signals.py" to capture the trades and data

When you want the graph run "MM-graphg.py", remember to put in the ticker symbol.

## Known problems

- On windows the table flashes
- Timeouts when no data comes in for a while
- Need to make the graph do select the day(s) you want it to display.

## Version History

- 0.1
  - Initial "Release"

## License

This project is licensed under the GNU AFFERO GENERAL PUBLIC LICENSE Version 3 - see the LICENSE.md file for details
