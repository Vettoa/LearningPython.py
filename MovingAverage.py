import csv

with open('E:\Python\cdr.csv', newline='') as csvfile:  #Read csv file
    spamreader = csv.reader(csvfile, delimiter=',')
    spam = list(spamreader)
    spam.remove(spam[0])
    closes = list(map(lambda x: float(x[4]), spam)) #'Close' column from csv
    data_high_low = list(map(lambda x: (x[0], float(x[2]), float(x[3])), spam)) #'Data' with higher prices and lower prices
    data_open_close = list(map(lambda x: (x[0], float(x[1]), float(x[4])), spam)) #'Data' with higher prices and lower prices

class SakataChart:

    def __init__(self, prices, window_size):
        self.prices = prices
        self.window_size = window_size

    def moving_avg(self): #Moving average for close prices
        avg = []
        for x in range(0, len(self.prices) - self.window_size+1):
            new_prices = self.prices[x:self.window_size+x]
            number = round(sum(new_prices) / self.window_size, 2)
            avg.append(number)
        return avg

    def moving_min(self): #Moving minimum for close prices
        avg = []
        for x in range(0, len(self.prices) - self.window_size+1):
            new_prices = self.prices[x:self.window_size+x]
            number = min(new_prices)
            avg.append(number)
        return avg

    def single_candle_height(self, data): #Single candle height
        '''
        Data with higher and lowest prices
        '''
        return [round(highs - lows,2) for data, highs, lows in data]

    def calculate_support(self, data, ratio = 0.1): #Calculating support for prices
        '''
        Data with higher and lowest prices
        '''
        minimum_avg = self.moving_min()
        high_low_list = [round(highs - lows,2) for data, highs, lows in data]
        supp_avg = [round(values - (diff * ratio), 2) for values, diff in zip(minimum_avg, high_low_list)]

        return supp_avg

    def find_doji(self, data): #Finding doji
        '''
        Data with open and close prices
        '''
        doji = list(map(lambda x: abs(x[1]- x[2]), data))
        data_list = list(zip(doji, data))
        return '{}'.format(min(data_list)[1][0])
