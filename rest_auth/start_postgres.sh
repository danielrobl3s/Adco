#!/bin/bash

# Check if PostgreSQL is already running
if pgrep "postgres" > /dev/null
then
    echo "PostgreSQL is already running."
else
    # Start PostgreSQL server
    /usr/local/bin/pg_ctl -D /usr/local/var/postgres start
    
    # Check if PostgreSQL started successfully
    if [ $? -eq 0 ]
    then
        echo "PostgreSQL has been started."
    else
        echo "Failed to start PostgreSQL."
    fi
fi

# Activate virtual environment (replace with path to your venv)
source ../env/scripts/activate

# Run Django development server
python manage.py runserver