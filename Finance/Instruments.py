import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#Default Instrument Template
fig= plt.figure(figsize=(6, 6), facecolor='white',)
ax = plt.subplot(111, frameon=False)
# Add a subplot with no frame
y = list(np.zeros(100))
x = list(range(len(y)))
ax.text(0.5, 1.0, "{}".format('Instrument'), transform=ax.transAxes,
        ha="center", va="bottom", color="gray",
        family="geneva", fontweight="light", fontsize=16)
ax.set_ylim(0,100)
ax.set_xlim(0,100)
def update(*args):
    y[1:] = y[0:-1]
    y[0] = np.random.randint(0,100)
    test_line.set_ydata(y)
    #print(y[0])
    return line
test_line, = ax.plot(x,y, color="red")
anim = animation.FuncAnimation(fig, update, interval=50)
plt.grid(True)
plt.axhline(90, color='blue')
plt.show()
#Streamline Instrument (Oscilliscope)
def update(idx,*args):
    idx+=1
    if idx >= len(ydata)-1:
        plt.pause(-1)
    yset = ydata[0:idx+2]
    x.append(x[-1]+1)
    test_line.set_data(x,yset)
    return test_line
query = {'Country Name': 'United States'}
record = collection.find(query)
data = record.next()
yrange = range(1800,2017)
ydata = [data[str(i)] for i in yrange]
#ydata = range(0, len(range(1800,2017)))
ydata = np.array(ydata)
ydata = np.nan_to_num(ydata)
x = [list(yrange)[0]]
y = ydata[:1]
fig = plt.figure(figsize=(6, 6), facecolor='white',)
ax = plt.subplot(111, frameon=False)
ax.text(0.5, 1.0, '{} World Debt'.format(query['Country Name']),
        transform=ax.transAxes,ha="center", 
        va="bottom", color="gray", 
        fontweight="heavy", fontsize=16)
ax.set_ylim(0,ydata.max())
ax.set_xlim(yrange[0],yrange[-1])
idx = 1
test_line, = ax.plot(x,y, color="crimson")
anim = animation.FuncAnimation(fig, update, interval=1)
plt.grid(True)
plt.axhline(ydata.max()*.75, color='blue')
plt.show()
#Multiple Country
