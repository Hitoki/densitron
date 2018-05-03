from django.conf.urls import url

from elastic_pages import views


urlpatterns = [
    url(r'^$', views.GlobalView.as_view(), name='home'),

    url(r'^terms-conditions/$', views.GlobalView.as_view(),
        name='terms_&_conditions'),

    url(r'^promotion/$', views.GlobalView.as_view(), name='promotion'),

    url(r'^privacy/$', views.GlobalView.as_view(), name='privacy'),

    url(r'^knowledge_base/$', views.GlobalView.as_view(),
        name='knowledge-base'),

    url(r'^contact/$', views.GlobalView.as_view(), name='contact'),

    url(r'^search_results/$', views.GlobalView.as_view(),
        name='search_results'),

    url(r'^product_found/$', views.GlobalView.as_view(),
        name='product_found'),

    # Products url set

    url(r'^products/$', views.GlobalView.as_view(),
        name='product-technology'),

    url(r'^products/(?P<technology>\w+)/(?P<category>\w+)/'
        r'(?P<product_id>\w+)/evaluation_kit/$',
        views.GlobalView.as_view(),
        name='product-product_detail_kit'),

    url(r'^products/(?P<technology>\w+)/(?P<category>\w+)/'
        r'(?P<product_id>\w+)/$',
        views.GlobalView.as_view(),
        name='product-product_detail'),

    url(r'^products/bespoke-orders/', views.GlobalView.as_view(),
        name='products-bespoke_orders'),

    url(r'^products/(?P<technology>\w+)/$', views.GlobalView.as_view(),
        name='product-technology_detail'),

    # Services url set

    url(r'^services/$', views.GlobalView.as_view(),
        name='services-service_list'),

    url(r'^services/(?P<service>.*)/$', views.GlobalView.as_view(),
        name='services-service_detail'),

    # Company url set

    url(r'^company/about_us/$', views.GlobalView.as_view(),
        name='company-about_us'),
    url(r'^company/our-people/$', views.GlobalView.as_view(),
        name='company-our_people'),

    url(r'^company/news/$', views.GlobalView.as_view(),
        name='company-news'),
    url(r'^company/news/(?P<id>\w+)/$', views.GlobalView.as_view(),
        name='company-news_detail'),

    url(r'^company/career_opportunities/$',
        views.GlobalView.as_view(),
        name='company-career_opportunities'),

    url(r'^company/(?P<company>.*)/$', views.GlobalView.as_view(),
        name='company-company_detail'),

    # Special pages

    url(r'^(?P<special_name>.*)/$', views.GlobalView.as_view(),
        name='special-special_page'),
    url(r'^(?P<special_name>.*)/(?P<special_2_name>.*)/',
        views.GlobalView.as_view(), name='special-special_2_page'),
]
