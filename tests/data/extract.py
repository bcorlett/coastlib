import os
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import coastlib

path = os.path.join(os.getcwd(), 'tests', 'data')
df = pd.read_csv(os.path.join(path, 'Ws_Dir.txt'), sep=',', index_col=None)
# index = [datetime.datetime(year=int(_d[:4]), month=int(_d[4:6]), day=int(_d[6:8]),
#                            hour=int(_h[:2]), minute=int(_h[2:4]))
#          for _d in df['Date     '] for _h in df['HrMn ']]
data = df[['I .1','QCP  ']]
data.columns = ['Spd', 'Dir']
data = data[data['Spd'] < 999]
data = data[data['Dir'] <= 360]
data = data[data['Dir'] >= 0]

bins = [np.percentile(data['Spd'], _p) for _p in np.arange(0, 100, 10)]
coastlib.rose_plot(values=data['Spd'].values, directions=data['Dir'].values,
                   direction_bins=16, calm_region=0,
                   colormap=plt.get_cmap('jet'))

