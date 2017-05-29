from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import app.views

# Examples:
# url(r'^$', 'project.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', app.views.index, name='index'),
    url(r'^db', app.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
]
