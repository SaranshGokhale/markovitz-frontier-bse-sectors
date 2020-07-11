import pandas as pd
import numpy as np
import matplotlib

bse = pd.read_csv("C:/Users/Saransh Gokhale/Anaconda/weeklysectoraldata.csv",index_col=0,parse_dates=True)
bse.head()