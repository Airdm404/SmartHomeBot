# SmartHomeBot

The SmartHome Slack Bot is an interactive Slack app that enables users to query product information from a database that was specifically created by scraping a subsection of data from the 'Smart Home' section of the Home Depot website.

# Features
The bot allows querying by:
* Product ID - id: product_id_number(found in a parenthesis just before product name)
* Product Category - cat:category_name
* Product Brand - brand:brand_name


Additionally, it supports the following Slack slash commands:

* /brands - Lists all available brands
* /categories - Lists all available categories


# Setting up enviroments

## Slack Setup
* Bot Token Scopes: chat:write, channels:history, commands

## Python Setup
* pip3 install slackclient for slack sdk
* pip3 install python-dotenv for python-dotenv
* pip3 install slackeventsapi for slackeventsapi
* pip3 install flask for flask

## Local Server Setup
* Install ngrok:https://ngrok.com/download
* run ngrok http 5002 to start ngrok and copy the https url
* paste the url in the request url field when you enable events under events subscriptions followed by "/slack/events"
* save changes and reinstall app into work place



# Usage
* Set the environment variables in .env file(Slack bot token and sign secret):\
    SLACK_BOT_TOKEN=YOUR_BOT_USER_OAuth_Token\
    SIGN_SECRET=YOUR_SIGNING_SECRET
* Run the bot:
  python3 main.py
* Open your Slack workspace, add bot to a channel and start interacting with the bot.

# Libraries/Modules Used
* Flask - A lightweight WSGI web application framework.
* Slack SDK for Python - This allows for interaction with the Slack API.
* Slackeventsapi - This allows the bot to use the Events API.
* python-dotenv - This allows the application to use environment variables from a .env file.
* os - This provides functions for interacting with the operating system.
Contributing


