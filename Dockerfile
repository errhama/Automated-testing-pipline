FROM selenium/chrome-standalone  
# Public Chrome image

# Install Python 3 (modify based on your base image)
RUN yum -y install python3  # Replace with appropriate package manager for your base image

# Rest of your Dockerfile content...

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY test_all_button.py .

CMD ["python3", "test_all_button.py"]
