from django.db import models


# Create your models here.

# 导航栏和添加字段设置
class book(models.Model):
    # 点击左侧导航栏添加出现在中间
    title = models.CharField(max_length=20, verbose_name='图书名称')
    publishdate = models.DateField(verbose_name='出版日期')
    publishing = models.ForeignKey(to='publishing', on_delete=models.CASCADE, verbose_name='出版社')
    author = models.ManyToManyField(to='author', verbose_name='作者')  # 多对多键
    descript = models.TextField(verbose_name='书籍简介')

    class Meta:
        verbose_name = '图书基本信息'  # 右侧添加按钮
        verbose_name_plural = '图书信息'  # 左侧导航栏

    # 添加成功上方提示
    def __str__(self):
        return self.title + '--相关图书信息'  # 成功添加了图书基本信息“Django 实战--相关图书信息”。


class publishing(models.Model):
    name = models.CharField(max_length=20, verbose_name='出版社名称')
    address = models.CharField(max_length=20, verbose_name='出版社地址')

    class Meta:
        verbose_name = '出版社信息'
        verbose_name_plural = '出版社图书信息'

    def __str__(self):
        return '社名：' + self.name


class author(models.Model):
    name = models.CharField(max_length=35, verbose_name='姓名')
    email = models.EmailField(verbose_name='邮箱地址')
    birthday = models.DateField(verbose_name='出生日期')
    header = models.ImageField(verbose_name='作者头像')

    class Meta:
        verbose_name = '作者基本情况'
        verbose_name_plural = '作者基本信息'

    def __str__(self):
        return '作者：' + self.name
