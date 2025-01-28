FROM python:3.11 

# Set the working directory
WORKDIR /app

# Copy only the necessary files into the container
COPY requirements.txt /app/
COPY server.py /app/
COPY templates /app/templates/
COPY EmotionDetection /app/EmotionDetection/

# Install dependencies
RUN apt-get update && apt-get install -y python3-distutils
RUN pip install -r requirements.txt

# Command to run the application
CMD ["python", "server.py"]
