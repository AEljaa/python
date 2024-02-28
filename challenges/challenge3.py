class SalesItem:
  def __init__(self, branch, totalSales, date):
    self.branch = branch
    self.totalSales = totalSales
    self.date = date

# <summary >
# It has been a busy year at mountain warehouse, having made lots of sales.
# Management would like to know which branch made the most in revenue.
# For this challenge you will be given an array of sales broken down by Branch and Date.
# You will need to sum all branch across multiple days and identify which branch had the highest sales overall
# Assume that there is only one branch with the highest total
# We have provided some starting code but if you know of a better method then go ahead with that
# </summary >
# <param name = "sales" > The array of sales items < /param >
# <returns > The branch with the best performing sales < /returns >

import sys

def CalculateBestBranch(sales):
  branchSales={}
  for i in range(0,len(sales)):
    currbranch=sales[i]
    branchSales[currbranch.branch]=sales[i].totalSales + branchSales.get(currbranch.branch,0)
  
  #Now get the branch with highest val
  bestpref=["",-sys.maxsize]
  for key,amount in branchSales.items():
    if(bestpref[1]<amount):
        bestpref=[key,amount]
  return bestpref[0]

  # branchSales = {}

  # Implement your code here
  # raise NotImplementedError

  # order your dictionary by value
  # get key of first item

  # return "FOO"
