# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 19:08:02 2021
​
@author: RebekahDSK
"""
​
import requests
import pandas as pd
​
url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/complexSearch"
​
querystring = {"limitLicense": "<REQUIRED>",
	"offset": "0",
	"number": "10",
	"query": "burger",
	"cuisine": "american",
    "addRecipeInformation": "True",
	"includeIngredients": "onions, lettuce, tomato",
	"excludeIngredients": "coconut, mango",
	"intolerances": "peanut, shellfish",
	"type": "main course",
	"ranking": "2",
	"minCalories": "150",
	"maxCalories": "1500",
	"minFat": "5",
	"maxFat": "100",
	"minProtein": "5",
	"maxProtein": "100",
	"minCarbs": "5",
	"maxCarbs": "100",} ### CHANGE INGREDIENT TO WHAT YOU WANT
​
headers = {
    'x-rapidapi-key': "9e12485098mshdefbf3ff62ef150p1717ddjsn1cf8f48a5741",
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }
​
response = requests.request("GET", url, headers=headers, params=querystring)
​
print(response.text)
​
​
list1 = response.json()
​
df =pd.DataFrame(list1)
​
#unpack columns in dataframe
​
def unpack(df, column, fillna=None):
    ret = None
    if fillna is None:
        ret = pd.concat([df, pd.DataFrame((d for idx, d in df[column].iteritems()))], axis=1)
        del ret[column]
    else:
        ret = pd.concat([df, pd.DataFrame((d for idx, d in df[column].iteritems())).fillna(fillna)], axis=1)
        del ret[column]
    return ret
​
df1 = unpack(df, 'results', 0)
df2=  unpack(df1, 0, 0)