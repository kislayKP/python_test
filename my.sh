#!/bin/bash

# MySQL credentials
DB_USER="root"
DB_PASS="student"

# Run MySQL command to show databases
mysql -u"$DB_USER" -p"$DB_PASS" -e "SHOW DATABASES;"
