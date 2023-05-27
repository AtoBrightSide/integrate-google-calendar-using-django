Steps to Run Application
1. Type `pip3 install -r requirements.txt` in console 
2. Create google credentials(client id and client secret key) and set environment variable as follows;
    - CLIENT_ID=yourclientid
    - CLIENT_SECRET_KEY=yourclientsecretkey
    You can set environment variables in one of two ways;
        - On the console by using the keyword `export` for Linux and `set` for Windows
            - You can check if the environment variable has indeed been set by `echo $variable_name`
        - By creating a `.env` file in the working directory and setting the variables there.
3. Type ```python3 manage.py runserver``` in console 
4. Go to `http://127.0.0.1:8000/rest/v1/calendar/init`
5. Login using google account