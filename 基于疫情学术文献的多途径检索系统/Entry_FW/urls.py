from django.urls import path
from . import views

## 指定url次级路径
app_name = 'Entry_FW'
urlpatterns = [
    path('', views.template_index, name='index'),
    path('abstract', views.abstractpage, name="abstract"),
    path('search', views.template_search, name='search'),
    path('search_class',views.template_search_class,name='search_class'),
    path('keywordmap', views.template_keywordmappage, name='keywordmap'),
    path('keywordrel_data', views.keywordmapdata, name='keywordrel_data'),
    path('research_detail',views.template_research_deatil,name='researhc_detail'),
    path('test', views.test, name='test_port'),
    path('request_doclist', views.request_doclist, name='request_doclist'),
    path('request_graph', views.request_graph, name='request_graph'),
    path('sta', views.sta, name='sta'),
    path('tupujiansuo', views.tupujiansuo, name='tupujiansuo'),

    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
]
