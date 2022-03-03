from django.shortcuts import render
from .models import Article
# Create your views here.
def articles(request):
    article = Article.objects.all()
    return  render(request, 'magazine/magazine.html', context={
        "queryset":article
    })
