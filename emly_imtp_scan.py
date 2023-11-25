# emlx_imtop_scan.py
# SOURCE

import os
import pymysql
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve MySQL connection details from environment variables
db_host = os.getenv("DB_HOST", "localhost")
db_user = os.getenv("DB_USER", "sec_user")
db_pass = os.getenv("DB_PASS", "password")
db_name = os.getenv("DB_NAME", "database_master")


# Connect to the MySQL instance
con = pymysql.connect(
    host=db_host,
    user=db_user,
    password=db_pass,
    database=db_name,
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)

# Perform your database operations using 'con'

# Don't forget to close the connection when done
con.close()
