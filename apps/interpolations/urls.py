from django.urls import path

from apps.interpolations import views

app_name = "interpolations"

urlpatterns = [
    path(
        'cubic-spline/',
        views.CubicSplineTemplateView.as_view(),
        name='cubic-spline'
    ),
    path(
        'lagrange/',
        views.LagrangeTemplateView.as_view(),
        name='lagrange'
    ),
    path(
        'lineal-spline/',
        views.LinealSplineTemplateView.as_view(),
        name='lineal-spline'
    ),
    path(
        'newton-interpolation/',
        views.NewtonInterpolationTemplateView.as_view(),
        name='newton-interpolation'
    ),
    path(
        'quadratic-spline/',
        views.QuadraticSplineTemplateView.as_view(),
        name='quadratic-spline'
    ),
    path(
        'vandermonde/',
        views.VandermondeTemplateView.as_view(),
        name='vandermonde'
    ),
]
