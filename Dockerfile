FROM browserless/chrome:latest

# Install Python 3 and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy the test script
COPY test_all_button.py .

# Run the test script
CMD ["python3", "test_all_button.py"]
