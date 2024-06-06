FROM python:3.10

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
 && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
 && apt install -y ./google-chrome-stable_current_amd64.deb \
 && rm google-chrome-stable_current_amd64.deb \
 && apt-get clean 

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy the test script
COPY test_all_button.py .

# Run the test script
CMD ["python3", "test_all_button.py"]
