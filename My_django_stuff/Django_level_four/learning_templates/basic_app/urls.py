from django.urls import path
from basic_app import views

#snoel template tagging
# here, the variable MUST be called app_name
app_name = 'basic_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]
