from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from utils import constants


# Create your models here.
class CommonUtils(models.Model):
    start_time = models.DateTimeField('生效开始时间', null=True, blank=True)
    end_time = models.DateTimeField('生效结束时间', null=True, blank=True)
    reorder = models.SmallIntegerField('排序', default=0, help_text='数字越大，越靠前')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('最后修改时间', auto_now=True)
    is_valid = models.BooleanField('是否删除', default=True)

    class Meta:
        # 抽象模型 不会生成数据库表
        abstract = True


class Slider(CommonUtils):
    """系统轮播图"""
    name = models.CharField('名称', max_length=32)
    desc = models.CharField('描述', max_length=100, null=True, blank=True)
    types = models.SmallIntegerField('展现位置', choices=constants.SLIDER_TYPES_CHOICES,
                                     default=constants.SLIDER_TYPE_INDEX)
    img = models.ImageField('图片', upload_to='slider')
    target_url = models.CharField('跳转地址', max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'system_slider'
        ordering = ['-reorder']  # 按reorder降序排序


class News(CommonUtils):
    """新闻及通知"""
    types = models.SmallIntegerField('类型', choices=constants.NEWS_TYPES_CHOICES, default=constants.NEWS_TYPE_NEW)
    title = models.CharField('标题', max_length=255)
    content = models.TextField('内容')
    is_top = models.BooleanField('是否置顶', default=False)
    view_count = models.IntegerField('浏览次数', default=0)

    class Meta:
        db_table = 'system_news'
        ordering = ['-reorder']


class Imagefile(models.Model):
    """图片表"""
    img = models.ImageField('图片', upload_to='%Y%m/images/')
    summary = models.CharField('图片名称', max_length=200)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    is_valid = models.BooleanField('是否有效', default=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        db_table = 'system_images'
