import csv

with open('cdr.csv', newline='') as csvfile:  #Read csv file
    spamreader = csv.reader(csvfile, delimiter=',')
    closes = [x[4] for x in spamreader] #'Close' column from csv
    closes.remove(closes[0])

123
def moving_avg(prices, window_size): #Moving average for close prices
    avg = []
    for x in range(0, len(closes) - window_size+1):
        new_prices = prices[x:window_size+x]
        new_prices = [float(y) for y in new_prices] #Changing str to flaot
        number = round(sum(new_prices) / window_size, 2)
        avg.append(number)
    return avg

def moving_min(prices, window_size): #Moving minimum for close prices
    avg = []
    for x in range(0, len(closes) - window_size+1):
        new_prices = prices[x:window_size+x]
        new_prices = [float(y) for y in new_prices] #Changing str to flaot
        number = min(new_prices)
        avg.append(number)
    return avg


