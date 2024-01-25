from django.contrib import admin
from django.urls import path, include
from mainsite import views
from mainsite import urls as mainsite_urls
from accounts import urls as accounts_urls
from surveys import urls as surveys_urls
from django.contrib.auth.models import User, Group
from django.conf import settings
from django.conf.urls import include
try:
    from django.conf.urls import url
except ImportError:
    from django.urls import re_path as url
urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include(accounts_urls)),
    path('mainsite/', include(mainsite_urls)),
    path('surveys/', include(surveys_urls)),
    #path('custom-admin/', include(custom_admin_urls)),
    #path('survey/', include(survey_urls)),
]

if 'survey' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'^survey/', include('survey.urls'))
    ]

