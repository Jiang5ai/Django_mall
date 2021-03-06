from django.shortcuts import render
from datetime import datetime

from system.models import Slider, News
from utils import constants


def index(request):
    """首页"""
    # 查询轮播图
    slider_list = Slider.objects.filter(types=constants.SLIDER_TYPE_INDEX)

    # 查询新闻
    now_time = datetime.now()
    # 置顶的 有效的 时间范围内的
    news_list = News.objects.filter(types=constants.NEWS_TYPE_NEW,
                                    is_top=True,
                                    is_valid=True,
                                    start_time__lte=now_time,
                                    end_time__gte=now_time)
    return render(request, 'index.html', {
        'slider_list': slider_list,
        'news_list': news_list,
    })
