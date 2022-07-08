**This is my solution for the task assignment below. Assignment is also a description how the application works.**

**The whole project was dockerized.**

## RUNNING THE APPLICATION:

1. Docker and docker-compose should be installed on your computer

2. The project folder should contain an .env file with these environment variables:
    ```
    API_KEY=        #you can get yours here: https://free.currencyconverterapi.com/
    DB_USER=        #default: postgres
    DB_PASSWORD=    #default: postgres
    ```
3. Everthing needed for the application and application itself should start with with the following command from the project directory: 
    ```
    docker-compose run --rm main
    ```
    
## TASK ASSIGNMENT:

Create a CLI application that will prompt the user for a currency pair 
and then print the exchange rate for that pair.
The exchange rate should be rounded to 2 decimal places.

The app should prompt the user for a currency pair in a loop until the user
enters the command 'quit', which should exit the app, or a command 'history', 
which should print all the currency pairs for which the user has requested an exchange rate.

A valid input will be in form "USD EUR". The app should then print the 
exchange rate for that pair.

The currency pair input should be treated as case-insensitive. All of these are a valid input:
```
USD EUR
usd eur
usD EuR
```
No other input besides two currency pairs and commands for quitting and history should be accepted.
If user enters an invalid input, the app should print an error message and prompt the user again.

If the exchange rate is higher than it was yesterday, the app should print the exchange rate in green letters.
If the exchange rate is lower than it was yesterday, the app should print the exchange rate in red letters.

All of the user's input should be stored in a PostgreSQL database, to be later retrieved
when the user types the command 'history'. It's up to you how you model the relations in that database.

One line of the 'history' command output should contain the time & date of the conversion (when the user inputted the pair)
the currency pair (USD EUR) and the exchange rate. The exchange rate should be color-coded as described above (green or red).
(This means that you will somehow have to store in database whether the exchange rate was higher of lower than a day before.)

An example 'history' command output:
```
2022-05-02 12:00 USD EUR 1.12
2022-05-04 23:13 AUD CAD 1.82
2022-05-03 11:57 CHF JPY 14.22
```
The formatting of the date and time is up to you.

The database should be running in Docker. The definition of that containerized database should be
in a compose-file. 

To get the currency exchange rate, you can use the following API:
    https://free.currencyconverterapi.com/

You shouldn't hard-code the API key in your code. Instead, you should read it from an environment variable.

Some libraries that might come in handy:
    requests
    psycopg2
    sys
    string (Template)
    os
    datetime

All of the codebase should be checked-in in a publicly accessible remote repository on GitHub.

glhf
