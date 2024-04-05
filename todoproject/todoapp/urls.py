
from django.urls import path

from todoapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:taskid>', views.delete,name='delete'),
    path('edit/<int:id>/', views.edit,name='edit'),
    path('cbvhome/',views.todolistview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/', views.tododetailview.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.todoupdateview.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.tododeleteview.as_view(), name='cbvdelete'),
]
