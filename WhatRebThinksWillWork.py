import requests
import pandas as pd
from flask import Flask, request, render_template, jsonify


###################################################
###################################################
###################################################
#   getIngredients()
###################################################
###################################################
##################################################

def getIngredients(query, cuisine):
    
    #######################################
    # consider separating this part into a function
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
    }
    
    headers = {
        'x-rapidapi-key': "9e12485098mshdefbf3ff62ef150p1717ddjsn1cf8f48a5741",
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
        }
    
    response = requests.get(url, headers=headers, params=querystring)
    
    response_json = response.json()
    
    results = response_json['results']
    
    # consider making everything above part of a separate function
    #######################################

    recipe_ingredients = []
    recipe_steps = []
    
    # ingredients stuff
    for result in results:
        try:
            recipe_id = result['id']
            recipe_title = result['title']        
            cooking_minutes = result['cookingMinutes']
            health_score = result['healthScore']
            source_url = result['sourceUrl']
            likes = result['aggregateLikes']                # Brooke modification / previously, it had been 'likes'
            # cuisine = result['cuisines'][0]                 # Brooke addition (my slicing may not work; my method used a df)
            calories_serving = result['calories']           # Brooke addition
            carbohydrates_serving = result['carbs']         # Brooke addition
            servings = result['servings']                   # Brooke addition

            analyzedInstructions = result['analyzedInstructions']
            
        except Exception as e:
            print('--- error with something ---')
            print(result.keys())
            continue 

        instruction_steps = analyzedInstructions[0]['steps']        # Brooke addition

        counter = 0                                                 # Brooke addition

        for item in instruction_steps:                              # Brooke addition
            counter = counter + 1                                   # Brooke addition
            step = item['step']                                     # Brooke addition
            numbered_step = f'{counter}. {step}'                    # Brooke addition
            recipe_steps.append(numbered_step)                      # Brooke addition
        
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

                    recipe_ingredients.append(recipe_ingredient)

    recipe_df = pd.DataFrame(recipe_ingredients)

    # dedupe ingredients df
    recipe_df.drop_duplicates(inplace=True)

    return recipe_df


###################################################
#####################
#####################
#   getRecipeMetadata
##################################################
##################################################
##################################################

def getRecipeMetadata(query, cuisine):
    
    #######################################
    # consider separating this part into a function
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
    }
    
    headers = {
        'x-rapidapi-key': "9e12485098mshdefbf3ff62ef150p1717ddjsn1cf8f48a5741",
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
        }
    
    response = requests.get(url, headers=headers, params=querystring)
    
    response_json = response.json()
    
    results = response_json['results']
    
    # consider making everything above part of a separate function
    #######################################

    recipe_metadata_list = []
    # recipe_steps = []
    
    # ingredients stuff
    for result in results:
        try:
            recipe_id = result['id']
            recipe_title = result['title']        
            cooking_minutes = result['cookingMinutes']
            health_score = result['healthScore']
            source_url = result['sourceUrl']
            likes = result['aggregateLikes']                # Brooke modification / previously, it had been 'likes'
            # cuisine = result['cuisines'][0]                 # Brooke addition (my slicing may not work; my method used a df)
            calories_serving = result['calories']           # Brooke addition
            carbohydrates_serving = result['carbs']         # Brooke addition
            servings = result['servings']                   # Brooke addition

            analyzedInstructions = result['analyzedInstructions']
            
        except Exception as e:
            print('--- error with something ---')
            print(result.keys())
            continue

        # 'directions': recipe_steps
        # # we need to figure out what this block is...
        # for result in results:
        #     servings = result['servings']     


        instruction_steps = analyzedInstructions[0]['steps']        # Brooke addition

        counter = 0
        
        recipe_steps = []                                                 # Brooke addition

        for item in instruction_steps:                              # Brooke addition
            counter = counter + 1                                   # Brooke addition
            step = item['step']                                     # Brooke addition
            numbered_step = f'{counter}. {step}'                    # Brooke addition
            recipe_steps.append(numbered_step)                      # Brooke addition
                    
        recipe_metadata = {
            'recipe_id': recipe_id,
            'recipe_title': recipe_title,
            'cooking_minutes': cooking_minutes,
            'health_score': health_score,
            'source_url': source_url,
            'likes': likes,
            'calories_serving': calories_serving,
            'carbohydrates_serving': carbohydrates_serving,
            'servings': servings,
            'recipe_steps': recipe_steps
        }

        # will need to rename this
        recipe_metadata_list.append(recipe_metadata)

    recipe_metadata_df = pd.DataFrame(recipe_metadata_list)

    # dedupe ingredients df
    # recipe_metadata_df.drop_duplicates(inplace=True)

    return recipe_metadata_df

app = Flask(__name__)

@app.route('/api/ingredients')
def ingredients():
    
    query = request.args.get('query')
    cuisine = request.args.get('cuisine')
    
    recipe_df = getIngredients(query, cuisine)
    
    recipe_json = recipe_df.to_json(orient='records')
    
    return recipe_json

@app.route('/api/recipemetadata')
def recipemetadata():
    
    query = request.args.get('query')
    cuisine = request.args.get('cuisine')
    
    recipe_df = getRecipeMetadata(query, cuisine)
    
    recipe_json = recipe_df.to_json(orient='records')
    
    return recipe_json

if __name__ == '__main__':
    app.run(debug=True)