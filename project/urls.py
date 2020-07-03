from django.contrib import admin
from django.urls import path, include
from bw2color import views

urlpatterns = [
    path('bw2color/', include('bw2color.urls')),
    path('admin/', admin.site.urls),
]
