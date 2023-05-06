import os
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests

from .models import Recipe


def get_recipes_info():
    # Extract course information from Martha Stewart website using BeautifulSoup
    urls = ["https://www.marthastewart.com/313844/chocolate-covered-strawberries", 
            "https://www.marthastewart.com/338930/chocolate-covered-almonds", 
            "https://www.marthastewart.com/350005/devils-food-cake-milk-chocolate-frosting"]
    recipes = []
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Get the recipe title
        title = soup.find('h1', {'class': 'comp type--lion article-heading mntl-text-block'}).text.strip()
        # Get the ingredients
        ingredients = []
        for li in soup.find_all('li', {'class': 'mntl-structured-ingredients__list-item'}):
            ingredients.append(li.text.strip())
       # Get the image URL
        
        # get the 'src' attribute of the img element
        img_url = soup.find('img', {'class': 'lazyload'})['data-src']
        img_name = os.path.basename(urlparse(img_url).path)
        if not os.path.exists('recipes/images'):
            os.makedirs('recipes/images')

        img_response = requests.get(img_url)

        with open(os.path.join('recipes/images', img_name), 'wb') as f:
            f.write(img_response.content) 
        Recipe.image = os.path.join('recipes/images', img_name) 
        Recipe.objects.create(title=title,  ingredients='\n'.join(ingredients))
        
       