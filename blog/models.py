from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    qq = models.CharField(max_length=10)
    addr = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    score = models.IntegerField()  # 文章的打分
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

'''
查看 Django queryset 执行的 SQL:
print(Author.objects.all().query)

values_list 获取元组形式结果：
Author.objects.values('name', 'qq')

values 获取字典形式的结果：
Author.objects.values('name', 'qq')

extra 实现 别名，条件，排序等：
tags = Tag.objects.all().extra(select={'tag_name': 'name'})

annotate 聚合 计数，求和，平均数等：
计数
Article.objects.all().values('author__name').annotate(count=Count('author')).values('author__name', 'count')
求和、平均值
Article.objects.values('author__name').annotate(sum_score=Sum('score')).values('author__name', 'sum_score')
Article.objects.values('author_id').annotate(avg_score=Avg('score')).values('author_id', 'avg_score')

select_related 优化一对一，多对一查询:(本质上就是使用了多表查询)
articles = Article.objects.all().select_related('author')[:10]

prefetch_related 优化一对多，多对多查询:
articles = Article.objects.all().prefetch_related('tags')[:10]

defer 排除不需要的字段:
在复杂的情况下，表中可能有些字段内容非常多，取出来转化成 Python 对象会占用大量的资源。
这时候可以用 defer 来排除这些字段，比如我们在文章列表页，只需要文章的标题和作者，没有必要把文章的内容也获取出来（因为会转换成python对象，浪费内存）
Article.objects.all().defer('content')

only 仅选择需要的字段:
Author.objects.all().only('name')

自定义聚合功能:
GROUP_CONCAT

'''