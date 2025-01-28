FROM python:3.11 

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN apt-get update && apt-get install -y python3-distutils
RUN pip install -r requirements.txt

# Command to run the application
CMD ["python", "server.py"]
