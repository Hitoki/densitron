from django.forms.models import model_to_dict


def get_serialized_product_info(product):
    extra_data = {}
    data = {'Dimension WxHxD (mm)': product.get_dimension()}
    display_fields = [
        'size', 'viewing_angle', 'brightness', 'touch_points'
    ]
    special_value_field = [
        'dimension_w', 'dimension_h', 'dimension_d', 'active_area_w',
        'active_area_h', 'viewing_area_w', 'viewing_area_h', 'resolution_w',
        'resolution_h'
    ]
    fc_field = ['controller', 'touch', 'structure']
    mtom_field = ['features', 'interface', 'supported_os', 'tft_interface']

    for i in product._meta.get_all_field_names():
        if i in display_fields:
            extra_data = {
                product._meta.get_field(i).verbose_name:
                    model_to_dict(product)[i],
            }
        elif i in special_value_field:
            if i == 'dimension_w' or i == 'dimension_h' or i == 'dimension_d':
                extra_data = {
                    'Dimension WxHxD (mm)': product.get_dimension(),
                }
            elif i == 'active_area_h' or i == 'active_area_w':
                extra_data = {
                    'Active Area WxH (mm)': product.get_active_area(),
                }
            elif i == 'viewing_area_w' or i == 'viewing_area_h':
                extra_data = {
                    'Viewing Area WxH (mm)': product.get_viewing_area(),
                }
            elif i == 'resolution_w' or i == 'resolution_h':
                extra_data = {
                    'Resolution': product.get_resolution(),
                }
        elif i in fc_field:
            if i == 'controller' and product.controller:
                extra_data = {
                    product._meta.get_field(i).verbose_name:
                        product.controller.name,
                }
            if i == 'structure' and product.structure:
                extra_data = {
                    product._meta.get_field(i).verbose_name:
                        product.structure.name,
                }
            if i == 'touch' and product.touch:
                t_i_f = product.touch.touch_i_f.name\
                    if product.touch.touch_i_f else '-'

                extra_data.update({
                    'Touch Type': product.touch.type,
                    'Touch I/F': t_i_f,
                    'Touch Points': product.touch.points,
                })
        elif i in mtom_field:
            if i == 'features' and product.features.all():
                extra_data = {
                    product._meta.get_field(i).verbose_name: ', '.join(
                        feature.name for feature in
                        product.features.all()),
                }
            if i == 'interface' and product.interface.all():
                extra_data = {
                    product._meta.get_field(i).verbose_name: ', '.join(
                        interface.name for interface in
                        product.interface.all()),
                }
            if i == 'supported_os' and product.supported_os.all():
                extra_data = {
                    product._meta.get_field(i).verbose_name: ', '.join(
                        supported_os.name for supported_os in
                        product.supported_os.all()),
                }
            if i == 'tft_interface' and product.tft_interface.all():
                extra_data = {
                    product._meta.get_field(i).verbose_name: ', '.join(
                        tft_interface.name for tft_interface in
                        product.tft_interface.all()),
                }
        if extra_data and list(extra_data.values())[0]:
            data.update(extra_data)
    return data