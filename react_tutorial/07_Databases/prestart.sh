#!/bin/bash

# Start DB
python app/backend_pre_start.py

# Run migrations
alembic update head 

# Create initial data in DB
python app/initial_data.py