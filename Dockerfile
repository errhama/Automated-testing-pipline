FROM debian:latest

# Install dependencies

RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    python3 \
    python3-pip
# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy the test script
COPY test_all_button.py .

# Run the test script
CMD ["python3", "test_all_button.py"]
