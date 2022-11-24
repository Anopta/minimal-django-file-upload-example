from django.urls import path
from . import views

urlpatterns = [
    # path('', my_view, name='my-view')
    path('', views.HomeView.as_view(), name='my-view'),
    path('create/', views.CreateFile.as_view(), name='my-create'),
    path('update/<int:pk>', views.UpdateFile.as_view(), name='my-update')

]
