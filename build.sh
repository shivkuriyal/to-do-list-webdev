#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install python dependencies
python3 -m pip install -r requirements.txt || pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput || python manage.py collectstatic --noinput

# Run database migrations
python3 manage.py migrate || python manage.py migrate

# Seed sample tasks
python3 manage.py seed_tasks || python manage.py seed_tasks
