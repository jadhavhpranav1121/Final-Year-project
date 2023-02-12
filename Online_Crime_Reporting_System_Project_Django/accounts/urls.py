from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from django.conf.urls import handler404, handler500, handler403, handler400

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('settings/<int:pk>', views.AccountSettings.as_view(), name='settings'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
]
handler404 = "accounts.views.page_not_found_view"