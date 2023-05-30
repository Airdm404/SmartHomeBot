import json

# Load JSON data
with open("homedepotData.json", "r") as read_file:
    data = json.load(read_file)

# Create a new dictionary where the keys are product IDs
products = {item['ID']: {**item, 'Brand': item['Brand'] or 'Unknown'} for item in data}


brands = list(set(product['Brand'] for product in products.values()))
categories = list(set(product['Category'] for product in products.values()))

catType = {}
for id, product in products.items():
    cat = product['Category'].lower()
    if cat not in catType:
        catType[cat] = [id]
    else:
        catType[cat].append(id)

brandType = {}
for id, product in products.items():
    brand = product['Brand'].lower()
    if brand not in brandType:
        brandType[brand] = [id]
    else:
        brandType[brand].append(id)


def get_brands():
     return '\n'.join(brands)

def get_categories():
     return '\n'.join(categories)

