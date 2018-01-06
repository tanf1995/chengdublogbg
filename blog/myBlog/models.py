# coding=utf-8
from django.db import models
from tinymce.models import HTMLField


# 分类
class Classify(models.Model):
    C_name = models.CharField(max_length=100)
    C_delete = models.BooleanField(default=False)  # 逻辑删除

    def __str__(self):
        return self.C_name.encode('utf-8')


# 文章
class Article(models.Model):
    A_author = models.CharField(max_length=100)
    A_pubTime = models.DateField(auto_now_add=True)
    A_title = models.CharField(max_length=400)
    A_clickNum = models.IntegerField(default=0)
    A_keyword = models.CharField(max_length=100, blank=True, null=True)
    A_cover = models.ImageField(upload_to='articleImg')  # 封面图, 设置默认图片
    A_content = models.TextField()  # 富文本编辑器的使用
    A_classify = models.ForeignKey(Classify)
    A_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.A_title.encode('utf-8')

    class Meta():
        ordering = ['-id']
        db_table = 'myBlog_article'


# 留言板
class Message(models.Model):
    M_author = models.CharField(max_length=100)
    M_content = models.CharField(max_length=4000)
    M_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.M_content[:10].encode('utf-8')

    class Meta():
        ordering = ['-id']


# 自己的记录
class Record(models.Model):
    R_pubTime = models.DateField(auto_now_add=True)
    R_content = models.CharField(max_length=4000)
    R_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.R_content[:10].encode('utf-8')
