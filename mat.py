import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]
plt.pie(y,labels=mylabels,startangle=90,explode=myexplode,shadow=True)
plt.legend(title="fruite")

plt.show()