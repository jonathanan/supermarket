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
        if not self.product_codes:
            print('Empty, no product codes')
        else:
            for code, info in self.product_codes.items():
                print(code, info)

    def add_product(self, product):
        for code, info in product.items():
            self._validate_product_code_pattern(code)
            self._validate_product_price(product[code]['price'])
            if not code in self.product_codes:
                self.product_codes[code.upper()] = info
            else:
                raise KeyError('Product already exists: {0}'.format(code))

    def remove_product(self, code):
            code = code.upper()
            self._validate_product_code_pattern(code)
            if code in self.product_codes:
                self.product_codes.pop(code, None)
            else:
                raise KeyError('Product does not exists: {0}'.format(code))

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

