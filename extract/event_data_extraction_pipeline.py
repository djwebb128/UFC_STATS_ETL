#importing pertinent libraries
import os
import csv
import sys
sys.path.append('../src/')
import bs4
import time
import random
import pandas as pd
import requests, re
from bs4 import BeautifulSoup
import eventDetailsExtractor as e

#making a request for all completed UFC events
event_all_url = "http://ufcstats.com/statistics/events/completed?page=all"

#saving response soup to limit calls
events_response = requests.get(event_all_url)

events_soup = BeautifulSoup(events_response.content, "html.parser")

#extracting the event URLs from soup object
event_url_list = e.getEventUrls(events_soup)

#saving event_urls to csv for upload
with open('./data/event_urls.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(event_url_list)

#extracting event dates from soup object
event_date_list = e.getEventDates(events_soup)

#saving event_data to csv for upload
with open('./data/event_dates.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(event_date_list)

#extracting event locations from soup object
event_location_list = e.getEventLocations(events_soup)

#saving event locations for upload
with open('./data/event_locations.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(event_location_list)

#extracting and saving the list of fights ties to each event
with open('../data/event_fights.csv', 'a', newline='') as file:
   
    writer = csv.writer(file)

    for event_url in event_url_list:
		
        delay = random.uniform(5, 15)
    
        response = requests.get(event_url)
    
        fight_list = e.getEventFightUrls(event_url)
        
        writer.writerow(fight_list)
        
        time.sleep(delay)