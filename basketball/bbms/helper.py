import math

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

PER_PAGE_COUNT = 10


def calculate_percentile(input_list, percent=90):
    if None in input_list:
        input_list = list(map(lambda ele: 0.0 if ele is None else ele, input_list))
    sorted_list = sorted(input_list)
    index = math.ceil(percent/100 * len(sorted_list))
    return sorted_list[index-1]


def populate_pagination(page, pagination_object):
    paginator = Paginator(pagination_object, PER_PAGE_COUNT)
    try:
        pagination_object = paginator.page(page)
    except PageNotAnInteger:
        pagination_object = paginator.page(1)
    except EmptyPage:
        pagination_object = paginator.page(paginator.num_pages)
    return pagination_object
