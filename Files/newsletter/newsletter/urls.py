"""newsletter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from register import views as regv
from login import views as logv
from admin_panel import views as admv
from faculty_panel import views as facv
from newsletter import views
from django.conf import settings
from django.conf.urls.static import static
import random

randnum = random.randrange(99999)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', logv.login, name='login'),
    path('registration', regv.registration, name='registration'),
    path('test',logv.test, name='test'),
    path('logout', logv.logout, name='logout'),
    path('admin-panel', logv.login, name='admin-panel'),
    path('faculty-panel', logv.login, name='faculty-panel'),
    path('faculty-data-submitted', facv.submit_data, name='faculty-submit-data'),
    path('admin-data-submitted', admv.submit_data, name='admin-submit-data'),
    path('download-doc-'+str(randnum), views.download_doc, name='download'),


]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)