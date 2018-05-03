import collections

from datetime import datetime
from decimal import Decimal as D


def serialize_sort_data(data):
    touch, mapping, q = '', {}, ''

    for key, value in data.items():
        if value.lower() == 'true' and key.lower() != 'touch':
             mapping[key] = True
        elif value.lower() == 'false' and key.lower() != 'touch':
            if key.lower() == 'colour':
                mapping['colour__isnull'] = 'True'
            else:
                mapping[key] = False
        elif value.lower() == 'true' and key.lower() == 'touch':
            touch = 'True'
        elif value.lower() == 'false' and key.lower() == 'touch':
            touch = 'False'
        elif key.lower().startswith('dimension') and value != '':
            mapping[key] = D(value)
        elif key.lower() == 'technology':
            mapping['category__technology__id'] = value
        elif key.lower() == 'q':
            q = value
        elif value != '':
            mapping[key] = value
    return mapping, touch, q


def get_news_map(queryset):
    data = {}
    dates = queryset.dates('publicated', 'day', order='DESC')
    for item in dates:
        data[item.year] = list(set(
            [datetime.strftime(x, '%B') for x in dates if x.year == item.year]
        ))
    for key, values in data.items():
        data[key] = {}
        for value in values:
            data[key].update({value: list(set(
                [x.day for x in dates
                 if x.year == key and datetime.strftime(x, '%B') == value]
            ))})
    return collections.OrderedDict(reversed(sorted(data.items())))