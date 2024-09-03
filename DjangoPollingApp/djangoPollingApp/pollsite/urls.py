
from django.contrib import admin
from django.urls import include, path

admin.site.site_header = 'PollSite Admin'
admin.site.site_title = 'PollSite Admin Title'
admin.site.index_title = 'PollSite Administrator'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pollapp.urls'))
]
