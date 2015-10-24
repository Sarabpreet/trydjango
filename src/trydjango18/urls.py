from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^home/', 'feeds.views.home', name='home'),
    url(r'^resume/', 'feeds.views.resume', name='resume'),
    # url(r'/', 'feeds.views.home1', name='home1'),
    
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
