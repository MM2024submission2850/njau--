"""Knowledge_map URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.Entry_FW, name='Entry_FW')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='Entry_FW')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Entry_FW.urls')),  # index home
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns=[
        path('__debug__/',include(debug_toolbar.urls)),
    ]+urlpatterns
