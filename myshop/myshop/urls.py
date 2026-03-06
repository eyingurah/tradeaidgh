"""myshop URL Configuration

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
from shop.views import *
from django.views.static import serve
#from django.conf.urls import url
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('corporate/', corporate, name='corporate'),
    path('income_project/', project_income, name='project_income'),
    path('bawemas_project/', project_bawemas, name='project_bawemas'),
    path('suscrib_project/', project_suscrib, name='project_suscrib'),
    path('ieow_project/', project_ieow, name='project_ieow'),
    path('sei_project/', project_sei, name='project_sei'),
    path('shine_project/', project_shine, name='project_shine'),
    path('isolve_project/', project_isolve, name='project_isolve'),
    path('coslec_project/', project_coslec, name='project_coslec'),
    path('impact/', impact, name='impact'),
    path('contribute/',contribute, name='contribute'),
    path('gift/', gift_card, name='gift_card'),
    path(r'^download/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
    path('catalogue.pdf', download_file, name='download_file'),
    path('COSLEC_Application_Form.pdf', coslec_form, name='coslec_form'),
    path('gallery/', gallery, name='gallery'),
    path('blog/', blog, name='blog'),
    path('blog-kayayei/', blog_kayayei, name='blog-kayayei'),
    path('blog-cftc/', blog_cftc, name='blog-cftc'),
    path('blog-environ/', blog_environ, name='blog-environ'),
    path('blog-call/', blog_call, name='blog-call'),
    path('blog-bicaf23/', blog_bicaf23, name='blog-bicaf23'),
    path('blog-25years/', blog_25years, name='blog-25years'),
    path('blog-25years2/', blog_25years2, name='blog-25years2'),
    path('media/', media, name='media'),
 ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
