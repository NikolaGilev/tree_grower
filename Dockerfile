FROM --platform=linux/amd64 python:3.12

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install poetry==1.4.2 
RUN poetry config virtualenvs.in-project true 
RUN poetry install --no-root 

COPY . .

ENTRYPOINT ["/app/.venv/bin/uvicorn", "--host", "0.0.0.0", "--port", "80", "app.main:app"]
