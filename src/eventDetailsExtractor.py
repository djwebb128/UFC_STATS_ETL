from bs4 import BeautifulSoup
import re
import requests

def getEventUrls(event_soup: BeautifulSoup) -> BeautifulSoup:
	
	'''
	Returns the event urls found on the given UFC Stats url
		
	Parameters:
	---------------- 
	
	string: unmodified target events url
	
	Returns:
	----------------  
	
	list: python object containing strings of event urls
	'''
	
	events = event_soup.findAll("a", attrs={"class": re.compile("b-link b-link_style_black")})
	
	event_url_list = [event.get("href") for event in events]
	
	return event_url_list

def getEventDates(event_soup: BeautifulSoup) -> BeautifulSoup:
    
    '''
    Fetches the event urls found on the given UFC Stats url
        
    Parameters:
    ----------------    
    
    string: unmodified target events url
    
    Returns:
    ----------------    
    
        list: python object containing strings of event dates
    '''
	
    event_dates = event_soup.findAll("span", attrs={"class": re.compile("b-statistics__date")})

    event_dates_list = [event_date.text.strip() for event_date in event_dates]
    
    return event_dates_list[1:]

def getEventLocations(event_soup: BeautifulSoup) -> BeautifulSoup:
    
	'''
	Fetches the event city, state/province/country for events on UFC Stats
		
	Parameters:
	----------------    
	
	string: unmodified target events url
	
	Returns:
	----------------    
	
		list: python object containing strings of event dates
	'''
	event_locations = event_soup.findAll("td", attrs={"class": re.compile("b-statistics__table-col b-statistics__table-col")})
	
	event_location_list = [event_location.text.strip().split(',') for event_location in event_locations[1:]]
	
	return event_location_list

def getEventFightUrls(event_details_url: str) -> str:
    
    '''
    Fetches the event urls found on the given UFC Stats
        
    Parameters:
    ---------------- 
    
    string: unmodified target event-details url
    
    Returns:
    ----------------    
    
    list: python object containing strings of event dates
    '''   
    
    events_response = requests.get(event_details_url)
    
    event_soup = BeautifulSoup(events_response.content, "html.parser")
    
    event_fights = event_soup.findAll("a", attrs={"class": re.compile("b-flag b-flag_style_green")})
    
    event_fight_url_list = [fight.get("href") for fight in event_fights]
    
    return event_fight_url_list

def getFightStatsTables(fight_url):
    
    fight_stats_tables_list = pd.read_html(fight_url)

    return fight_stats_tables_list