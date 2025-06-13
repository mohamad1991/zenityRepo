#!/bin/bash

# Run Project
cd theDoctor
docker compose up --build -d
sleep 5

# Query results
curl 127.0.0.1:5001/secret | jq '.secretCode'
curl 127.0.0.1:5001/health | jq '.'

# Destroy 
docker compose down

