from django.urls import path
from .views import PluginList, PluginRun, PluginInstall

urlpatterns = [
    path("list/", PluginList.as_view()),
    path("run/<str:name>/", PluginRun.as_view()),
    path("install/", PluginInstall.as_view()),
]
