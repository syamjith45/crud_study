from django.urls import path
from . import views
urlpatterns = [
    path('',views.create,name='create'),
    path('list/',views.list,name='list'),
    path('edit/<int:pk>/',views.edit,name='edit'),
    path('delete/<int:pk>',views.delete_record,name='delete')
]
