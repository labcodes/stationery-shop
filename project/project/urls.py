"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView

frontend_urls = [
    re_path(r"^.*$", TemplateView.as_view(template_name="frontend/index.html")),
]

if not settings.DEBUG:
    frontend_urls.insert(0, path("", include("pwa.urls")))

# if you wish to test the PWA on dev, uncomment the following lines,
# so that django serves static files.
# remember to built the frontend manually and run collectstatic as well.
# from django.views.static import serve
# frontend_urls += [
#     re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})
# ]

urlpatterns = [
    path("admin/", admin.site.urls),
] + frontend_urls
