import pandas as pd
import glob
import os
import re
from datetime import datetime

path = r'../TradeCSVs/'  # use your path
all_files = glob.glob(os.path.join(path, "*.csv"))

pre_li = []
post_li = []

for filename in all_files:
    x = re.search("\d.......", filename)
    file_date = datetime.strptime(x[0], "%Y%m%d") 
    split_date = datetime.strptime("20220721", "%Y%m%d")
    #print(file_date)
    df = pd.read_csv(filename, delimiter="|", names=[
        "datetime", "tickType", "time", "price", "volume", "tickAttribLast", "exchange", "specialConditions"])
    if file_date <= split_date:
        pre_li.append(df)
    else:
        post_li.append(df)
        
pre_df = pd.concat(pre_li, axis=0, ignore_index=True)
post_df = pd.concat(post_li, axis=0, ignore_index=True)
pre_df["cost"] = pre_df.price * pre_df.volume
post_df["cost"] = post_df.price * post_df.volume

with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(post_df.sort_values(by="volume", ascending=False, ignore_index=True))
