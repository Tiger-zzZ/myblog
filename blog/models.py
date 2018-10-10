from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):  # 文章类别
    id = models.IntegerField(primary_key=True)
    name = models.CharField('类别', max_length=20, unique=True)

    class Meta:
        verbose_name_plural = verbose_name = '类别'

    def __str__(self):
        return self.name


class Tag(models.Model):  # 文章标签
    name = models.CharField('标签', max_length=20, unique=True)

    class Meta:
        verbose_name_plural = verbose_name = '标签'

    def __str__(self):
        return self.name


class Article(models.Model):  # 文章
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='作者')
    title = models.CharField('标题', max_length=50)
    content = models.TextField('内容')
    pub_time = models.DateField('日期', auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=1, verbose_name='类别')
    tag = models.ManyToManyField(Tag, verbose_name='标签')

    class Meta:
        verbose_name_plural = verbose_name = '文章'

    def __str__(self):
        return self.title


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('昵称', max_length=20)
    email = models.EmailField('邮箱')
    content = models.TextField('内容')
    publish = models.DateField('时间', auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='文章')
    reply = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='回复')

    class Meta:
        verbose_name_plural = verbose_name = '评论'

    def __str__(self):
        return self.content
