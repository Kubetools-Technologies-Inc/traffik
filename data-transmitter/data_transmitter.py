import os
from google.cloud import storage  # Import for Google Cloud Storage access
from time import sleep

# User-defined variables (replace with YOUR actual values for testing)
PROJECT_ID = os.environ.get('PROJECT_ID')
BUCKET_NAME = os.environ.get('BUCKET_NAME')

def transmit_data():
  """Checks connection and transmits data from shared volume to GCS"""
  # Client configuration using user-defined variables
  client = storage.Client(project=PROJECT_ID)

  # Check connection to GCS
  try:
    buckets = list(client.list_buckets())
    print(f"Successfully connected to GCS. Found buckets: {buckets}")
  except Exception as e:
    print(f"Error connecting to GCS: {e}")
    return

  # Access data file from shared volume (replace with your data file path and format)
  data_file = os.path.join("/shared", "traffic_data.json")  # Example path

  if not os.path.exists(data_file):
    print(f"Data file not found: {data_file}")
    return

  # Read data from the file
  with open(data_file, "r") as f:
    data = f.read()

  # Create a new blob in the bucket
  blob = client.bucket(BUCKET_NAME).blob(os.path.basename(data_file))  # Use filename
  blob.upload_from_string(data)

  print(f"Data uploaded to GCS bucket: {BUCKET_NAME}, Blob name: {blob.name}")

if __name__ == "__main__":
  while True:
    transmit_data()
    # Adjust the sleep time (in seconds) for desired data transfer frequency
    sleep(10)

