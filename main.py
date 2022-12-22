from tools import testing
import csv
import numpy as np

from tools import testing

if __name__ == "__main__":
    with open("data/data.csv") as file:
        record = list(csv.reader(file, delimiter=","))
        record = record[1:]
    record = np.array(record)
    stocks = list(set(record[:,0]))
  #  print(stocks)
    PL = {}
    for s in stocks:
        sub_data = record[(record[:,0])==s,]
        transaction_size = 10
        date = sub_data[:,1]
        price = list(map(float, sub_data[:,2]))
        volume = list(map(float, sub_data[:,3]))
        output = testing.excution_PL(price, volume, date, transaction_size)
        PL[s] = output["Final PL"]
    print(PL)