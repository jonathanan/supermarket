# supermarket

## Requirements
Docker (Tested with Docker version 17.05.0-ce, build 89658be)

## Building/Testing
To run unit tests and build the application:
`make build` or
`docker build -t supermarket .`

## Running
Set environment variable `SKUS` to a string of products codes separated by
semicolons.

Product codes can be found in `config/products.json`

To run the application:
`make run` or
`docker run --rm -e SKUS=$SKUS supermarket`
