# Base image for Python environment
FROM python:3.8-slim

# Set working directory
WORKDIR /app

ENV SHARED_DATA_PATH /shared

VOLUME ["/shared"]
# Install required libraries
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy your Python script for data collection
COPY data_collection.py .

# Set the entrypoint for the container
ENTRYPOINT ["python", "data_collection.py"]

# Expose port for potential future communication (optional)
EXPOSE 8080

# Command to run the script when container starts
CMD ["tail", "-f", "$SHARED_DATA_PATH/traffic_data.json"]

