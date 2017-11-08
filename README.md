# Arena Helper
### A website designed to track all information possible for World of Warcraft arenas
#### Contact: 
* jvd5839@g.rit.edu
* jvd33 on github
    
# Planned Features: 
* US and EU server ladder tracking
* Player lookup/Armory with arena win/loss, statistics, achieves
* Talent Builds
* Tracking most commonly used talent builds
* Tracking spec and talent build usage over time, weekly/season 
* **HONOR TALENTS WHEN BLIZZARDS API SUPPORTS IT**


# Development:

## Setup
##### Install a Python 3.6.2 Virtual environment:
* `python -m venv *virtual envi folder name*`

##### Activate the virtual environment
* Windows:
  * run `venv/Scripts/activate.bat`
* Unix:
  * `source venv/bin/activate`

##### Install dependencies (with the virtual environment activated)
* `pip install -r requirements.txt`

##### (Dev) After adding a new dependency
* `pip freeze > requirements.txt`

app.py is the Flask app and main entry point, UI is a React application

To build and run:

`docker-compose build`

`docker-compose up`

