# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
import pandas as pd
from flask import Flask, request, render_template, jsonify

# %%

def queryRecipeEndpoint(query, cuisine):

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/searchComplex"
    
    # these will come from form controls
    query = query
    cuisine = cuisine
    type_of_recipe = 'main course'
    ranking = "2"
    minCalories = "150"
    maxCalories = "1500"
    minFat = "5"
    maxFat = "100"
    minProtein = "5"
    maxProtein = "100"
    minCarbs = "5"
    maxCarbs = "100"
    
    querystring = {"limitLicense": "<REQUIRED>",
        "offset": "0",
        "number": "10",
        "query": query,
        "cuisine": cuisine,
        #"includeIngredients": "onions, lettuce, tomato",
        #"excludeIngredients": "coconut, mango",
        #"intolerances": "peanut, shellfish",
        "type": type_of_recipe,
        "ranking": ranking,
        "minCalories": minCalories,
        "maxCalories": maxCalories,
        "minFat": minFat,
        "maxFat": maxFat,
        "minProtein": minProtein,
        "maxProtein": maxProtein,
        "minCarbs": minCarbs,
        "maxCarbs": maxCarbs,
        "instructionsRequired": "True",
        "addRecipeInformation": "True",
        "fillIngredients": "True",
    };

    headers = {
        'x-rapidapi-key': ,
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
        }
    
    response = requests.get(url, headers=headers, params=querystring)
    
    response_json = response.json()
    
    results = response_json['results']
    
    recipe_ingredients = []
    
    
    # ingredients stuff
    for result in results:
        recipe_id = result['id']
        recipe_title = result['title']
            
        analyzedInstructions = result['analyzedInstructions']
        
        for instruction in analyzedInstructions:
            
            steps = instruction['steps']
            
            for step in steps:
                
                ingredients = step['ingredients']
                
                for ingredient in ingredients:
                    
                    ingredient_name = ingredient['name']
                    
                    recipe_ingredient = {
                        'recipe_id': recipe_id,
                        'recipe_title': recipe_title,
                        'ingredient_name': ingredient_name
                    }
                    
                    # check to see if the ingredient is already attached a recipe
                    # if not, append it... if so, dont
                    recipe_ingredients.append(recipe_ingredient)
                    
    recipe_df = pd.DataFrame(recipe_ingredients)
    recipe_df.drop_duplicates(inplace=True)
    
    return recipe_df

# %%



# %%
# Flask shit

app = Flask(__name__)

@app.route('/api/ingredients')
def ingredients():
    
    query = request.args.get('query')
    cuisine = request.args.get('cuisine')
    
    recipe_df = queryRecipeEndpoint(query, cuisine)
    
    recipe_json = recipe_df.to_json(orient='records')
    
    return recipe_json

# %%
    
if __name__ == '__main__':
    app.run(debug=True)