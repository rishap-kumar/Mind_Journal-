from django.contrib import admin
from django.urls import path
from journal import views
urlpatterns = [
    path('save_journal/',views.save_journal,name='savedata'),
    path('view_journal/',views.view_journal,name='viewjournal'),
    path('update_journal/',views.update_journal,name='updatedata'),
    path('update/',views.update,name='update'),
    path('deletedata/',views.delete_data,name='deletedata'),
    path('login_page/',views.login_page,name='login'),
    path('signup_page/',views.signup_page,name='signup'),
    path('saveuser/',views.saveuser,name='saveuser'),
    path('Authenticateuser/',views.check_login,name='authenticate'),
    path('logout/',views.user_logout,name='logout'),


]