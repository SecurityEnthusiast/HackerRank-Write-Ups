#!/bin/python

import sys
from collections import OrderedDict

number_of_items = raw_input()
list_of_products = []

if __name__ == "__main__":
    for item in range(int(number_of_items)):
            item = raw_input()
            list_of_products.append(item)

    splitted_products = OrderedDict()
    for product in list_of_products:
        item_name = " ".join(product.strip().split(" ")[0:-1])
        price = int(product.strip().split(" ")[-1])
        if (item_name in splitted_products):
            splitted_products[item_name] += price
        else:
            splitted_products[item_name] = price

    for item_name in splitted_products:
        print("{0} {1}".format(item_name,str(splitted_products[item_name])))