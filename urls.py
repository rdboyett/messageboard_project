from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

#links to other views files
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'messageboard_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^google/', include('google_login.urls')),
    url(r'^class/', include('classrooms.urls')),
    url(r'^profile/', include('userInfo_profile.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#local views file
urlpatterns += patterns('messageboard_project.views',
    (r'^$', 'loginRedirect'),
    (r'^dashboard/$', 'dashboard'),
    (r'^dashboard/(?P<classID>\d+)/$', 'dashboard'),


    (r'^test/$', 'test'),
)
