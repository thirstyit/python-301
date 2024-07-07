# Use your `Ingredients` class to create a URL to an online search
# that allows to look for recipes for dishes made from the
# available ingredients.

"""

Prepare for input into an ingredients class
Create a web scraper
connect web scraper results to database
create a way to search for ingredients (soup?)

"""


import sqlalchemy
import keys
from bs4 import BeautifulSoup
import requests

engine = sqlalchemy.create_engine('mysql+pymysql://'+ keys.root +':' + keys.pwd + '@localhost/recipes', echo=True)
connection = engine.connect()
metadata = sqlalchemy.MetaData()  
recipe_table = sqlalchemy.Table('recipe', metadata, autoload_with=engine)
ingredient_table = sqlalchemy.Table('ingredient', metadata, autoload_with=engine)

class Ingredient:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    
    
    def __str__(self):
        return f"You have {self.amount} {self.name}"
    
def getInput():
    ing = input("What is your ingredient?: ")
    amt = input("How many do you have?: ")

    i = Ingredient(ing, amt)
    return i

URL = 'https://codingnomads.github.io/recipes/'

def webScraper(URL):
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, features="html.parser")

    links = soup.find_all("a")

    r_id = 1
    i_id = 1     
    for link in links:
        recipe_name = link.string
        
        stmt = sqlalchemy.insert(recipe_table).values(recipeid=r_id, recipetitle=recipe_name)
        connection.execute(stmt)
        connection.commit()
        href_link = link['href']
                
        response = requests.get('https://codingnomads.github.io/recipes/' + href_link)
        soup = BeautifulSoup(response.text)
        ingredients = soup.find('ul')

        if ingredients:
            for ingredient in ingredients.find_all('li'):
                ingredient_text = ingredient.string
                #print(ingredient_text)
                stmt = sqlalchemy.insert(ingredient_table).values(ingredientid=i_id, recipeid=r_id, ingredienttext=ingredient_text)
                connection.execute(stmt)
                connection.commit()
                i_id+=1
    
        r_id+=1



#webScraper(URL)

enteredIngredient = getInput()

def findIngredient(e_ing):
    stmt = sqlalchemy.select(recipe_table.columns.recipetitle, ingredient_table.columns.ingredienttext).filter(ingredient_table.columns.ingredienttext.ilike("%{}%".format(e_ing.name))).where(recipe_table.columns.recipeid == ingredient_table.columns.recipeid)
    output = connection.execute(stmt)

    result_set = output.fetchall()  
    print(result_set)

findIngredient(enteredIngredient)

