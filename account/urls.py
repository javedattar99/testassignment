




from django.urls import path
from .views import login_page,logout_page,signup

app_name = 'account'

urlpatterns = [
     path('login/', login_page, name='login'),
     path('logout/', logout_page, name='logout'),
     path('signup/', signup, name='signup'),
]
