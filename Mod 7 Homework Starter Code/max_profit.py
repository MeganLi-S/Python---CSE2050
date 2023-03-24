def price_to_profit(L): 
    list_dif = []
    for i in range(len(L)):
        if i == 0:
            list_dif.append(0)
        else:
            list_dif.append(L[i] - L[i-1])
    return list_dif


# brute force solution, for reference
def max_profit_brute(L):
    n = len(L)
    max_sum = 0

    # outer loop finds the max profit for each buy day
    for i in range(n):
        total = 0

        # inner loop finds the profit for each sell day
        for j in range(i+1, n):
            total += L[j] # total profit if we sell on day j
            if total > max_sum: max_sum = total

    return max_sum


# you can use a helper function or add parameters, your choice
def max_profit(L): # O(nlogn)
# base case? Return today's profit
    if len(L) == 0:
        return 0
# find the max profit in the left-hand sublist
    def helper(L, left, right):
        #print(str(L[left:right+1]))
        if left == right:
            return 0

        median = (left + right) // 2

        maxprofitleft = helper(L, left, median )
        maxprofitright = helper(L, median + 1, right)

        start = left
        mini = start
        maxi = start
        counter = 0
        placeholdmin = start
        maxcount = counter
        mincount = counter

        for i in range(left, right +1):
            start = start + L[i]
            counter += 1
            if start > maxi:
                maxi = start
                maxcount = counter
            if start < mini:
                placeholdmin = start
                mincount = counter
            if mincount <= maxcount:
                mini = placeholdmin
            
            
            
        # print("left: " + str(left))
        # print("maxprofitleft: " + str(maxprofitleft))
        # print("right: " + str(right))
        # print("maxprofitright: " + str(maxprofitright))
        maxprofit = maxi - mini
       # print("1: " + str(maxprofit))
        maxprofit = max(maxprofit, maxprofitright, maxprofitleft)

       # print(maxprofit)

        return maxprofit
    
    maxprofit = helper(L, 0, len(L) -1)
    return maxprofit
def max_profit_crossing(L, left, right, median): 
    
    # O(n)
# Starting from the median, find the best price moving left
# starting from just after the median, find the best price moving right
# return the best profit:
# * left of median (inclusive)
# * right of median (exclusive)
# * buy on the left, sell on the right (does not require a recursive call)
    pass





# some test cases, and an example of reading CSVs
if __name__ == '__main__':
    # some basic tests of the necessary functions

    assert price_to_profit([100, 105, 97, 200, 150]) == [0, 5, -8, 103, -50]
    print(max_profit([0, 5, -8, 103, -50]))
    print(max_profit([0, -1, 3, 4, -5, 9, -2]))
    print(max_profit([0,3,4,-10,103,-200, 400, -4, 16, -500, 15, 14, 1000, -2000, -500, 200]))
    assert max_profit([0, -1, 3, 4, -5, 9, -2]) == 11


    ##### Import and read values from associated csvs, then check if you can become a bitcoin-optimaire
    #import csv
    import os


    val_2015 = []
    val_2016 = []
    val_2017 = []
    val_2018 = []
    val_2019 = []
    val_2020 = []

    vals = [val_2015, val_2016, val_2017, val_2018, val_2019, val_2020]

    for file in os.scandir(r'./bitcoin_prices'):
        if (file.path.endswith(".csv")):
            if file.name == "2015.csv": i = 0
            elif file.name == "2016.csv": i = 1
            elif file.name == "2017.csv": i = 2
            elif file.name == "2018.csv": i = 3
            elif file.name == "2019.csv": i = 4
            elif file.name == "2020.csv": i = 5

            with open(file, 'r') as f:
                reader = csv.reader(f)

                lst = list(reader)[1:]
                for j in range(len(lst)):
                    vals[i].append( float(lst[j][1].replace(",","")))


    # find the profits for each year
    year_profits = []
    for year in vals:
        year_profits.append([])
        year_profits[-1] = price_to_profit(year)
    
    #print(year_profits)
    # correct max profits per year, 2015-2020, rounded to ints
    max_profits = [298, 604, 18561, 4476, 9665, 24052]

    # test that max_profit returns the correct profit for each year
    for i, year in enumerate(year_profits):
        assert round(max_profit(year), 0) == max_profits[i]