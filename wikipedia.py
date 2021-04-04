import requests

url = "https://cat-fact.herokuapp.com/facts/random"
cat_api_url = "https://api.thecatapi.com/v1/images/search"

data = requests.get(url)
cleaned = data.json()
print(cleaned['text'])

cat_data = requests.get(cat_api_url)
cleaned_cat = cat_data.json()
print(cleaned_cat)