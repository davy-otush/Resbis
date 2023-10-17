from django.urls import path
from .import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('blogs/', views.BlogsView.as_view(), name='blogs'),
    path('services/', views.ServicesView.as_view(), name='services'),
    path('service/<str:slug>/', views.ServiceView.as_view(), name='service'),
    path('team/', views.TeamView.as_view(), name='team'),
    path('policies/', views.PoliciesView.as_view(), name='policies'),
    path('policy/<str:slug>/', views.PolicyView.as_view(), name='policy'),
    path('blog/<str:slug>/', views.BlogView.as_view(), name='blog'),
    path('requests/', views.RequestsView.as_view(), name='requests'),
    path('prices/', views.PricesView.as_view(), name='prices'),
]