import requests
from django.shortcuts import render

def index(request):
      # Fetch a random dog image
      response = requests.get("https://dog.ceo/api/breeds/image/random")
      dog_data = response.json()
      dog_image_url = dog_data['message']

      # Fetch a random joke
      joke_response = requests.get("https://v2.jokeapi.dev/joke/Any")
      joke_data = joke_response.json()
      joke_text = joke_data.get('setup', '') + " " + joke_data.get('delivery', joke_data.get('joke', ''))

      # Pass both the dog image URL and the joke text to the template
      return render(request, 'templates/index.html', {'dog_image_url': dog_image_url, 'joke': joke_text})
