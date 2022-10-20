from django.urls import path
from database import views

urlpatterns = [
  path('add path here', views.DataListView.as_view(), name="url"),
  path('add path here', views.DataCreateView.as_view(), name="url"),
  path('add path here /<pk>', views.DataUpdateView.as_view(), name="url"),
  path('add path here /<pk>', views.DataDeleteView.as_view(), name="url"),
]