from django.urls import path
from apps.accounts.views import signin, signup, signout


urlpatterns = [
    path('register/', signup, name='register'),
    path('login/', signin, name='login'),
    path('logout/', signout, name='logout')
]
