import os
import csv
import statistics
from data_types import Purchase


def main():
    print_header()
    filename = get_data_file()
    data = load_data(filename)
    query_data(data)


def print_header():
    print('-----------------------------')
    print('  REAL ESTATE ANALYSIS APP')
    print('-----------------------------')
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv')


def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)

    return purchases


def query_data(data):
    data.sort(key=lambda p: p.price)

    highest = data[-1]
    lowest = data[0]
    print('The most expensive house is: ${:,}, with {} beds and {} baths'.format(highest.price, highest.beds, highest.baths))
    print('The least expensive house is: ${:,} with {} beds and {} baths'.format(lowest.price, lowest.beds, lowest.baths))

    prices = [
        p.price
        for p in data
    ]
    average_price = statistics.mean(prices)
    print('The average price of a house is: ${:,}'.format(int(average_price)))

    two_bed = [
        p  # projection or items
        for p in data  # the set to process
        if p.beds == 2  # test / condition
    ]
    average_price = statistics.mean([p.price for p in two_bed])
    average_baths = statistics.mean([p.baths for p in two_bed])
    average_size = statistics.mean([p.sq__ft for p in two_bed])
    print('The average 2-bed house is: ${:,}, baths = {:,} and sq ft = {:,}'
          .format(int(average_price), round(average_baths, 1), round(average_size, 1)))


if __name__ == '__main__':
    main()
