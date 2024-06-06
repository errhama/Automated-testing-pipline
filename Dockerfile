FROM google/chrome:latest

RUN apt-get update && apt-get install -y python3

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY test_all_button.py .

CMD ["python3", "test_all_button.py"]