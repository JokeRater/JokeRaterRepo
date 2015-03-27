# JokeRater

JokeRater is a webapp implemented using Python and Django that allows users to create and rate their favourite jokes
A live demo of the app is avalaible at http://jokerater.pythonanywhere.com/JokeRater

## Project Info
This Web App was created for WAD2 course at University of Glasgow
Deevloped by Robert Allison, Chris Brown, Gary Curran and Ben Procter

## Set Up and Deployment

In order to run JokeRater on your machine, you will need a virtual environment running both Django 1.7 and Python 2.7
You will also need to install various additional add-ons which can be found in the Requirements.txt file

The code can be found using 
	
	git clone https://github.com/JokeRater/JokeRaterRepo.git
	
	cd JokeRaterProject
	python manage.py migrate
	python populate_jokeRater.py
	python manage.py runserver
	
	
## Usage

You can choose which joke is your favourite by clicking the select button

To create your own joke you must be registered and can then add from your profile

If you believe a jopke to be unsavoury, click report and a moderator will review if at the first possible opportunity