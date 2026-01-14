FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --fix-missing \
  build-essential \
  curl \
  || (apt-get update && apt-get install -y --fix-missing build-essential curl) \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install jupyter

COPY . .

CMD ["python", "new_demo.py"]
