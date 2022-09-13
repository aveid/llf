from django.urls import path
from . import views


urlpatterns = [
    path("registrations/", views.UserRegisterAPIView.as_view()),
    path("activation_code/<str:activation_code>/", views.Index.as_view(), name='activate_account')
]