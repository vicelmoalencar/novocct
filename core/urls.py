from django.urls import path
from .views import HomeView, AboutView, ContactView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('sobre/', AboutView.as_view(), name='about'),
    path('contato/', ContactView.as_view(), name='contact'),
]
