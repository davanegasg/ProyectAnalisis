from django.urls import path

from apps.functions.views import (
    BisectionTemplateView,
    IncrementalSearchTemplateView,
    FalseRuleTemplateView,
    MultipleRootsTemplateView,
    NewtonTemplateView,
    FixedPointTemplateView,
    SecantTemplateView
)

app_name = "functions"

urlpatterns = [
    path(
        'incremental-search/',
        IncrementalSearchTemplateView.as_view(),
        name='incremental-search'
    ),
    path(
        'bisection/',
        BisectionTemplateView.as_view(),
        name='bisection'
    ),
    path(
        'false-rule/',
        FalseRuleTemplateView.as_view(),
        name='false-rule'
    ),
    path(
        'newton/',
        NewtonTemplateView.as_view(),
        name='newton'
    ),
    path(
        'fixed-point/',
        FixedPointTemplateView.as_view(),
        name='fixed-point'
    ),
    path(
        'secant/',
        SecantTemplateView.as_view(),
        name='secant'
    ),
    path(
        'multipleroots/',
        MultipleRootsTemplateView.as_view(),
        name='multipleroots'
    ),
]
