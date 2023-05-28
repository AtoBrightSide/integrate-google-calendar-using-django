# Steps to Run Application Locally
## 1. `pip3 install -r requirements.txt` in console to install required libraries

## 2. Go to Google Developer Console website and get your credentials (`client id` and `client secret key`) and set environment variables in one of the following two ways;

### On the console by using the keyword `export` for Linux and `set` for Windows
    export CLIENT_ID=yourclientid
    export CLIENT_SECRET_KEY=yourclientsecretkey
- You can check if the environment variable has indeed been set by `echo $variable_name`

## OR

### By creating a `.env` file in the working directory and setting the variables there.
    CLIENT_ID=yourclientid
    CLIENT_SECRET_KEY=yourclientsecretkey
- After setting the variables in the .env file, you can access them using Python's `os.environs` dictionary

## 3. ```python3 manage.py runserver``` in console to run app locally 

## 4. Go to `http://127.0.0.1:8000/rest/v1/calendar/init`

## 5. Login using google account