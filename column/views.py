from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from column.models import Column
from user.forms import ColumnForm


def category(request):
    if request.method == 'GET':
        categorys = Column.objects.all()
        activate = 'category'
        return render(request, 'category.html', {'categorys': categorys, 'activate': activate})

    if request.method == 'POST':
        form = ColumnForm(request.POST)
        fid = request.POST.get('fid')
        if form.is_valid():
            name = form.cleaned_data['name']
            alias = form.cleaned_data['alias']
            Column.objects.create(col_name=name, col_alias=alias, col_id=fid)
            return HttpResponseRedirect(reverse('column:category'))
        else:
            errors = form.errors
            return render(request, 'category.html', {'errors': errors})


@csrf_exempt
def del_col(request):
    if request.method == 'POST':
        id = request.POST.get('category_id')
        Column.objects.filter(pk=id).delete()
        return JsonResponse({'code': 200, 'msg': '请求成功'})


def change_col(request):
    if request.method == 'GET':
        id = request.GET.get('col_id')
        category = Column.objects.filter(pk=id).first()
        categorys = Column.objects.all()
        return render(request, 'update-category.html', {'categorys': categorys, 'category':category})

    if request.method == 'POST':
        id = request.GET.get('col_id')
        category = Column.objects.filter(pk=id).first()
        form = ColumnForm(request.POST)
        fid = request.POST.get('fid')
        keyword = request.POST.get('keywords')
        describe = request.POST.get('describe')
        if form.is_valid():
            name = form.cleaned_data['name']
            alias = form.cleaned_data['alias']
            category.col_name = name
            category.col_alias = alias
            category.col_id = fid
            category.key_word = keyword
            category.describe = describe
            category.save()
            return HttpResponseRedirect(reverse('column:category'))
        else:
            errors = form.errors
            return render(request, 'update-category.html', {'errors':errors})