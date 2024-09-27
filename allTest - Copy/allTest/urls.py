from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.contrib.staticfiles.urls import static
from django.conf import settings




urlpatterns = [
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root' : settings.STATIC_ROOT }),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root' : settings.MEDIA_ROOT }),
    path('admin/', admin.site.urls),
    path('', include('first_app.urls'))



]
