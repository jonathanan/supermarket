#!/usr/bin/env python3

import supermarket_register
import json
import os

if __name__ == '__main__':
    product_file = open('products.json').read()
    product_data = json.loads(product_file)

    register = supermarket_register.SupermarketRegister(product_data)
    print('$', register.total_cost(os.environ['SKUs']))
