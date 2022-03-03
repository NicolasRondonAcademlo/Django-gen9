from django.shortcuts import render

# Create your views here.
def index(request):
    favorite_person={
        "name": "Maria",
        "age": 24
    }
    return  render(request, 'restaurants/index.html', context=favorite_person)