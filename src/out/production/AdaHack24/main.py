import matplotlib.pyplot as plt
import pandas as pd
import csv
import numpy as np

global budget
global moneyPerDay
global moneyMin
global moneyMax
global compound
global years


with open('C:\Users\GlenF\IdeaProjects\AdaHack24\Lib\output.csv', newline='') as file:
    csvreader = csv.reader(file)
    i = 0
    rows = list(csvreader)
    moneyPerDay = float((rows[0])[0])
    moneyMin = float((rows[1])[0])
    moneyMax = float((rows[2])[0])
    moneyPerDay = moneyMax - moneyPerDay



#budget = 100
#moneyPerDay = 24.50

investmentAnnum = 1.1385
investmentMonthly = 1.010868
instantAnnum = 1.0273
instantMonthly =1.000852

#moneyLeftOver = budget - moneyPerDay

def calculateCompoundPerAnnum(years,money,rate):
    compoundVariables = pd.DataFrame(columns=['Year','Money'])
    for i in range(0,years+1):
        moneyTotal = ((money * 365) * (rate ** (i)))
        compoundVariables.loc[i] = ([i,moneyTotal])
    return compoundVariables

def calculateCompoundPerMonth(money,rate):
    compoundVariables = pd.DataFrame(columns=['Year','Money'])
    for i in range(0,13):
        moneyTotal = ((money * 30.4375) * (rate ** (i)))
        compoundVariables.loc[i] = ([i,moneyTotal])
    return compoundVariables

def compoundYearly(money,year,rate):
    moneyTotal = ((money * 365) * (rate ** (i)))
    return moneyTotal




userInvestAnnumTen = calculateCompoundPerAnnum(10,moneyPerDay,investmentAnnum)
userInvestAnnumThirty = calculateCompoundPerAnnum(30,moneyPerDay,investmentAnnum)

#userInvestAnnumTen = calculateCompoundPerAnnum(10,(moneyMax - moneyPerDay),investmentAnnum)
#userInvestAnnumThirty = calculateCompoundPerAnnum(30,(moneyMax - moneyPerDay),investmentAnnum)

userInstantAnnumThirty = calculateCompoundPerAnnum(30,moneyPerDay,instantAnnum)
userInstantAnnumTen = calculateCompoundPerAnnum(10,moneyPerDay,instantAnnum)

userInstantMonthly = calculateCompoundPerMonth(moneyPerDay,instantMonthly)
userInvestmentMonthly = calculateCompoundPerMonth(moneyPerDay,investmentMonthly)




minInvestAnnumTen = calculateCompoundPerAnnum(10,moneyMin,investmentAnnum)
minInvestAnnumThirty = calculateCompoundPerAnnum(30,moneyMin,investmentAnnum)

minInstantAnnumThirty = calculateCompoundPerAnnum(30,moneyMin,instantAnnum)
minInstantAnnumTen = calculateCompoundPerAnnum(10,moneyMin,instantAnnum)

minInstantMonthly = calculateCompoundPerMonth(moneyMin,instantMonthly)
minInvestmentMonthly = calculateCompoundPerMonth(moneyMin,investmentMonthly)



maxInvestAnnumTen = calculateCompoundPerAnnum(10,moneyMax,investmentAnnum)
maxInvestAnnumThirty = calculateCompoundPerAnnum(30,moneyMax,investmentAnnum)

maxInstantAnnumThirty = calculateCompoundPerAnnum(30,moneyMax,instantAnnum)
maxInstantAnnumTen = calculateCompoundPerAnnum(10,moneyMax,instantAnnum)

maxInstantMonthly = calculateCompoundPerMonth(moneyMax,instantMonthly)
maxInvestmentMonthly = calculateCompoundPerMonth(moneyMax,investmentMonthly)


print("Hello")
plt.plot(userInvestmentMonthly["Year"], userInvestmentMonthly["Money"])
plt.plot(userInstantMonthly["Year"], userInstantMonthly["Money"],linestyle='dashed')

plt.plot(minInvestmentMonthly["Year"], minInvestmentMonthly["Money"])
plt.plot(minInstantMonthly["Year"], minInstantMonthly["Money"],linestyle='dashed')

plt.plot(maxInvestmentMonthly["Year"], maxInvestmentMonthly["Money"])
plt.plot(maxInstantMonthly["Year"], maxInstantMonthly["Money"],linestyle='dashed')

plt.legend(['Your Investment', 'Your Savings Account', 'Minimum Investment', 'Minimum Savings Account', 'Maximum Investment', 'Maximum Savings Account'])
plt.title('Investment vs Savings', fontname="Arial", fontweight="bold")
plt.xlabel('Month', fontname="Arial", fontweight="bold")
plt.ylabel('Money (in £)', fontname="Arial", fontweight="bold")
plt.xticks(np.arange(0, 13, step=1))
plt.xlim(0,12)
plt.savefig("oneyear.jpg")
plt.clf()

plt.plot(userInvestAnnumTen["Year"], userInvestAnnumTen["Money"])
plt.plot(userInstantAnnumTen["Year"], userInstantAnnumTen["Money"],linestyle='dashed')

plt.plot(minInvestAnnumTen["Year"], minInvestAnnumTen["Money"])
plt.plot(minInstantAnnumTen["Year"], minInstantAnnumTen["Money"],linestyle='dashed')

plt.plot(maxInvestAnnumTen["Year"], maxInvestAnnumTen["Money"])
plt.plot(maxInstantAnnumTen["Year"], maxInstantAnnumTen["Money"],linestyle='dashed')


plt.legend(['Your Investment', 'Your Savings Account', 'Minimum Investment', 'Minimum Savings Account', 'Maximum Investment', 'Maximum Savings Account'])
plt.title('Investment vs Savings', fontname="Arial", fontweight="bold")
plt.xlabel('Number of years', fontname="Arial", fontweight="bold")
plt.ylabel('Money (in £)', fontname="Arial", fontweight="bold")
plt.xlim(0,10)
maxval = compoundYearly(moneyPerDay,10,investmentAnnum)

plt.savefig("tenyears.jpg")
plt.clf()

plt.plot(userInvestAnnumThirty["Year"], userInvestAnnumThirty["Money"])
plt.plot(userInstantAnnumThirty["Year"], userInstantAnnumThirty["Money"], linestyle = 'dashed')

plt.plot(minInvestAnnumThirty["Year"], minInvestAnnumThirty["Money"])
plt.plot(minInstantAnnumThirty["Year"], minInstantAnnumThirty["Money"],linestyle='dashed')

plt.plot(maxInvestAnnumThirty["Year"], maxInvestAnnumThirty["Money"])
plt.plot(maxInstantAnnumThirty["Year"], maxInstantAnnumThirty["Money"],linestyle='dashed')


plt.legend(['Your Investment', 'Your Savings Account', 'Minimum Investment', 'Minimum Savings Account', 'Maximum Investment', 'Maximum Savings Account'])
plt.title('Investment vs Savings', fontname="Arial", fontweight="bold")
plt.xlabel('Number of years', fontname="Arial", fontweight="bold")
plt.ylabel('Money (in £)', fontname="Arial", fontweight="bold")
plt.xlim(0,30)
plt.savefig("thirtyyears.jpg")
plt.clf()