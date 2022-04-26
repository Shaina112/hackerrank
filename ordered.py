from collections import OrderedDict


if __name__ == '__main__':
    d = OrderedDict()
    n = int(input())

    for i in range(n):
        item, price = input().rsplit(' ', 1)

        if item not in d:
            d[item] = int(price)
        else:
            d[item] += int(price)
    for item, price in d.items():
        print(item, price)

