from django.conf.urls import url
from . import views
from .views import post_data, DataList, post_data_sdm, DataListSDM, DataListESPLast10



app_name = 'collectdata'

urlpatterns = [
    url(r'^esp/$', post_data, name="post_data"),
    url(r'^sdm/$', post_data_sdm, name="post_data_sdm"),
    url(r'^esp_data/$', DataList.as_view(), name="get_data"),
    url(r'^esp_last/$', DataListESPLast10.as_view(), name="get_data_esp_10"),
    url(r'^sdm_data/$', DataListSDM.as_view(), name="get_data_sdm"),
]