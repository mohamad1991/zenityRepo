FROM python:3.11-slim

RUN pip install requests

COPY app/app.py /app/app.py

WORKDIR /app

CMD ["python", "app.py"]
