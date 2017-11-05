#!/usr/bin/env python3

import supermarket_register
import json
import os

def print_menu():
    print('1. List products')
    print('2. Add a product')
    print('3. Remove a product')
    print('4. Calculate total of products')
    print('5. Save and exit')

if __name__ == '__main__':
    # Read config and create Supermarket Register
    product_file = open('config/products.json', 'r').read()
    product_data = json.loads(product_file)
    register = supermarket_register.SupermarketRegister(product_data)

    while True:
        print_menu()
        print('Select option:')
        option = int(input())

        try:
            if(option == 1):
                register.list_products()
            elif(option == 2):
                print('Enter product code:')
                code = str(input())
                print('Enter product name:')
                name = str(input())
                print('Enter product price:')
                price = str(input())
                product = { code: { 'product': name, 'price': price } }
                register.add_product(product)
            elif(option == 3):
                print('Enter product code:')
                code = str(input())
                register.remove_product(code)
            elif(option == 4):
                print('Enter product codes (separated by semicolons):')
                os.environ['SKUS'] = str(input())
                print('$', register.total_cost(os.environ['SKUS']))
            elif(option == 5):
                with open('config/products.json', 'w') as config:
                    json.dump(register.product_codes, config)
                break
            else:
                print('Invalid option')
        except KeyError:
            print('Invalid input')
        except ValueError:
            print('Invalid input')
        print()
