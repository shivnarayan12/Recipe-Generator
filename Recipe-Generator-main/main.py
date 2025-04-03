import os
import urllib.parse
import json
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from datetime import datetime

# API Initialization
def recipe_search(ingredient):
    api_key = '7a7cd9b85dd6e0d516903b7c2d582bfa'  # Replace with your Edamam API key
    application_id = 'a720f909'  # Replace with your Edamam Application ID

    # URL Encoding to handle spaces and special characters
    encoded_ingredient = urllib.parse.quote(ingredient)

    # Correct API URL
    url = f'https://api.edamam.com/api/recipes/v2?type=public&app_id={application_id}&app_key={api_key}&q={encoded_ingredient}'

    try:
        # Opening the URL
        result = urlopen(url)

        # Converting the information to JSON format
        data = json.load(result)

        # Ensure 'hits' key exists, otherwise return an empty list
        return data.get('hits', [])

    except HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
    except URLError as e:
        print(f"URL Error: {e.reason}")
    except json.JSONDecodeError:
        print("Error parsing JSON response from API.")

    return []  # Return empty list if there was an error


# User Inputs the ingredient
ingredient = input('Enter an ingredient: ')

# Renaming the File to the ingredient 
opname = ingredient.replace(" ", "_") + '-recipes.txt'  # Replace spaces with underscores

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the script directory
outFileName = os.path.join(script_dir, opname)  # Save file in the same folder

# Creating the File with Encoding
report = open(outFileName, "w", encoding="utf-8")

# Date and Time
now = datetime.now()
dt = now.strftime("%d/%m/%Y %H:%M:%S")

# API Call
hits = recipe_search(ingredient)

# Heading the Text File
report.write(f"-------------------------------------------- Recipe Generated From {ingredient} --- {dt} --------------------------\n\n")

# Loop for Searching Recipes
if hits:
    for single_hit in hits:
        recipe_json = single_hit['recipe']
        report.write(str(recipe_json['label']) + '\n')
        report.write("Ingredients:\n" + "\n".join(recipe_json['ingredientLines']) + '\n')
        report.write("Diet Labels: " + ", ".join(recipe_json.get('dietLabels', [])) + '\n')
        report.write('-' * 150 + '\n\n')
else:
    report.write("No recipes found for the given ingredient.\n")

print(f'File saved at: {outFileName}')

# Closing the File
report.close()
