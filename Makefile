build:
	docker build -t supermarket .
run:
	docker run --rm -e SKUS="${SKUS}" supermarket
