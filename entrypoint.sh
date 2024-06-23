#!/bin/bash

# Exit on error
set -e

# Run migrations
python manage.py migrate

# Start the Django development server
exec "$@"
