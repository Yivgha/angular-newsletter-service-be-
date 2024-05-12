FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install uvicorn fastapi

RUN pip install -r requirements.txt

CMD python -m uvicorn main:app --port=8000 --host=0.0.0.0
