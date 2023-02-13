#Daniyal Khan HW1

import numpy as n
import matplotlib.pyplot as pl
#question 3
mean = [0, 0.6]
covar = [[0.3, -1], [-1, 5]] 
x, y =n.random.multivariate_normal(mean, covar, 1000).T

pl.plot(x, y, 'x')
pl.axis('Equal')
pl.show()

#question4
mean = 209
simulated_counts = n.random.poisson(mean, 1000)

pl.hist(simulated_counts, bins=21, edgecolor='black')
pl.xlabel('Amount of Bikers')
pl.ylabel('Occurency')
pl.title('Cyclists crossing the Brooklyn Bridge per Day')
pl.show()
