from django.urls import path

from .views import GetView, IncreaseView

app_name = "counter"

urlpatterns = [path("get", GetView.as_view(), name="get-counter"), path("increase", IncreaseView.as_view(), name="increase-counter")]
