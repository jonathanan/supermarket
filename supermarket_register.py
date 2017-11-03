#!/usr/bin/env python3

import re

class SupermarketRegister:
    def __init__(self, product_codes, local_sales_tax=0.0875):
        for code, info in product_codes.items():
            product_codes[code.upper()] = product_codes.pop(code)
            self._validate_product_code_pattern(code)
            self._validate_product_price(info['price'])
        self.product_codes = product_codes
        self.local_sales_tax = local_sales_tax

    def list_products(self):
        for code, info in self.product_codes.items():
            print(code, info)

    def total_cost(self, products):
        codes = ''.join(products.split()).split(';')
        total_cost = 0
        for code in codes:
            code = code.upper()
            try:
                self._validate_product_code_pattern(code)
                self._validate_product_price(self.product_codes[code]['price'])
                total_cost += float(self.product_codes[code]['price'])
            except KeyError as e:
                print('Invalid product code: {0}'.format(code))
                print('Valid product codes are:')
                self.list_products()
                raise
        return round(total_cost + (total_cost * self.local_sales_tax), 2)

    def _validate_product_price(self, price):
        if float(price) <= 0:
            raise ValueError('Invalid price: {0}'.format(price))

    def _validate_product_code_pattern(self, code):
        pattern = re.compile(
                '^[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}$'
                )
        if not pattern.match(code):
            raise ValueError('Invalid product code pattern: {0}'.format(code))

