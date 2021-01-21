from django.urls import path

from . import views
app_name = 'checklist'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:sets_id>/', views.setDetail, name='setDetail'),
    path('<int:sets_id>/<int:item_id>/', views.itemDetail, name='itemDetail')
]