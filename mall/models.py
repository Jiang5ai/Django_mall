import uuid
from django.db import models

from utils import constants


# Create your models here.


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

    class Meta:
        db_table = 'accounts_user_address'
        ordering = ['-reorder']
