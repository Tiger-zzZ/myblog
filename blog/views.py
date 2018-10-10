from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.shortcuts import HttpResponse
from .models import *
from django.db.models import Q

from .forms import CommentForm


# Create your views here.
class Index(ListView):
    model = Article
    template_name = 'index.html'
    queryset = Article.objects.all().order_by('-id')
    paginate_by = 5


class CategoryList(ListView):
    model = Article
    template_name = 'category.html'
    paginate_by = 5

    def get_queryset(self):
        return Article.objects.filter(category=self.kwargs['category']).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.get(id=self.kwargs['category'])
        context['category'] = category.name
        return context



class Search(ListView):
    model = Article
    template_name = 'search.html'
    paginate_by = 5

    def get_queryset(self):
        key = self.request.GET['key']
        if key:
            return Article.objects.filter(Q(title__icontains=key)|Q(content__icontains=key)).order_by('-id')
        else:
            return ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = self.request.GET['key']
        return context


class ArticleDetail(DetailView):
    model = Article
    template_name = 'detail.html'

    def comment_sort(self,comments):
        self.comment_list = []
        self.top_level = []
        self.sub_level = {}
        for comment in comments:
            if comment.reply == None:
                self.top_level.append(comment)
            else:
                self.sub_level.setdefault(comment.reply.id,[]).append(comment)
        for top_menment in self.top_level:
            self.format_show(top_menment)
        return self.comment_list

    def format_show(self, top_comment):
        self.comment_list.append(top_comment)
        try:
            self.kids = self.sub_level[top_comment.id]
        except KeyError:
            pass
        else:
            for kid in self.kids:
                self.format_show(kid)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Comment.objects.filter(article=self.kwargs['pk'])
        context['comment_list'] = self.comment_sort(comments)
        comment_form = CommentForm()
        context['comment_form'] = comment_form
        return context

def pub_comment(request):  # 发布评论函数
    if request.method == 'POST':  # 如果是post请求
        comment = Comment()  # 创建评论对象
        comment.article = Article.objects.get(id=request.POST.get('article'))  # 设置评论所属的文章
        if request.POST.get('reply') != '0':  # 如果回复的不是文章而是他人评论
            comment.reply = Comment.objects.get(id=request.POST.get('reply'))  # 设置回复的目标评论
        form = CommentForm(request.POST, instance=comment)  # 将用户的输入和评论对象结合为完整的表单数据对象
        if form.is_valid():  # 如果表单数据校验有效
            try:
                form.save()  # 将表单数据存入数据库
                result = '200'  # 提交结果为成功编码
            except:  # 如果发生异常
                result = '100'  # 提交结果为失败编码

        else:  # 如果表单数据校验无效
            result = '100'  # 提交结果为失败编码
        return HttpResponse(result)  # 返回提交结果到页面
    else:  # 如果不是post请求
        return HttpResponse('非法请求！')  # 返回提交结果到页面