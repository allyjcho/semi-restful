from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows/new', views.new),
    path('shows', views.shows),
    path('shows/create', views.create_show),
    path('shows/<int:id>', views.one_show),
    path('edit/<int:id>', views.show_edit_page),
    path('update/<int:id>', views.process_edit),
    path('shows/<int:id>/delete', views.delete_show)
]
