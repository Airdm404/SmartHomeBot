import slack
import os
import database as db
import helpers as hp
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter


env_path = Path('.') / ".env"
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGN_SECRET'],'/slack/events', app)
client = slack.WebClient(token=os.environ['SLACK_BOT_TOKEN'])
BOT_ID = client.api_call('auth.test')['user_id']


#messages: handles message inputs from user
@slack_event_adapter.on('message')
def message(payload):
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')
    text = text.lower()

    if BOT_ID != user_id:
        if text.startswith('id:'):
            # Extract the ID from the text
            id_str = text.split('id:')[1].strip()
            try:
                product_id = int(id_str)
            except ValueError:
                response = "Invalid ID format. Please enter an integer."
                client.chat_postMessage(channel=channel_id, text=response)
            else:
                product_info = db.products.get(product_id)
            if product_info is not None:
                response = hp.formulate_response(product_info)
                client.chat_postMessage(channel=channel_id, blocks=response)
            else:
                response = "No product found with ID: {}".format(product_id)
                client.chat_postMessage(channel=channel_id, text=response)


        elif text.lower().startswith('cat:'):
            cat_str = text.split('cat:')[1].strip()
            if cat_str in db.catType:
                response = ""
                for id in db.catType[cat_str]:
                    product_info = db.products.get(id)
                    response += f"({id}) {product_info['Name']}\n"
                if response == "":
                    response = "No products found for this category."
                client.chat_postMessage(channel=channel_id, text=response)
            else:
                response = "No category found with name: {}".format(cat_str)
                client.chat_postMessage(channel=channel_id, text=response)

        
        elif text.lower().startswith('brand:'):
            brand_str = text.split('brand:')[1].strip()
            if brand_str in db.brandType:
                response = ""
                for id in db.brandType[brand_str]:
                    product_info = db.products.get(id)
                    response += f"({id}) {product_info['Name']}\n"
                if response == "":
                    response = "No products found for this brand."
                client.chat_postMessage(channel=channel_id, text=response)
            else:
                response = "No brand found with name: {}".format(brand_str)
                client.chat_postMessage(channel=channel_id, text=response)

        else:
            response = """
            Enter Valid Commands:
            cat:category_name - for a list of products under category name
            brand:brand_name - for a list of products under brand name
            id:id_number - for a detailed, multimedia view of product
            \n\n
            type /categories for a list of available categories
            type /brands for a list of available brand

            \n\n\n
            @about 
            This application serves as an interactive chatbot for querying a
            tailored database derived from the 'Smart Home' category of the Home Depot 
            website. Utilizing data scraping techniques, I accumulated an array of 
            products across a few subcategories to provide a comprehensive yet focused
            resource for users. Through seamless integration with Slack, the bot responds
            to specific commands, offering information such as product details, brands,
            and categories. This bot illustrates a creative approach to digital product
            building, effectively demonstrating data indexing and chatbot logic.
            """
            client.chat_postMessage(channel=channel_id, text=response)



##slashcommands

#/brands slash command: displays all product brands
@app.route('/brands', methods=['POST'])
def brand_command():
    data = request.form
    channel_id = data.get('channel_id')
    brands = db.get_brands()
    brands += "\n\n\n"
    brands += "View Products From Each Brand by entering brand:brand_name" 

    client.chat_postMessage(channel=channel_id, text=brands)

    return Response(), 200

#/categories slash command: displays all product categories
@app.route('/categories', methods=['POST'])
def category_command():
    data = request.form
    channel_id = data.get('channel_id')

    categories = db.get_categories()
    categories += "\n\n\n"
    categories += "View Products From Each Category by entering cat:category_name"  
    client.chat_postMessage(channel=channel_id, text=categories)

    return Response(), 200



if __name__ == "__main__":
    app.run(debug=True, port=5002)