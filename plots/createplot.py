import sys
import csv
from datetime import datetime

import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns


fin = open('delft.csv')
reader = csv.reader(fin)
x_data = []
y_data = []
next(reader) #-- skip the header

for row in reader:
    x_data.append(datetime.strptime(row[0], "%I:%M %p"))
    y_data.append(row[1])

plt.title('Temperature throughout the day')
plt.plot(x_data, y_data)
plt.gcf().autofmt_xdate()
plt.xlabel('time')
plt.ylabel('temperature (in Celcius)')
plt.savefig('myplot.pdf')
