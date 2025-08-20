import psycopg2
import configparser
import os

# Load config
config = configparser.ConfigParser()

config.read("../config.ini")

def ufcConnect(config):
    """ Connect to the PostgreSQL database server """
    try:
        return psycopg2.connect(
                                dbname=config["ufc"]["dbname"],
                                user=config["ufc"]["user"],
                                password=config["ufc"]["password"],
                                host=config["ufc"]["host"],
                                port=config["ufc"].getint("port")
        )
    except (psycopg2.DatabaseError, Exception) as error:
		
        print(error)

if __name__ == '__main__':
	
    # config = load_config()

    connect(config)