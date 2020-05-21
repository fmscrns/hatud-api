# hatud-api
This is an API using Python Flask-RESTPlus for a food delivery system called Hatud.

###### __SET UP INSTRUCTIONS__ (BY ORDER)
1. To enable Python virtual environment...
- input ". venv/bin/activate" or "source venv/bin/activate"
- you should see "(venv)" before the command line prompt

2. To install Python required dependencies...
- input "pip install -r requirements.txt"

3. To enable environment configuration file...
- change ".env.example" file in root folder into ".env" and set up the required fields e.g. DATABASE_URL

4. Create your preferred database manually

5. To migrate database models...
- input "python manage.py db migrate"
- input "python manage.py db upgrade"

6. To run the application...
- input "flask run"

###### __ADDITIONAL INSTRUCTIONS__
* To change port...
- open ".flaskenv" file  in root folder and change "FLASK_RUN_PORT" variable to you preferred port