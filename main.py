from tools import testing
import csv
import numpy as np
from tools import testing


def main():
    with open("data/data.csv") as file:
        record = list(csv.reader(file, delimiter=","))
        record = record[1:]
    record = np.array(record)
    stocks = list(np.unique(record[:, 0]))
    window = 20
    pl = {}
    for s in stocks:
        sub_data = record[
            (record[:, 0]) == s,
        ]
        transaction_size = 10
        date = sub_data[:, 1]
        price = list(map(float, sub_data[:, 2]))
        volume = list(map(int, sub_data[:, 3]))
        output = testing.execution_pl(price, volume, date, transaction_size, window)
        pl[s] = output["Final PL"]
        # a demonstration of our signal and log
        if s == "1332 JT":
            log = np.stack(
                (
                    np.array(output["date"]),
                    np.array(output["position record"]),
                    np.array(output["P&L record"]),
                ),
                axis=1,
            )
            np.savetxt("log_book32JT.csv", log,fmt="%s", delimiter=",", header="date, position, P and L")

            # plot the time series plot for prices to indicate our transaction
            action = output["action"]  # entry and exit signals for stock 1332 JT
            testing.get_plot(date, price, volume, action, window)
    with open("P_and_L.txt", "a", newline="", encoding="utf-8") as f:
        for key in pl.keys():
            f.write("%s,%s\n" % (key, pl[key]))


if __name__ == "__main__":
    main()
