from tools import utils
def excution_PL(price, volume, date, transaction_size):
    window = 20
    position_log = []
    PL_log = []
    date_log = []
    vo = utils.vo(volume, 5, window)
    bolu, bold = utils.bb(price, window)
    indicator = utils.signal(vo, bolu, bold, price, window)
    price = price[window - 1:]
    date = date[window - 1:]
    last_position = 0
    last_PL = 0
    for i, act in enumerate(indicator):
        date_log.append(date[i])
        if act == 1:
            last_position += transaction_size
            last_PL -= transaction_size*price[i]
        elif act == -1:
            last_position -= transaction_size
            last_PL += transaction_size*price[i]
        position_log.append(last_position)
        PL_log.append(last_PL)
    PL = PL_log[-1]+position_log[-1]*price[-1]
    return {"date" : date_log, "position record" : position_log, "P&L record": PL_log, "Final PL" : PL}
