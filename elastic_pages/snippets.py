from django.core import urlresolvers


def get_choice_patterns():
    resolver = urlresolvers.get_resolver('elastic_pages.urls')
    patterns = sorted([
        (key, ' '.join(key.title().split('_')))
        for key, value in resolver.reverse_dict.items()
        if isinstance(key, str)
    ])
    return patterns


def get_header_menu_architect():
    """For selenium test"""
    resolver = urlresolvers.get_resolver('elastic_pages.urls')
    patterns = sorted([
        key for key, value in resolver.reverse_dict.items()
        if isinstance(key, str)
    ])
    pattern_dict = {}
    for item in patterns:
        it = item.split('-')
        if len(it) > 1:
            if it[0] in pattern_dict:
                pattern_dict[it[0]].append(it[1])
            else:
                pattern_dict.update({it[0]: [it[1]]})
        else:
            pattern_dict.update({it[0]: it[0]})
    return pattern_dict


def get_all_model_field_names(model):
    names = set()
    fields = model._meta.get_fields()
    for field in fields:
        # For backwards compatibility GenericForeignKey should not be
        # included in the results.
        if field.is_relation and field.many_to_one\
                and field.related_model is None:
            continue
        # Relations to child proxy models should not be included.
        if (field.model != model and
            field.model._meta.concrete_model == model._meta.concrete_model):
            continue
        names.add(field.name)
        if hasattr(field, 'attname'):
            names.add(field.attname)
    return list(names)


def calculate_paginate(num_list, num):
    num_changed_list = num_list
    if len(num_list) > 9:
        num_changed_list = num_list[:4]+['...']+num_list[-4:]
        if int(num) in num_list[4:-4]:
            num_changed_list = \
                num_list[:3]+['...']+[num]+['...']+num_list[-3:]
    return num_changed_list
