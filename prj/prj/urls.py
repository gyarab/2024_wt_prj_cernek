"""
URL configuration for prj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.views.generic import TemplateView
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('seznam-potravin', views.foods),
    path('seznam-jidel', views.meals),
    path('potraviny-v-souctu', views.weighted_foods),
    path('kalkulacka-dennich-kalorii',TemplateView.as_view(template_name='main/idealni-kalorie-kalkulacka.html')),
    path('test',TemplateView.as_view(template_name='main/detail-potraviny.html')),
    path('detail-potraviny/<int:food_id>', views.food_detail, name='food_detail'),
    path('pridani-potraviny',TemplateView.as_view(template_name='main/pridani-potraviny.html')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
