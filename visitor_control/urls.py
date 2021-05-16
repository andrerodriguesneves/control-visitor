"""visitor_control URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

import visitor_control.users.views, visitor_control.core.views, visitor_control.visitors.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout', auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('', visitor_control.core.views.index, name='index'),
    path('users/', visitor_control.users.views.page_users ), 
    path('registrar-visitante', visitor_control.visitors.views.register_visitor, name="registrar_visitante"),
    path('visitantes/<int:id>/', visitor_control.visitors.views.visitor_information, name="informacoes_visitantes"),
    path('visitantes/<int:id>/finalizar-visita', visitor_control.visitors.views.visitor_finalization, name="finalizar_visitantes"),

]
