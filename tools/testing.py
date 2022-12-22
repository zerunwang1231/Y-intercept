from tools import utils
import matplotlib.pyplot as plt
import numpy as np
import datetime


def execution_pl(price, volume, date, transaction_size, window):
    position_log = []
    pl_log = []
    date_log = []
    vo = utils.vo(volume, 5, window)
    bolu, bold = utils.bb(price, window)
    indicator = utils.signal(vo, bolu, bold, price, window)
    price = price[window - 1 :]
    date = date[window - 1 :]
    last_position = 0  # cumulative position of each day
    last_pl = 0  # cumulative profit and loss of each day
    for i, act in enumerate(indicator):
        date_log.append(date[i])
        if act == 1:
            last_position += transaction_size
            last_pl -= transaction_size * price[i]
        elif act == -1:
            last_position -= transaction_size
            last_pl += transaction_size * price[i]
        position_log.append(last_position)
        pl_log.append(last_pl)
    pl = (
        pl_log[-1] + position_log[-1] * price[-1]
    )  # clean up all remaining positions to derive final PL
    return {
        "date": date_log,
        "position record": position_log,
        "P&L record": pl_log,
        "Final PL": pl,
        "action": indicator,
    }


def get_plot(date, price, volume, action, window):
    plt.rc("figure", figsize=(15, 10))
    fig, axes = plt.subplots(2, gridspec_kw={"height_ratios": [3, 1]})
    fig.tight_layout(pad=3)

    to_numpy_with_window = lambda arr: np.array(arr[window - 1 :])
    price, date, volume = (
        to_numpy_with_window(price),
        to_numpy_with_window(date),
        to_numpy_with_window(volume),
    )
    action = np.array(action)
    date = np.array([datetime.datetime(*[int(s) for s in elem.split("-")]) for elem in date])

    plot_price = axes[0]
    plot_price.plot(date, price, color="black", linewidth=1, label="Price")

    buy_at_idx, sell_at_idx = np.where(action == 1), np.where(action == -1)
    plot_price.scatter(date[buy_at_idx], price[buy_at_idx], marker="x", color="green", label="buy")
    plot_price.scatter(date[sell_at_idx], price[sell_at_idx], marker="x", color="red", label="sell")
    plot_price.legend()

    plot_vol = axes[1]
    plot_vol.bar(date, volume, width=2, color="darkgrey")
    plt.show()
