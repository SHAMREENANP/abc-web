"""
URL configuration for samplework project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from sampleapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Itempage,name='Itempage'),
    path('Additem',views.Additem,name='Additem'),
    path('Itemlist',views.Itemlist,name='Itemlist'),
    path('Itemdetails/<int:id>', views.Itemdetails, name='Itemdetails'),
    path('editpage/<int:pk>',views.editpage,name='editpage'),
    path('edit_item/<int:pk>',views.edit_item,name='edit_item'),
    path('delete/<int:pk>',views.delete,name='delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
