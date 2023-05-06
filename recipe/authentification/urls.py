from django.urls import path
from .views import signup,login_view,logout_view,profile_update,profile_detail

urlpatterns = [
    path('signUp/', signup, name='signUp'),
    path('signIn/', login_view, name='signIn'),
    path('profile/', profile_detail, name='profile'),
    path('profile/update/', profile_update, name='profile_update'),
    path('logout/', logout_view, name='logout'),
]   