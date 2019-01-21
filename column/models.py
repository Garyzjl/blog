from django.db import models


class Column(models.Model):
    col = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='父节点', null=True)
    col_name = models.CharField(max_length=10, verbose_name='栏目名称')
    col_alias = models.CharField(max_length=20, verbose_name='栏目别名')
    key_word = models.CharField(max_length=10, verbose_name='关键字', null=True)
    describe = models.CharField(max_length=255, verbose_name='描述', null=True)

    class Meta:
        db_table = 'column'

