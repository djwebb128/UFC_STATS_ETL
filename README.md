# UFC_STATS_ETL
## Overview

The Ultimate Fighting Championship (UFC) is currently one of the most popular sport franchises in the world. There have been many mostly, friendly debates over what makes a fighter the best, or what makes them better than their opponent. I'm developing this pipeline to develop some insight into what makes for a good fighter.

## Setup

### Cloning the repo
1. Clone the present repo to target directory
   ```
   git clone git@github.com:djwebb128/UFC_STATS_ETL.git
   ```
3. Navigate into the UFC_STATS_ETL directory
   ```
   cd UFC_STATS_ETL
   ```
5. Create your config.ini
   ```
   touch config.ini
   ```
### Configuring your config.ini
   The layout should match the below template:
```
[<your_db>]
host = localhost
dbname = <your_db>
user = postgres
password = <your_password>
port = <your_port>
```
**The present project uses postgreSQL and the config.ini is formatted for connecting to postgreSQL databases. If you do not have postgres installed locally, please reference the documentation [here](https://www.postgresql.org/download/) to download it.**
### Creating your virtual environment
1. Create the virtual environment
   ```
   python3 -m venv <your_venv>
   ```
3. Activate your virtual environment
   ```
   source activate <your_venv>
   ```
5. Insall your dependencies
   ```
   pip install -r requirements.txt
   ```

## Directory Tree

<pre> 
├── config.ini
├── src
│   ├── event_data_extraction_pipeline.py
│   ├── event_etl_pipeline.py
│   └── __init__.py
├── queries
│   └── ufcInsertQueries.py
│   ├── __init__.py
├── extract
│   ├── eventDetailsExtractor.py
│   ├── fightDetailsExtractor.py
├── db
│   └── pgconnect.py
│   ├── __init__.py
├── data
├── DATADICTIONARY.md
├── LICENSE
├── README.md
</pre>

## Process Map
TBD

## Database Schema
To store the data scapped for the present database, a relational database model was employed. Please reference the data dictionary
![UFC Database Model](https://lucid.app/publicSegments/view/9b9a607d-3ade-48c3-9124-a571201d1ac6/image.png)
