import bs4
from bs4 import NavigableString
import re
import requests
import pandas as pd

def getFighters(bout_soup: bs4.BeautifulSoup) -> tuple[str, str]:
	    
    '''
    Fetches a tuple of the bout's fighters' names
        
    Parameters:
    ----------------    
    
    BeautifulSoup: unmodified, parsed target bout url
    
    Returns:
    ----------------    
    
    tuple (string, string): fighter_1_name, fighter_2_name 
    '''
	
    #confirming that there is data for 2 fighters
    fighter_n = len(bout_soup.findAll("a", attrs={"class": re.compile("b-link b-fight-details__person-link")}))

    #ensuring the return of null values if fighter(s) absent
    fighter_1, fighter_2 = None, None

    #isolating the fighter assigned to each corner
    if fighter_n == 2:

        fighter_1 = bout_soup.findAll("a", attrs={"class": re.compile("b-link b-fight-details__person-link")})[0].text.strip()
		
        fighter_2 = bout_soup.findAll("a", attrs={"class": re.compile("b-link b-fight-details__person-link")})[1].text.strip()
        
    return fighter_1, fighter_2

def getFightWinner(bout_soup: bs4.BeautifulSoup) -> str:

    '''
    Fetches the winner of bout
        
    Parameters:
    ----------------    

	BeautifulSoup: unmodified, parsed target bout url
    
    Returns:
    ----------------    
    
    str: winner of bout
    '''
    
    fighter_headlines = bout_soup.findAll("div", attrs={"class": re.compile('b-fight-details__person')})[0]
    
    isolation_list = []
    
    for fighter_headline in fighter_headlines:
        
        if isinstance(fighter_headline, NavigableString)==False:
            
            isolation_list.append(fighter_headline)
            
    for headline in isolation_list:
        
        winner = headline.find("i", attrs={"class": re.compile("b-fight-details__person-status b-fight-details__person-status_style_green")})
        
        if winner:
            
            name = headline.find("a", attrs={"class": re.compile("b-link b-fight")}).text.strip()
            
    return name

def getFightWeightClass(bout_soup: bs4.BeautifulSoup) -> str:
    	    
    '''
    Fetches a string for the bout's weight class
        
    Parameters:
    ----------------    

	BeautifulSoup: unmodified, parsed target bout url
    
    Returns:
    ----------------    
    
    str: weight class of bout
    '''
	
    weight_class_raw = bout_soup.find("i", attrs={"class": re.compile("b-fight-details__fight-title")}).text
    
    weight_class_words = weight_class_raw.split()

    #identifying strings with weight key word
    weight_class_search = [weight for weight in weight_class_words if weight.endswith('weight')]

    if len(weight_class_search) == 1:

        weight_class = weight_class_search[0]
        
    else:
        
        weight_class = None
        
    # return weight_class
    return weight_class

def getFightOutcome(bout_soup: bs4.BeautifulSoup) -> str:
        	    
    '''
    Fetches a tuple of the bout's fighters' names
        
    Parameters:
    ----------------    

	BeautifulSoup: unmodified, parsed target bout url
    
    Returns:
    ----------------    
    
    list: [
            method, 
            round bout was stopped,
            time bout was stopped,
            fight round format,
            bout referee,
            additional notable details
            ]
    '''
	
    search = bout_soup.findAll("i", attrs={"class": re.compile("b-fight-details__text")})

    values_list = []
    judge_array = []
    for detail in search:    
        
        if 'Method:' in detail.text:
            
            text = detail.text.split(':')[1].strip()
            
            if text == '':
                
                values_list.append(None)
                
            else:
                
                values_list.append(text)
                
        elif 'Round:' in detail.text:
            
            text = detail.text.split(':')[1].strip()
            
            if text == '':
                
                values_list.append(None)
                
            else:
                
                values_list.append(text)
                
        elif 'Time:' in detail.text:
            
            text = detail.text.strip().split(maxsplit=1)[1]
            
            if text == '':
                
                values_list.append(None)
                
            else:
                
                values_list.append(text)
                
        elif 'Time format:' in detail.text:
            
            text = detail.text.split(':')[1].strip()
            
            if text == '':
                
                values_list.append(None)
                
            else:
                
                values_list.append(text)
                
        elif 'Referee:' in detail.text:
            
            text = detail.text.split(':')[1].strip()
            
            if text == '':
                
                values_list.append(None)
                
            else:
                
                values_list.append(text)

        elif ':' not in detail.text:
            
            lines = [line.strip().replace('.', '') for line in detail.text.splitlines() if line.strip()]

            if len(lines) == 2:
                
                judge_tuple = ','.join(lines)
                
                judge_array.append([judge_tuple])

    if judge_array == []:
        
        values_list.append(None)
        
    else:
        
        values_list.append(judge_array)
        
    return values_list

def getSigStrkTrgts(bout_soup: bs4.BeautifulSoup) -> str:
            	    
    '''
    Fetches a significant strike percentages for bout
        
    Parameters:
    ----------------    

	BeautifulSoup: unmodified, parsed target bout url
    
    Returns:
    ----------------    
    
    tuple (list, list): (
                            [head1, body1, leg1, distance1, clinch1, ground1], 
                            [head2, body2, leg2, distance2, clinch2, ground2]
                        )
    '''
    
    sig_strk_brkdn_list = bout_soup.findAll("i", attrs={"class": re.compile("b-fight-details__charts-num")})

    stats_list = []
    
    for stat in sig_strk_brkdn_list:
        
        stats_list.append(stat.text.strip())
    
    return stats_list

def getFightStats(bout_soup: bs4.BeautifulSoup) -> str:
            	    
    '''
    Fetches a summary and round by round stats for a bout
        
    Parameters:
    ----------------    

	BeautifulSoup: unmodified, parsed target bout url
    
    Returns:
    ----------------    
    
    tuple (list, list, list, list) : (
                                        [
                                            totals,
                                            totals_pr_rnd,
                                            sig_strks_totals,
                                            sig_strks_pr_rnd
                                        ]
                                    )
    '''
    
    sections_soups = bout_soup.findAll("tbody", attrs={"class": re.compile("b-fight-details__table")})

    if len(sections_soups) == 4:
        
        sections_data = []

        for section in sections_soups:
            
            section_soup = section.findAll("p", attrs={"class": re.compile("b-fight-details__table-text")})
            
            section_data = []
            
            for item in section_soup:
                
                if not item.find('a'):
                    
                    section_data.append(item.get_text(strip=True))

            section_data = [None if '--' in item or '---' in item else item for item in section_data]
            sections_data.append(section_data)
        
        totals = sections_data[0]
        
        totals_pr_rnd = sections_data[1]
        
        sig_strks_totals = sections_data[2]
        
        sig_strks_pr_rnd = sections_data[3]
    
    return totals, totals_pr_rnd, sig_strks_totals, sig_strks_pr_rnd

def extractFightData(bout_soup):
            	    
    '''
    Fetches a dictionary of all fight summary and round by round statistics
        
    Parameters:
    ----------------    

	BeautifulSoup: unmodified, parsed target bout url
    
    Returns:
    ----------------    
    
    dictionary: {
                'matchup': bout_matchups_list,
                'winner': bout_winner,
                'weight_class': bout_weight_class,
                'outcome': bout_outcome,
                'fight_stats_list': bout_stats_list,
                'sig_strks_list': bout_sig_strks_list
                }
    '''

    bout_matchups_list = getFighters(bout_soup)

    bout_winner = getFightWinner(bout_soup)

    bout_weight_class = getFightWeightClass(bout_soup)

    bout_outcome = getFightOutcome(bout_soup)
    
    bout_sig_strks_list = getSigStrkTrgts(bout_soup)

    bout_stats_list = getFightStats(bout_soup)

    fight_data_dict = {
                        'matchup': bout_matchups_list,
                        'winner': bout_winner,
                        'weight_class': bout_weight_class,
                        'outcome': bout_outcome,
                        'fight_stats_list': bout_stats_list,
                        'sig_strks_list': bout_sig_strks_list
                        }

    return fight_data_dict

if __name__ == "__main__":
	
    main()