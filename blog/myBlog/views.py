# coding=utf-8
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from models import *
from PIL import Image
import json
import time


# 主页
def index(request):
    newest_art = Article.objects.filter(A_delete=False)[:7]
    hottest_art = Article.objects.filter(A_delete=False).order_by('-A_clickNum')[:5]
    context = {'name': 'tf\'blog', 'newest_art': newest_art, 'hottest_art': hottest_art}
    return render(request, 'myBlog/index.html', context=context)


# 关于
def about(request):
    context = {'name': 'about me'}
    return render(request, 'myBlog/aboutMe.html', context=context)


# 生活文章分类页面
def life(request):
    life_classify = Classify.objects.get(C_name='生活')
    article_list = life_classify.article_set.filter(A_delete=False)
    newest_art = life_classify.article_set.filter(A_delete=False)[:7]
    hottest_art = life_classify.article_set.filter(A_delete=False).order_by('-A_clickNum')[:5]
    # 分页
    page_index = request.GET.get('page', '')
    p = Paginator(article_list, 8)  # 分页器
    if page_index == '':
        page_index = '1'
    page_index = int(page_index)  # 当前页页码
    article_list = p.page(page_index)  # 当前页列表
    list_range = p.page_range  # 页码列表

    context = {'name': 'life is like a bot', 'article_list': article_list,\
               'list_range': list_range, 'p': p, 'page_index': page_index,\
               'newest_art': newest_art, 'hottest_art': hottest_art}
    return render(request, 'myBlog/life.html', context=context)


# 技术文章
def technique(request):
    tech_classify = Classify.objects.get(C_name='技术分享')
    article_list = tech_classify.article_set.filter(A_delete=False)
    newest_art = tech_classify.article_set.filter(A_delete=False)[:7]
    hottest_art = tech_classify.article_set.filter(A_delete=False).order_by('-A_clickNum')[:5]
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
               'otherClass': 'tech', 'newest_art': newest_art, 'hottest_art': hottest_art}
    return render(request, 'myBlog/technique.html', context=context)


# web感悟
def feeling(request):
    feel_classify = Classify.objects.get(C_name='感悟')
    article_list = feel_classify.article_set.filter(A_delete=False)
    newest_art = feel_classify.article_set.filter(A_delete=False)[:7]
    hottest_art = feel_classify.article_set.filter(A_delete=False).order_by('-A_clickNum')[:5]
    # 分页
    page_index = request.GET.get('page', '')
    p = Paginator(article_list, 8)  # 分页器
    if page_index == '':
        page_index = '1'
    page_index = int(page_index)  # 当前页页码
    article_list = p.page(page_index)  # 当前页列表
    list_range = p.page_range  # 页码列表

    context = {'name': 'this is a question', 'article_list': article_list,
               'list_range': list_range, 'p': p, 'page_index': page_index,
               'newest_art': newest_art, 'hottest_art': hottest_art}
    return render(request, 'myBlog/webFeeling.html', context=context)


# 留言
def messages(request):
    newest_art = Article.objects.filter(A_delete=False)[:7]
    hottest_art = Article.objects.filter(A_delete=False).order_by('-A_clickNum')[:5]

    messages_list = Message.objects.filter(M_delete=False)
    user_name = request.session.get('user_name', '')
    # 分页
    page_index = request.GET.get('page', '')
    p = Paginator(messages_list, 8)  # 分页器
    if page_index == '':
        page_index = '1'
    page_index = int(page_index)  # 当前页页码
    messages_list = p.page(page_index)  # 当前页列表
    list_range = p.page_range  # 页码列表

    context = {'name': 'messages', 'newest_art': newest_art, 'hottest_art': hottest_art,
               'list_range': list_range, 'p': p, 'page_index': page_index,
               'messages_list': messages_list, 'user_name': user_name}
    return render(request, 'myBlog/messages.html', context=context)


# 提交留言
def messageHandler(request):
    name = request.POST.get('name', '')
    content = request.POST.get('content', '')
    if name:
        user_name = request.session.get('user_name', '')
        if name != user_name:
            request.session['user_name'] = name
    else:
        name = '匆匆过客'
        request.session['user_name'] = ''

    if content:
        message = Message()
        message.M_author = name
        message.M_content = content
        message.save()

    return HttpResponseRedirect(reverse('blog:messages'))


# 时光轴
def timeRecord(request):
    record = Record.objects.filter(R_delete=False).order_by('-R_pubTime')
    # 按时间分类展示
    list = []
    if len(record) != 0:
        inner_list = []
        year_value = record[0].R_pubTime.year
        inner_list.append(record[0])
        for i in range(1, len(record)):
            if record[i].R_pubTime.year != year_value:
                list.append([year_value, inner_list])
                inner_list = []
                year_value = record[i].R_pubTime.year
                inner_list.append(record[i])
            else:
                inner_list.append(record[i])
        list.append([year_value, inner_list])
    else:
        pass

    context = {'name': 'time is never stay', 'list': list}
    return render(request, 'myBlog/timeRecord.html', context=context)


# 单篇文章
def article(request, id):
    the_article = Article.objects.get(pk=id)
    the_article.A_clickNum += 1
    the_article.save()
    classify = the_article.A_classify
    newest_art = classify.article_set.all()[:7]
    hottest_art = classify.article_set.order_by('-A_clickNum')[:5]
    context = {'name': 'article', 'article': the_article, 'classify': classify,\
               'newest_art': newest_art, 'hottest_art': hottest_art}
    return render(request, 'myBlog/detail.html', context=context)


static_base = 'http://192.168.40.128:8080'
static_url = static_base + settings.MEDIA_URL  # 上传文件展示路径前缀


# 上传图片 POST
@csrf_exempt
def upload_img(request):
    file = request.FILES['file']
    data = {
        'error':True,
        'path':'',
    }
    if file:
        timenow = int(time.time()*1000)
        timenow = str(timenow)
        try:
            img = Image.open(file)
            img.save(settings.MEDIA_ROOT + "content/" + timenow + unicode(str(file)))
        except Exception,e:
            print e
            return HttpResponse(json.dumps(data), content_type="application/json")
        imgUrl = static_url + 'content/' + timenow + str(file)
        data['error'] = False
        data['path'] = imgUrl
    return HttpResponse(json.dumps(data), content_type="application/json")
