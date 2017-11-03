FROM python:3

WORKDIR /usr/src/app
COPY . /usr/src/app

# Run unit tests
RUN python test_supermarket_register.py

CMD ["python", "app.py"]
