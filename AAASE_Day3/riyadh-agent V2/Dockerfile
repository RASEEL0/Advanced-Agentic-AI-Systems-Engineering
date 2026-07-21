FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV REPORTS_DIR=/reports

RUN mkdir /reports

VOLUME /reports

CMD ["python", "app.py"]