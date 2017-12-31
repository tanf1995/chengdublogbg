# coding=utf-8
from django.shortcuts import render
from django.core.paginator import Paginator
from models import *


# 主页
def index(request):
    newest_art = Article.objects.all()[:7]
    context = {'name': 'tf\'blog', 'newest_art': newest_art}
    return render(request, 'myBlog/index.html', context=context)


# 关于
def about(request):
    context = {'name': 'about me'}
    return render(request, 'myBlog/aboutMe.html', context=context)


# 生活文章分类页面
def life(request):
    life_classify = Classify.objects.get(C_name='生活')
    article_list = life_classify.article_set.all()
    # 分页
    page_index = request.GET.get('page', '')
    p = Paginator(article_list, 8)  # 分页器
    if page_index == '':
        page_index = '1'
    page_index = int(page_index)  # 当前页页码
    article_list = p.page(page_index)  # 当前页列表
    list_range = p.page_range  # 页码列表

    context = {'name': 'life is like a bot', 'article_list': article_list,\
               'list_range': list_range, 'p': p, 'page_index': page_index}
    return render(request, 'myBlog/life.html', context=context)


# 技术文章
def technique(request):
    tech_classify = Classify.objects.get(C_name='技术分享')
    article_list = tech_classify.article_set.all()
    # 分页
    page_index = request.GET.get('page', '')
    p = Paginator(article_list, 8)  # 分页器
    if page_index == '':
        page_index = '1'
    page_index = int(page_index)  # 当前页页码
    article_list = p.page(page_index)  # 当前页列表
    list_range = p.page_range  # 页码列表

    context = {'name': 'make progress', 'article_list': article_list,\
               'list_range': list_range, 'p': p, 'page_index': page_index,\
               'otherClass': 'tech'}
    return render(request, 'myBlog/technique.html', context=context)


# web感悟
def feeling(request):
    feel_classify = Classify.objects.get(C_name='感悟')
    article_list = feel_classify.article_set.all()
    # 分页
    page_index = request.GET.get('page', '')
    p = Paginator(article_list, 8)  # 分页器
    if page_index == '':
        page_index = '1'
    page_index = int(page_index)  # 当前页页码
    article_list = p.page(page_index)  # 当前页列表
    list_range = p.page_range  # 页码列表

    context = {'name': 'this is a question', 'article_list': article_list,\
               'list_range': list_range, 'p': p, 'page_index': page_index}
    return render(request, 'myBlog/webFeeling.html', context=context)


# 留言
def messages(request):
    context = {'name': 'messages'}
    return render(request, 'myBlog/messages.html', context=context)


# 时光轴
def time(request):
    context = {'name': 'time is never stay'}
    return render(request, 'myBlog/timeRecord.html', context=context)


# 单篇文章
def article(request, id):
    the_article = Article.objects.get(pk=id)
    classify = the_article.A_classify
    context = {'name': 'article', 'article': the_article, 'classify': classify}
    return render(request, 'myBlog/detail.html', context=context)
