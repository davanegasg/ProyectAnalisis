from django.urls import path

from apps.home.views import HomeTemplateView, TestWithValuesTemplateView

app_name = "home"

urlpatterns = [
    path(
        '',
        HomeTemplateView.as_view(),
        name='index',
    ),
    path(
        'tests',
        TestWithValuesTemplateView.as_view(),
        name='tests',
    ),
]
