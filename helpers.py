#defines structure for detailed, multimedia view
def formulate_response(product_info):
    # Default values
    name = product_info.get('Name', 'Unknown')
    id = product_info.get('ID', 'Unknown')
    image = product_info.get('Image', 'https://via.placeholder.com/150')  # Link to a placeholder image
    category = product_info.get('Category', 'Unknown')
    brand = product_info.get('Brand', 'Unknown')
    price = product_info.get('Price', 'Unknown')
    ratings = product_info.get('Ratings', 'Unknown')
    url = product_info.get('URL', 'https://example.com')  # Link to a default webpage

    blocks = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*({id}) {name}*"
            }
        },
        {
            "type": "image",
            "image_url": image,
            "alt_text": name
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*Category:* {category}   *Brand:* {brand}"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*Price:* ${price}   *Ratings:* {ratings}"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"<{url}|Product Link>"
            }
        }
    ]
    return blocks