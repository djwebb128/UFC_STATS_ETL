#importing pertinent libraries
import re
import os
import csv
import sys
sys.path.append('./src/')
sys.path.append('./db/')
import psycopg2
import requests
import configparser
import eventDetailsExtractor as e
from bs4 import BeautifulSoup
import pgconnect as pg

# Load config
config = configparser.ConfigParser()

config.read("./config.ini")

if not os.path.exists("./data/ingested_event_urls.csv"):
    
    with open("./data/ingested_event_urls.csv", 'w') as file:
        
        read_file = csv.writer(file)
                
    print("./data/ingested_event_urls.csv created")
    
else:
    
    print("../data/ingested_event_urls.csv already present")

# loading history of previously ingested events
with open("./data/ingested_event_urls.csv", newline="") as file:
    
    read_file = csv.reader(file)
    
    try:
        
        ingested_event_url_list = next(read_file)
        
    except:
        
        ingested_event_url_list = []
    
#making a request for all completed UFC events
event_all_url = "http://ufcstats.com/statistics/events/completed?page=all"

#saving response soup to limit calls
events_response = requests.get(event_all_url)

events_soup = BeautifulSoup(events_response.content, "html.parser")

#extracting the event URLs from soup object
event_url_list = e.getEventUrls(events_soup)

#reversing the list for to maintain chronology upon upload

event_names = list(reversed(e.getEventNames(events_soup)))

event_dates = list(reversed(e.getEventDates(events_soup)))

event_locations = list(reversed(e.getEventLocations(events_soup)))

events_to_upload = []

for index, url in enumerate(event_url_list):
    
    if url in ingested_event_url_list:
        
        pass
        
    else:
        
        events_to_upload.append((event_names[index], event_dates[index], event_locations[index]))
        
        ingested_event_url_list.append(url)

#creating database connection
ufc_conn = pg.ufcConnect(config)

#creating cursor
cur = ufc_conn.cursor()

#inserting data into events table
cur.executemany(f"INSERT INTO events (name, date, location) VALUES (%s, %s, %s)", events_to_upload)

#saving changes
ufc_conn.commit()

#closing connection
ufc_conn.close()

#updating the ingestion history 
with open('./data/ingested_event_urls.csv', 'w', newline='') as file:
    
    csv_writer = csv.writer(file)
        
    csv_writer.writerow(ingested_event_url_list)