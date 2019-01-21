from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from article.models import Article
from column.models import Column


def article(request):
    if request.method == 'GET':
        activate = 'article'
        articles = Article.objects.all()
        return render(request, 'article.html', {'activate': activate, 'articles': articles})


def add_article(request):
    if request.method == 'GET':
        categorys = Column.objects.all()
        return render(request, 'add-article.html', {'categorys': categorys})

    if request.method == 'POST':
        user = request.user
        title = request.POST.get('title')
        content = request.POST.get('content')
        keyword = request.POST.get('keywords')
        describe = request.POST.get('describe')
        image = request.FILES.get('titlepic')
        category = int(request.POST.get('category'))
        Article.objects.create(user_id=user.id, col_id=category, title=title, content=content, keyword=keyword,
                               image=image, describe=describe)
        return HttpResponseRedirect(reverse('article:article'))
