# supermarket
A Supermarket Register CLI application which can take a set of product codes, look up
the price of each product, and compute the total amount of the sale (including
local sales tax).

Features:
- Initial products supported can be modified in `config/products.json`.
- List products
- Add a product
- Remove a product
- Calculate total amount of sale of selected products (including local sales tax)
- Save register products.

## Requirements
Docker (Tested with Docker version 17.05.0-ce, build 89658be)

## Building/Testing
To run unit tests and build the application:
```
# Using Makefile
make build

# Using docker explicitly
docker build -t supermarket .
```

## Running
(Optional) Set environment variable `SKUS` to a string of products codes separated by
semicolons. This will be used to calculate total amount of sale.

e.g.
```
export SKUS="E5T6-9UI3-TH15-QR88; YRT6-72AS-K736-L4AR"
```

To run the application:
```
# Using Makefile
make run

# Using docker explicitly
docker run --rm -e SKUS=$SKUS supermarket
````

To start an exited application and continue from it's last saved state:
```
docker start -i <CONTAINER_ID>
```

An example of the Supermarket CLI Application running:
```
1. List products
2. Add a product
3. Remove a product
4. Calculate total of products
5. Save and exit
Select option:
1
E5T6-9UI3-TH15-QR88 {'product': 'Chicken', 'price': 8.18}
65P1-UDGM-XH2M-LQW2 {'product': 'Tuna', 'price': 5.89}
A12T-4GH7-QPL9-3N4M {'product': 'Cereal', 'price': 3.46}
YRT6-72AS-K736-L4AR {'product': 'Pop', 'price': 1.63}
TQ4C-VV6T-75ZX-1RMR {'product': 'Pizza', 'price': 6.78}
```
