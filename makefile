build:
	docker build -t supermarket .
run:
	docker run --rm -e SKUs="${SKUs}" supermarket
