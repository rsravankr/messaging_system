# api/urls.py
from django.urls import path
from .views import RegisterAPI, LoginAPI, SendMessageAPI, MessageThreadAPI, SearchMessagesAPI
from knox import views as knox_views

urlpatterns = [
    path('auth/register/', RegisterAPI.as_view(), name='register'),
    path('auth/login/', LoginAPI.as_view(), name='login'),
    path('auth/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('auth/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]

urlpatterns += [
    path('messages/send/', SendMessageAPI.as_view(), name='send-message'),
    path('messages/thread/<int:user_id>/', MessageThreadAPI.as_view(), name='message-thread'),
]

urlpatterns += [
    path('messages/search/<int:user_id>/', SearchMessagesAPI.as_view(), name='search-messages'),
]
