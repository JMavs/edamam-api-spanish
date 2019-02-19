import json
import requests

class Edamam(object):
    def __init__(self, recipe_api_id=None, recipe_api_key=None):
        self.recipe_api_id = recipe_api_id
        self.recipe_api_key = recipe_api_key

    def search_recipes(self, query=None):
        url = "https://test-es.edamam.com/search"
        headers = {
                "Accept-encoding": "gzip"
                }
        params = {
                "q": query,
                "app_id": self.recipe_api_id,
                "app_key": self.recipe_api_key,
                }
        r = requests.get(url, headers=headers, params=params)
        return r.json()

    def analyze_meal(self, array_items=None):
        url = "https://wizard.edamam.com/api/wizard?perServing=true"
        headers = {
                "Accept-encoding": "gzip"
        }
        json_content = {
                "ingr": array_items,
                "title": "Recipe Title",
                "yield": 1
        }
        r = requests.post(url, headers=headers, json=json_content)
        print(json.dumps(r.json(), indent=4, sort_keys=True))
        return r.json()
