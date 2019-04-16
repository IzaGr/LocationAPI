#Python LocationAPI with CLI

#LocationAPI functionalities:

1. Adding new location to the database 
    * location name
    * location longitude
    * location latitude
    * location elevation (calculated based on online elevation api 'https://elevation-api.io/api/elevation?points=')

2. Finding location nearest to the user location
    * retrieving user data (first name, last name, user location data )
    * returning nearest location data and distance to the user
    
3. Finding all locations in range
    * retrieving user data (first name, last name, user location data )
    * retrieving range as user input
    * returning all locations in range and distance to the user

#User dashboard
 Options: 
 1. Add new location 
 2. Check nearest locations 
     1) Find nearest location
     2) Find all locations in range  
 3. Quit
 
# Getting Started
    
## Used technologies and tools:
* Python 3.7.1, 
* SQLite database - database file (database.db) with few initial locations included to the procject
* SQLAlchemy
* json
* urllib
* math
* pytest  

### Installing

install.sh

Program entry point:
__main__.py

## Running the tests
    ### Database tests
    conftest.py
    
#TO DO

* elevation function testing - tests.py
* improve database tests - conftest.py
* __main__.py cleaning
* better looking CLI
