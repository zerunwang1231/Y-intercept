from tools import utils
import csv

if __name__ == "__main__":
    with open("data/data.csv") as file:
        record = list(csv.reader(file, delimiter=","))


