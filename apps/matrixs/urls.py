from django.urls import path

from apps.matrixs.views import (
    CholeskyTemplateView,
    CroutTemplateView,
    DoolittleTemplateView,
    GaussSeidelTemplateView,
    GaussianEliminationWithPartialPivotingTemplateView,
    GaussianEliminationWithTotalPivotingTemplateView,
    GaussianSimpleEliminationTemplateView,
    JacobiTemplateView,
    LUWithPartialPivotingTemplateView,
    LUwithGaussianSimpleEliminationTemplateView,
    SorTemplateView, 
    
)

app_name = "matrixs"

urlpatterns = [
    path(
        'cholesky/',
        CholeskyTemplateView.as_view(),
        name='cholesky'
    ),
    path(
        'crout/',
        CroutTemplateView.as_view(),
        name='crout'
    ),
    path(
        'doolittle/',
        DoolittleTemplateView.as_view(),
        name='doolittle'
    ),
    
    path(
        'gaussian-elimination-with-partial-pivoting/',
        GaussianEliminationWithPartialPivotingTemplateView.as_view(),
        name='gaussian-elimination-with-partial-pivoting'
    ),
    path(
        'gaussian-elimination-with-total-pivoting/',
        GaussianEliminationWithTotalPivotingTemplateView.as_view(),
        name='gaussian-elimination-with-total-pivoting'
    ),
    path(
        'gaussian-simple-elimination/',
        GaussianSimpleEliminationTemplateView.as_view(),
        name='gaussian-simple-elimination'
    ),
    path(
        'gauss-seidel/',
        GaussSeidelTemplateView.as_view(),
        name='gauss-seidel'
    ),
    path(
        'jacobi/',
        JacobiTemplateView.as_view(),
        name='jacobi'
    ),
    path(
        'lu-with-partial-pivoting/',
        LUWithPartialPivotingTemplateView.as_view(),
        name='lu-with-partial-pivoting'
    ),
    path(
        'lu-with-gaussian-simple-elimination/',
        LUwithGaussianSimpleEliminationTemplateView.as_view(),
        name='lu-with-gaussian-simple-elimination'
    ),
    path(
        'sor/',
        SorTemplateView.as_view(),
        name='sor'
    ),
]
