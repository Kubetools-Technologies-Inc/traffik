from faker import Faker
import flask  # Import Flask for creating health and readiness endpoints
import json  # Import for JSON data transmission
import random
import time

# Configure for shared volume access (replace with actual volume mount path)
SHARED_DATA_PATH = "/shared"

app = flask.Flask(__name__)

# Create a Faker instance with a specific locale for realistic data (optional)
fake = Faker('en-US')  # Adjust locale code for desired region (e.g., 'de-DE' for Germany)
# Initialize data_list as an empty list
data_list = []

@app.route("/health")
def health_check():
  """Liveness Probe Endpoint"""
  try:
    # Perform a simple health check (e.g., verify Faker is initialized)
    if fake:
      return flask.jsonify({"status": "healthy"}), 200
    else:
      return flask.jsonify({"status": "unhealthy"}), 500
  except Exception as e:
    return flask.jsonify({"status": f"error: {str(e)}"}), 500

@app.route("/ready")
def is_ready():
  """Readiness Probe Endpoint"""
  # Check if data generation loop is running (replace with your actual logic)
  # For example, check a flag or counter set during data generation
  is_generating_data = True  # Placeholder, replace with actual logic
  if is_generating_data:
    return flask.jsonify({"status": "ready"}), 200
  else:
    return flask.jsonify({"status": "not ready"}), 500

# Simulate loop for generating traffic data
while True:
  # Generate random traffic data (example)
  intersection = fake.address()
  # Adjust speed range based on your scenario (e.g., higher for highways)
  speed = fake.pyfloat(min_value=30.0, max_value=80.0)
  volume = fake.pyint(min_value=10, max_value=100)  # Simulate traffic volume (number of vehicles)
  occupancy = round(random.random(), 2)  # Simulate occupancy (percentage)

  # Prepare data in JSON format
  traffic_data = {
      "intersection": intersection,
      "speed": speed,
      "volume": volume,
      "occupancy": occupancy
  }
  # Append the new data to the list
  data_list.append(traffic_data)
  
  # Save the updated data list to the file
  with open(f"{SHARED_DATA_PATH}/traffic_data.json", "w") as file:
    json.dump(data_list, file)

  # Print confirmation message
  print("Data saved to shared volume")

  # Adjust sleep time to simulate real-time data (e.g., sleep for a few seconds)
  time.sleep(5)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)  # Run Flask app on port 8080 (matches container port
