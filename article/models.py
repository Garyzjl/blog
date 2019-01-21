from django.db import models

from column.models import Column
from user.models import User


class Article(models.Model):
    """
    文章表
    """
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    col = models.ForeignKey(Column, verbose_name='栏目', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, verbose_name="文章标题", unique=True)
    label = models.CharField(max_length=20, verbose_name='标签', null=True)
    content = models.CharField(max_length=2048, verbose_name='文章内容')
    image = models.ImageField(max_length=5000, verbose_name='文章图片')
    keyword = models.CharField(max_length=10, verbose_name='关键字', null=True)
    describe = models.CharField(max_length=255, verbose_name='描述')

    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='发表时间')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'article'
