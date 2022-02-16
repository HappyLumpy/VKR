from django.urls import path
from . import views

app_name = 'map'
urlpatterns = [
    path('map/', views.mappoint, name='map'),
    path('mappoly/', views.mappoly, name='mappoly'),
    path('point/', views.PointView.as_view(), name='point'),
    path('concentrationpoints/', views.ConcentrationView.as_view(), name='concentrationpoints'),
    path('concentrationpoints1/', views.ConcentrationPointView.as_view(), name='ConcentrationPointView')
]
