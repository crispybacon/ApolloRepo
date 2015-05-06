#!/usr/bin/python
import numpy as np
from matplotlib.pyplot import plot, show
import matplotlib.pyplot as plt
x=range(1,100000)
y=[]
z=[]
for unit in x:
    cash = np.zeros(10000)
    cash[0] = 1000
    outcome = np.random.binomial(9, 0.5, size=len(cash))

    for i in range(1, len(cash)):

       if outcome[i] < 5:
          cash[i] = cash[i - 1] - 1
       elif outcome[i] < 10:
          cash[i] = cash[i - 1] + 1
       else:
          raise AssertionError("Unexpected outcome " + outcome)


    y.append(unit)
    z.append(cash[-1:])
plt.ylabel('Ending Value')             
plt.xlabel('Iteration')
plt.plot(y,z)
show()
