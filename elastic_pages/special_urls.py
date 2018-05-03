from django.conf.urls import url

from elastic_pages import views
from elastic_pages.views import RssSiteNewsFeed, csv_export
from products.views import ajax_product_filter, ajax_product_key_filter, \
    ajax_path_filter_sort, ajax_compare_product, ajax_email_message_create,\
    ajax_bespoke_order, ajax_update_country, ajax_download_docs

urlpatterns = [

    # AJAX url set
    url(r'^ajax/get-in-touch/', ajax_email_message_create,
        name='get_in_touch'),

    url(r'^ajax/product_filter/', ajax_product_filter,
        name='ajax_product_filter'),

    url(r'^ajax/product_key_filter/', ajax_product_key_filter,
        name='ajax_product_key_filter'),

    url(r'^ajax/path_filter_sort/', ajax_path_filter_sort,
        name='path_filter_sort'),

    url(r'^ajax/compare_product/', ajax_compare_product,
        name='compare_product'),

    url(r'^ajax/bespoke_orders/', ajax_bespoke_order,
        name='bespoke_order'),

    url(r'^ajax/update_country/', ajax_update_country,
        name='update_country'),

    url(r'^ajax/download_docs/', ajax_download_docs,
        name='download_docs'),

    # RSS
    url(r'^company/news/rss/$', RssSiteNewsFeed(),
        name='site_news_rss'),

    # CSV
    url(r'^csv_export/$', csv_export,
        name='csv_export'),

    # Test url set
    url(r'^page_not_found/$', views.Test404View.as_view(),
        name='page_not_found'),

]


handler404 = 'elastic_pages.views.handler404'