from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name="index"),
    url(r'^ccm_cognitivo$', views.CCMCognitivo.as_view(), name="ccmcognitivo"),

]
