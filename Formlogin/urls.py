
from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.render_login, name='render_login'),
    path('login', views.perform_login, name='perform_login'),
    path('logout/', views.perform_logout , name='perform_logout'),
    path('admin_dashboard/',views.admin_dashboard, name='admin_dashboard' )

]
