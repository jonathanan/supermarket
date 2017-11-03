#!/usr/bin/env python3

import supermarket_register
import unittest

class TestSupermarketRegister(unittest.TestCase):
    """
    Test the SupermarketRegister class.
    """
    def _mock_supermarket_instance(self):
        """
        Test helper function for mocking a basic SupermarketRegister instance.
        """
        product_codes = {
                'XXXX-XXXX-XXXX-XXXX': {
                    'product': 'a',
                    'price': 1
                }
        }
        return supermarket_register.SupermarketRegister(product_codes)

    def test_init(self):
        """
        Test initializing an instance of SupermarketRegister.
        """
        # Test simple initialization
        sm = self._mock_supermarket_instance()
        self.assertIs(type(sm),supermarket_register.SupermarketRegister)

        # Test invalid product code initialization
        product_codes = {
                'XXXX-XXXX-XXXX-XXX*': {
                    'product': 'a',
                    'price': 1
                }
        }
        with self.assertRaises(ValueError):
            supermarket_register.SupermarketRegister(product_codes)

        # Test invalid price initialization
        product_codes = {
                'XXXX-XXXX-XXXX-XXXX': {
                    'product': 'a',
                    'price': -1
                }
        }
        with self.assertRaises(ValueError):
            supermarket_register.SupermarketRegister(product_codes)

    def test_total_cost(self):
        """
        Test that an input string of product codes separated by semicolons will
        return the total price of all the products (including local sales tax).
        """
        product_codes = {
                'XXXX-XXXX-XXXX-XXXX': {
                    'product': 'x',
                    'price': 1
                },
                'YYYY-YYYY-YYYY-YYYY': {
                    'product': 'y',
                    'price': 1.12
                },
                'ZZZZ-ZZZZ-ZZZZ-ZZZZ': {
                    'product': 'z',
                    'price': 2.345
                },
                'AAAA-AAAA-AAAA-AAAA': {
                    'product': 'a',
                    'price': '1'
                }
        }
        sm = supermarket_register.SupermarketRegister(product_codes)
        # Test single item
        self.assertEqual(
                sm.total_cost('xxxx-xxxx-xxxx-xxxx'),
                round(1+(1*sm.local_sales_tax),2)
                )

        # Test different spacing in input string
        self.assertEqual(
                sm.total_cost('xxxx-xxxx-xxxx-xxxx;YYYY-YYYY-YYYY-YYYY'),
                round((1+1.12)+((1+1.12)*sm.local_sales_tax),2)
                )
        self.assertEqual(
                sm.total_cost('xxxx-xxxx-xxxx-xxxx; YYYY-YYYY-YYYY-YYYY'),
                round((1+1.12)+((1+1.12)*sm.local_sales_tax),2)
                )
        self.assertEqual(
                sm.total_cost('xxxx-xxxx-xxxx-xxxx;    YYYY-YYYY-YYYY-YYYY'),
                round((1+1.12)+((1+1.12)*sm.local_sales_tax),2)
                )

        # Test price greater than two decimal places
        self.assertEqual(
                sm.total_cost('zZzZ-zZzZ-zZzZ-zZzZ'),
                round(2.345+ (2.345*sm.local_sales_tax),2)
                )

        # Test price equals string integer
        self.assertEqual(
                sm.total_cost('aaaa-aaaa-aaaa-aaaa'),
                round(int(1)+(int(1)*sm.local_sales_tax),2)
                )

    def test__validate_product_price(self):
        """
        Test that the SupermarketRegister helper function will raise an error
        if product price is less than or equal to 0. Otherwise, it returns None.
        """
        sm = self._mock_supermarket_instance()
        # Test vaild price int
        self.assertIsNone(sm._validate_product_price(1))

       # Test vaild price float
        self.assertIsNone(sm._validate_product_price(1.1))

        # Test invalid price 0
        with self.assertRaises(ValueError):
            sm._validate_product_price(0)

        # Test invalid price < 0
        with self.assertRaises(ValueError):
            sm._validate_product_price(-1)

    def test__validate_product_codes_pattern(self):
        """
        Test that the SupermarketRegister helper function will raise an error
        if product code pattern does match the following specifications:
        - sixteen characters long, with dashes separating each four-character
          group
        - is alphanumeric
        - case insensitive
        Otherwise, it returns None
        """
        sm = self._mock_supermarket_instance()
        # Test valid product code pattern lowercase
        self.assertIsNone(
                sm._validate_product_code_pattern('abcd-1234-abcd-1234')
                )

        # Test valid product code pattern uppercase
        self.assertIsNone(
                sm._validate_product_code_pattern('ABCD-1234-ABCD-1234')
                )

        # Test valid product code pattern mixcase
        self.assertIsNone(
                sm._validate_product_code_pattern('A123-b123-C123-d123')
                )

        # Test invalid lowercase 3 character group
        with self.assertRaises(ValueError):
            sm._validate_product_code_pattern('aaaa-bbbb-cccc-123')

        # Test invalid uppercase 3 character group
        with self.assertRaises(ValueError):
            sm._validate_product_code_pattern('AAAA-BBBB-CCCC-123')

        # Test invalid lowercase 5 character group
        with self.assertRaises(ValueError):
            sm._validate_product_code_pattern('aaaa-bbbb-cccc-12345')

        # Test invalid uppercase 5 character group
        with self.assertRaises(ValueError):
            sm._validate_product_code_pattern('AAAA-BBBB-CCCC-12345')

        # Test invalid character
        with self.assertRaises(ValueError):
            sm._validate_product_code_pattern('AAA*-BBBB-CCCC-1234')

if __name__ == '__main__':
    unittest.main()
