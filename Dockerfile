FROM python:3.10


WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3-venv \
    libatlas-base-dev \
    libopenblas-dev

COPY requirements.txt /app/

RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD ["python", "server.py"]

