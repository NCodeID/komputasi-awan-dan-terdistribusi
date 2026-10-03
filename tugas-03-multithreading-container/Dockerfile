# TODO 1: Pilih base image Python resmi yang ringan (cari tag "slim" di Docker Hub).
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
# TODO 2: Tulis perintah untuk install dependency dari requirements.txt.

RUN "pip -r install requirements.txt"

COPY src/ ./src/

# TODO 3: Tulis perintah default yang dijalankan saat container start,
# yaitu menjalankan src/order_simulator.py dengan python3.
CMD ["python3", "src/order_simulator.py"]
