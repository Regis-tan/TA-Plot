#This is code to plot the number of stabbing crimes in london from the time period 2015-2022.
#I am using a line graph as I want to see the effect of year on the number of stabbings.
#In 2020, there was a sharp drop in stabbing crimes in london due to the covid restrictions.
#Data gotten from: https://www.statista.com/statistics/864736/knife-crime-in-london/

import matplotlib.pyplot as plt

#data
x = [2015,2016,2017,2018,2019,2020,2021,2022]
y = [9752,12077,14731,14902,15928,10150,11122,12786]

#labels
plt.xlabel("Year")
plt.ylabel("Stabbings")
plt.title("Stabbings in London 2015-2022")

plt.grid(True)
plt.plot(x,y)
plt.show()
