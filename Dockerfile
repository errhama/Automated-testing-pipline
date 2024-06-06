# Use Python 3.8 slim version as the base image
FROM python:3.8-slim

# Install necessary packages
RUN  apt-get update &&  apt-get install -y wget unzip curl


WORKDIR /app

# Copy Python dependencies file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the test script
COPY test_all_button.py .

# Command to run the tests
CMD ["python3", "test_all_button.py"]