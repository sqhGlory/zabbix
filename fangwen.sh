#!/bin/bash

# Set the number of requests to be sent
num_requests=1000

# Loop for the specified number of requests
for ((i=1; i<=$num_requests; i++)); do
  # Generate a random number between 1 and 100
  rand=$((1 + RANDOM % 100))
  # Send a GET request to the specified path, including the generated number
    curl -k https://172.16.66.26/path/to/resource?num=$rand
done