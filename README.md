# supermarket
A Supermarket Register CLI application which can take a set of product codes, look up
the price of each product, and compute the total amount of the sale (including
local sales tax).


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
Set environment variable `SKUS` to a string of products codes separated by
semicolons.

Product codes can be found in `config/products.json`

To run the application:
```
# Using Makefile
make run

# Using docker explicitly
docker run --rm -e SKUS=$SKUS supermarket
````
