import csv

with open('cdr.csv', newline='') as csvfile:  #Read csv file
    spamreader = csv.reader(csvfile, delimiter=',')
    spam = list(spamreader)
    spam.remove(spam[0])
    closes = list(map(lambda x: float(x[4]), spam)) #'Close' column from csv
    high = list(map(lambda x: float(x[2]), spam)) #'High prices' column from csv
    low = list(map(lambda x: float(x[3]), spam)) #'Low prices' column from csv

def moving_avg(prices, window_size): #Moving average for close prices
    avg = []
    for x in range(0, len(prices) - window_size+1):
        new_prices = prices[x:window_size+x]
        number = round(sum(new_prices) / window_size, 2)
        avg.append(number)
    return avg

def moving_min(prices, window_size): #Moving minimum for close prices
    avg = []
    for x in range(0, len(prices) - window_size+1):
        new_prices = prices[x:window_size+x]
        number = min(new_prices)
        avg.append(number)
    return avg

def calculate_support(prices, window_size, ratio = 0.1): #Calculating support for prices
    minimum_avg = moving_min(prices, window_size)
    high_low_list = [highs - lows for highs, lows in zip(high,low)]
    supp_avg = [round(values - (diff * ratio), 2) for values, diff in zip(minimum_avg, high_low_list)]

    return supp_avg