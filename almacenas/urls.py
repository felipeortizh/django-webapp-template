from django.urls import path
#from .views import uploads
from .views import StoragePageView
#from .almacenas import views

urlpatterns = [
    path("", StoragePageView.as_view(), name="uploads"),
]

#path("almacenas/", views.uploads, name="uploads"),