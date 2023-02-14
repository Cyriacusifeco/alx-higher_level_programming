#!/bin/bash
-- A script that lists all the databases
# Replace the username and password with your own
MYSQL_USER="your_username"
MYSQL_PASSWORD="your_password"

# Use the mysql command to get a list of all databases
mysql -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "SHOW DATABASES;"

