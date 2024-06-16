FROM python:3.9  # Base image with Python 3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt  # Install required libraries

COPY data_transmitter.py .  # Copy your Python script

# Optional: Set environment variables for GCS access (consider using Kubernetes Secrets)
# ENV PROJECT_ID your-project-id
# ENV BUCKET_NAME your-bucket-name

CMD ["python", "data_transmitter.py"]
