build:
	docker build -t supermarket .
run:
	docker run -e SKUS="${SKUS}" -it supermarket
