from django.urls import path
from . import views

app_name='cms'

urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.create,name='create'),
    path('read/<int:post_id>',views.read,name='read'),
    path('update/<int:post_id>',views.update,name='update'),
    path('delete/<int:post_id>',views.delete,name='delete'), 
]