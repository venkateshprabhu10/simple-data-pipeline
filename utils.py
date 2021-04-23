import pandas as pd
import mysql.connector as mc
from mysql.connector import errorcode as ec
import psycopg2
from config import DB_DETAILS

def get_tables(path):
    tables = pd.read_csv(path, sep=":")
    return tables["table"][tables["to_be_loaded"]=="yes"]

def get_credentials(env):
    return DB_DETAILS[env] if env in DB_DETAILS.keys() else exit

def get_mysql_connection(details):
    try:
        mysql_conn = mc.connect(
            user = details["db_user"],
            password = details["db_password"],
            host = details["db_host"],
            database = details["db_name"],
        )
        return mysql_conn

    except mc.Error as error:
        if error.errno == ec.ER_ACCESS_DENIED_ERROR:
            print("Invalid Credentials")
        else:
            print(error)

def get_postgres_connection(details):
    postgres_conn = psycopg2.connect(
        f"dbname = {details['db_name']} user = {details['db_user']} host = {details['db_host']} password = {details['db_password']}"
    )
    return postgres_conn

def get_connection(details):
    connection = None

    if details["db_type"] == "mysql":
        return get_mysql_connection(details)
    elif details["db_type"] == "postgres":
        return get_postgres_connection(details)