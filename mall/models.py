import uuid
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from utils import constants
from system.models import Imagefile
from accounts.models import User


# Create your models here.

class Classify(models.Model):
    """商品分类"""
    uid = models.UUIDField('分类ID', default=uuid.uuid4, editable=True)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE)
    img = models.ImageField('分类主图', upload_to='classify')
    name = models.CharField('名称', max_length=12)
    desc = models.CharField('描述', max_length=64, null=True, blank=True)
    code = models.CharField('编码', max_length=32, null=True, blank=True)
    reorder = models.SmallIntegerField('排序', default=0)
    is_valid = models.BooleanField('是否有效', default=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        db_table = 'mall_classify'
        ordering = ['-reorder']


class Tag(models.Model):
    """商品标签"""
    uid = models.UUIDField('标签ID', default=uuid.uuid4, editable=True)
    img = models.ImageField('主图', upload_to='tags')
    name = models.CharField('名称', max_length=12)
    code = models.CharField('编码', max_length=32, null=True, blank=True)
    reorder = models.SmallIntegerField('排序', default=0)
    is_valid = models.BooleanField('是否有效', default=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        db_table = 'mall_tag'
        ordering = ['-reorder']


class Product(models.Model):
    """商品"""
    uid = models.UUIDField('商品ID', default=uuid.uuid4(), editable=False)
    name = models.CharField('商品名称', max_length=128)
    desc = models.CharField('简单描述', max_length=256, null=True, blank=True)
    content = models.TextField('商品描述')
    types = models.SmallIntegerField('商品类型', choices=constants.PRODUCT_TYPE_CHOICES,
                                     default=constants.PRODUCT_TYPE_ACTUAL)
    price = models.IntegerField('兑换价格（积分兑换）')
    origin_price = models.FloatField('原价')
    img = models.ImageField('主图', upload_to='product')
    buy_link = models.CharField('购买链接', max_length=256, null=True, blank=True)
    reorder = models.SmallIntegerField('排序', default=0)
    status = models.SmallIntegerField('商品状态', choices=constants.SLIDER_TYPES_CHOICES,
                                      default=constants.PRODUCT_STATUS_LOST)
    sku_count = models.IntegerField('库存', default=0)
    remain_count = models.IntegerField('剩余库存', default=0)
    view_count = models.IntegerField('浏览次数', default=0)
    score = models.FloatField('商品评分', default=10.0)
    is_valid = models.BooleanField('是否有效', default=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('修改时间', auto_now=True)

    tags = models.ManyToManyField(Tag, verbose_name='标签')
    classes = models.ManyToManyField(Classify, verbose_name='分类 ')

    banners = GenericRelation(Imagefile, verbose_name='banner图', related_query_name='banners')

    class Meta:
        db_table = 'mall_product'
        ordering = ['-reorder']


