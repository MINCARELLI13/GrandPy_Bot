# GrandPy_Bot

## What is the purpose of this application?

This application allows you to find the address of any place in the world (examples: Eiffel Tower, pyramid of Menkaure in Egypt, the "good mother" in Marseille ...) with the added bonus of the location of the site on a Google map as well as a wikipedia explanation of the location sought.

## How to launch the application?

- Online, go to the following address: https://grandpybot-em.herokuapp.com/

- Local :
- Create a virtual environment and activate it
- Get the files from the GitHub repository: https://github.com/MINCARELLI13/GrandPy_Bot.git
- Install the dependencies of the requirements.txt file
- The run.py program can then be launched
- Once launched, go to your browser and enter the following url: http://127.0.0.1:5000/
- When you are done, don't forget to deactivate your virtual environment!

## How to use this application?

On the home page, enter a question including an address request and press the "Enter" key on your keyboard.
The application will offer you an address response as well as the location of the place on a Google map.
As a bonus, your Grand-Py will tell you an anecdote from his research on Wikipedia, in connection with the address retrieved.

## What APIs are used in this application?

- the Google Places API to obtain the address of the place as well as the latitude and longitude of the site.
- the Google Maps API to display a Google map in which the requested location appears with a marker indicating the precise address.
- the Wiki Media API to obtain the history of the searched place.

## What are the main programs used?

- Python-3.8
- HTML and CSS
- Bootstrap
- Javascript
- Flask 